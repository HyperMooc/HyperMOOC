import os
import xml.etree.ElementTree as ET
import cv2
import numpy as np
from pathlib import Path

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

def draw_annotations(image, annotations):
    """在图像上绘制标注框"""
    for anno in annotations:
        name = anno['name']
        xmin, ymin, xmax, ymax = anno['box']
        
        # 绘制矩形框
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
        
        # 绘制标签背景
        text_size = cv2.getTextSize(name, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
        cv2.rectangle(image, (xmin, ymin - text_size[1] - 10), (xmin + text_size[0] + 10, ymin), (0, 0, 255), -1)
        
        # 绘制标签文字
        cv2.putText(image, name, (xmin + 5, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    return image

def process_images(xml_dir, img_dir, output_dir):
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
            labeled_image = draw_annotations(image.copy(), annotations)
            
            # 保存带标注的图像
            output_filename = os.path.basename(image_path)
            output_path = os.path.join(output_dir, output_filename)
            cv2.imwrite(output_path, labeled_image)
            
            print(f"已处理: {xml_file} -> {output_filename}")
            
        except Exception as e:
            print(f"处理 {xml_file} 时出错: {e}")

if __name__ == "__main__":
    # 设置目录路径
    base_dir = Path(__file__).parent.parent  # 项目根目录
    xml_dir = base_dir / "src" / "assets" / "corpusXml"
    img_dir = base_dir / "src" / "assets" / "corpusImages"
    output_dir = base_dir / "src" / "assets" / "corpusImagesLabel"
    
    # 处理图像
    process_images(xml_dir, img_dir, output_dir)
    print(f"所有标注图像已保存到 {output_dir}") 