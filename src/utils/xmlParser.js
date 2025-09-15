// 解析 XML 文件并提取标注信息
export async function parseAnnotationXml(xmlPath) {
  console.log('尝试加载 XML 文件:', xmlPath);
  try {
    const response = await fetch(xmlPath);
    if (!response.ok) {
      console.error(`XML 文件加载失败: ${response.status} ${response.statusText}`);
      return { imagePath: null, annotations: [] };
    }
    
    const xmlText = await response.text();
    console.log('XML 内容:', xmlText.substring(0, 200) + '...');
    
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(xmlText, "text/xml");
    
    // 检查解析错误
    const parseError = xmlDoc.querySelector('parsererror');
    if (parseError) {
      console.error('XML 解析错误:', parseError.textContent);
      return { imagePath: null, annotations: [] };
    }
    
    // 提取图像路径
    const imagePath = xmlDoc.querySelector('path')?.textContent;
    console.log('从 XML 中提取的图像路径:', imagePath);
    
    // 提取标注信息
    const annotations = [];
    const objects = xmlDoc.querySelectorAll('object');
    console.log('找到的对象数量:', objects.length);
    
    objects.forEach(obj => {
      const name = obj.querySelector('name')?.textContent;
      const bndbox = obj.querySelector('bndbox');
      
      if (bndbox) {
        const xmin = parseInt(bndbox.querySelector('xmin')?.textContent || '0');
        const ymin = parseInt(bndbox.querySelector('ymin')?.textContent || '0');
        const xmax = parseInt(bndbox.querySelector('xmax')?.textContent || '0');
        const ymax = parseInt(bndbox.querySelector('ymax')?.textContent || '0');
        
        annotations.push({
          name,
          box: { xmin, ymin, xmax, ymax },
          width: xmax - xmin,
          height: ymax - ymin
        });
        
        console.log(`添加标注: ${name}, 位置: (${xmin},${ymin},${xmax},${ymax})`);
      }
    });
    
    return {
      imagePath,
      annotations
    };
  } catch (error) {
    console.error('解析 XML 文件失败:', error);
    return { imagePath: null, annotations: [] };
  }
} 