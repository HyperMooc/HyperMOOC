// 使用 Vite 的 import.meta.glob 自动导入所有资源

// 自动导入所有图片资源
const imageModules = import.meta.glob('./corpusImages/*.{png,jpg,jpeg,gif,webp}', { eager: true });
const labeledImageModules = import.meta.glob('./corpusImagesLabel/*.{png,jpg,jpeg,gif,webp}', { eager: true });
const videoModules = import.meta.glob('./corpusVideos/*.{mp4,webm,ogg}', { eager: true });

// 处理图片资源
export const trainingImages = Object.entries(imageModules).map(([path, module]) => {
  // 从路径中提取文件名（不含扩展名）
  const fileName = path.split('/').pop().split('.')[0];
  
  // 查找对应的带标注图像
  const labeledPath = Object.keys(labeledImageModules).find(p => p.includes(`/${fileName}.`));
  const labeledImage = labeledPath ? labeledImageModules[labeledPath].default : null;
  
  // 设置默认类型
  const type = '技术图解';
  
  return {
    title: `图像 ${fileName}`,
    category: 'training-images',
    type: type,
    path: module.default, // 原始图像路径
    labeledPath: labeledImage, // 带标注的图像路径
    fileName: fileName
  };
});

// 处理视频资源
export const videos = Object.entries(videoModules).map(([path, module]) => {
  // 从路径中提取文件名（不含扩展名）
  const fileName = path.split('/').pop().split('.')[0];
  
  // 设置默认类型
  const type = '技术演示';
  
  return {
    title: `视频 ${fileName}`,
    category: 'videos',
    type: type,
    path: module.default, // Vite 导入的资源默认路径
    fileName: fileName
  };
});

// 所有资源合并
export const allResources = [...videos, ...trainingImages];

// 调试信息
console.log(`已加载 ${videos.length} 个视频和 ${trainingImages.length} 个图片资源`); 