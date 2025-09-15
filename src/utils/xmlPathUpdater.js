import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// 获取当前文件的目录
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// XML 文件目录
const xmlDir = path.resolve(__dirname, '../assets/corpusXml');

// 更新 XML 文件中的路径
export function updateXmlPaths() {
  // 读取 XML 目录下的所有文件
  const files = fs.readdirSync(xmlDir);
  
  files.forEach(file => {
    if (file.endsWith('.xml')) {
      const filePath = path.join(xmlDir, file);
      let content = fs.readFileSync(filePath, 'utf8');
      
      // 提取文件名（不含扩展名）
      const baseName = path.basename(file, '.xml');
      
      // 替换绝对路径为相对路径
      content = content.replace(
        /<path>.*?([^\\\/]+\.png)<\/path>/g, 
        `<path>../assets/corpusImages/${baseName}.png</path>`
      );
      
      // 写回文件
      fs.writeFileSync(filePath, content);
      console.log(`已更新 ${file} 中的路径`);
    }
  });
  
  console.log('所有 XML 文件路径更新完成');
} 