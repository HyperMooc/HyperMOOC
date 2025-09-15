// 存储 XML 数据的对象
export const xmlData = {
  'T1': `<?xml version="1.0" encoding="UTF-8"?>
<annotation>
  <folder>images</folder>
  <filename>T1.png</filename>
  <path>../assets/corpusImages/T1.png</path>
  <source>
    <database>Unknown</database>
  </source>
  <size>
    <width>800</width>
    <height>600</height>
    <depth>3</depth>
  </size>
  <segmented>0</segmented>
  <object>
    <name>人物</name>
    <pose>Unspecified</pose>
    <truncated>0</truncated>
    <difficult>0</difficult>
    <bndbox>
      <xmin>200</xmin>
      <ymin>100</ymin>
      <xmax>400</xmax>
      <ymax>500</ymax>
    </bndbox>
  </object>
</annotation>`,
  // 为其他图像生成默认 XML 数据
  'T2': generateDefaultXml('T2'),
  'T3': generateDefaultXml('T3'),
  'T4': generateDefaultXml('T4'),
  'T5': generateDefaultXml('T5'),
  'T6': generateDefaultXml('T6'),
  'T7': generateDefaultXml('T7'),
  'T8': generateDefaultXml('T8')
};

// 生成默认的 XML 数据
function generateDefaultXml(fileName) {
  return `<?xml version="1.0" encoding="UTF-8"?>
<annotation>
  <folder>images</folder>
  <filename>${fileName}.png</filename>
  <path>../assets/corpusImages/${fileName}.png</path>
  <size>
    <width>800</width>
    <height>600</height>
    <depth>3</depth>
  </size>
  <segmented>0</segmented>
  <object>
    <name>示例标注</name>
    <bndbox>
      <xmin>100</xmin>
      <ymin>100</ymin>
      <xmax>300</xmax>
      <ymax>300</ymax>
    </bndbox>
  </object>
</annotation>`;
}

// 解析 XML 字符串
export function parseXmlString(xmlString) {
  if (!xmlString) {
    console.error('XML 字符串为空');
    return { imagePath: null, annotations: [] };
  }
  
  const parser = new DOMParser();
  const xmlDoc = parser.parseFromString(xmlString, "text/xml");
  
  // 检查解析错误
  const parseError = xmlDoc.querySelector('parsererror');
  if (parseError) {
    console.error('XML 解析错误:', parseError.textContent);
    return { imagePath: null, annotations: [] };
  }
  
  // 提取图像路径
  const imagePath = xmlDoc.querySelector('path')?.textContent;
  
  // 提取标注信息
  const annotations = [];
  const objects = xmlDoc.querySelectorAll('object');
  
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
    }
  });
  
  return {
    imagePath,
    annotations
  };
} 