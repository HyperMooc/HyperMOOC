import os
import xml.etree.ElementTree as ET
import cv2
import numpy as np
import argparse
from pathlib import Path

# 解析命令行参数
def parse_args():
    parser = argparse.ArgumentParser(description='生成带有标注框的图像')
    parser.add_argument('--xml-dir', type=str, help='XML 文件目录')
    parser.add_argument('--img-dir', type=str, help='原始图像目录')
    parser.add_argument('--output-dir', type=str, help='输出图像目录')
    parser.add_argument('--box-color', type=str, default='red', help='标注框颜色 (red, green, blue)')
    parser.add_argument('--box-thickness', type=int, default=2, help='标注框线宽')
    parser.add_argument('--font-scale', type=float, default=0.7, help='字体大小')
    return parser.parse_args()

def get_color(color_name):
    """将颜色名称转换为 BGR 值"""
    colors = {
        'red': (0, 0, 255),
        'green': (0, 255, 0),
        'blue': (255, 0, 0),
        'yellow': (0, 255, 255),
        'cyan': (255, 255, 0),
        'magenta': (255, 0, 255),
        'white': (255, 255, 255),
        'black': (0, 0, 0)
    }
    return colors.get(color_name.lower(), (0, 0, 255))  # 默认红色

def parse_xml(xml_path):
    """解析 XML 文件，提取标注信息"""
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    # 获取图像路径
    image_path = root.find('path').text
    
    # 提取标注信息
    annotations = []
    for obj in root.findall('object'):
        name = obj.find('name').text
        bndbox = obj.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)
        
        annotations.append({
            'name': name,
            'box': (xmin, ymin, xmax, ymax)
        })
    
    return image_path, annotations

def draw_annotations(image, annotations, box_color=(0, 0, 255), box_thickness=2, font_scale=0.7):
    """在图像上绘制标注框"""
    for anno in annotations:
        name = anno['name']
        xmin, ymin, xmax, ymax = anno['box']
        
        # 绘制矩形框
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), box_color, box_thickness)
        
        # 绘制标签背景
        text_size = cv2.getTextSize(name, cv2.FONT_HERSHEY_SIMPLEX, font_scale, box_thickness)[0]
        cv2.rectangle(image, (xmin, ymin - text_size[1] - 10), (xmin + text_size[0] + 10, ymin), box_color, -1)
        
        # 绘制标签文字
        cv2.putText(image, name, (xmin + 5, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), box_thickness)
    
    return image

def process_images(xml_dir, img_dir, output_dir, box_color=(0, 0, 255), box_thickness=2, font_scale=0.7):
    """处理所有图像和 XML 文件"""
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 获取所有 XML 文件
    xml_files = [f for f in os.listdir(xml_dir) if f.endswith('.xml')]
    
    for xml_file in xml_files:
        xml_path = os.path.join(xml_dir, xml_file)
        
        try:
            # 解析 XML 文件
            image_path, annotations = parse_xml(xml_path)
            
            # 处理图像路径
            # 如果是相对路径，则相对于 xml_dir 解析
            if not os.path.isabs(image_path):
                # 从 XML 中提取的路径可能是 ../assets/corpusImages/T1.png 格式
                # 我们需要提取文件名部分
                img_filename = os.path.basename(image_path)
                image_path = os.path.join(img_dir, img_filename)
            
            # 检查图像文件是否存在
            if not os.path.exists(image_path):
                # 尝试使用 XML 文件名（不含扩展名）+ .png
                base_name = os.path.splitext(xml_file)[0]
                image_path = os.path.join(img_dir, f"{base_name}.png")
                
                if not os.path.exists(image_path):
                    print(f"警告: 找不到图像文件 {image_path}")
                    continue
            
            # 读取图像
            image = cv2.imread(image_path)
            if image is None:
                print(f"警告: 无法读取图像 {image_path}")
                continue
            
            # 绘制标注
            labeled_image = draw_annotations(image.copy(), annotations, box_color, box_thickness, font_scale)
            
            # 保存带标注的图像
            output_filename = os.path.basename(image_path)
            output_path = os.path.join(output_dir, output_filename)
            cv2.imwrite(output_path, labeled_image)
            
            print(f"已处理: {xml_file} -> {output_filename}")
            
        except Exception as e:
            print(f"处理 {xml_file} 时出错: {e}")

if __name__ == "__main__":
    args = parse_args()
    
    # 设置默认目录路径
    base_dir = Path(__file__).parent.parent  # 项目根目录
    xml_dir = args.xml_dir if args.xml_dir else base_dir / "src" / "assets" / "corpusXml"
    img_dir = args.img_dir if args.img_dir else base_dir / "src" / "assets" / "corpusImages"
    output_dir = args.output_dir if args.output_dir else base_dir / "src" / "assets" / "corpusImagesLabel"
    
    # 获取颜色
    box_color = get_color(args.box_color)
    
    # 处理图像
    process_images(xml_dir, img_dir, output_dir, box_color, args.box_thickness, args.font_scale)
    print(f"所有标注图像已保存到 {output_dir}") 