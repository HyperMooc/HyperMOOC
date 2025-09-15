<template>
  <div class="annotated-image-container">
    <div v-if="error" class="error-message">
      {{ error }}
    </div>
    <div v-else class="image-wrapper" ref="imageWrapper">
      <img 
        v-if="imageSrc" 
        :src="imageSrc" 
        @load="onImageLoad" 
        @error="onImageError"
        ref="image"
        class="base-image"
      />
      <div 
        v-for="(annotation, index) in annotations" 
        :key="index"
        class="annotation-box"
        :style="getBoxStyle(annotation)"
      >
        <div class="annotation-label">{{ annotation.name }}</div>
      </div>
      <div v-if="loading" class="loading-overlay">
        <div class="loading-spinner"></div>
      </div>
    </div>
    <div class="debug-info" v-if="showDebug">
      <p>XML 路径: {{ xmlPath }}</p>
      <p>图像路径: {{ imageSrc }}</p>
      <p>标注数量: {{ annotations.length }}</p>
      <p>图像尺寸: {{ imageWidth }}x{{ imageHeight }}</p>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed, watch } from 'vue';
import { parseAnnotationXml, parseXmlString } from '../utils/xmlParser';

export default {
  name: 'AnnotatedImage',
  props: {
    xmlPath: {
      type: String,
      default: null
    },
    xmlData: {
      type: String,
      default: null
    },
    imagePath: {
      type: String,
      default: null
    },
    showDebug: {
      type: Boolean,
      default: false
    }
  },
  setup(props) {
    const image = ref(null);
    const imageWrapper = ref(null);
    const annotations = ref([]);
    const imageSrc = ref(props.imagePath);
    const loading = ref(true);
    const imageLoaded = ref(false);
    const imageWidth = ref(0);
    const imageHeight = ref(0);
    const error = ref(null);
    
    // 加载 XML 文件并解析标注
    const loadAnnotations = async () => {
      loading.value = true;
      error.value = null;
      
      try {
        let result;
        
        if (props.xmlData) {
          // 直接解析传入的 XML 数据
          console.log('使用内联 XML 数据:', props.xmlData ? props.xmlData.substring(0, 50) + '...' : 'null');
          result = parseXmlString(props.xmlData);
        } else if (props.xmlPath) {
          // 从 URL 加载 XML
          console.log('开始加载 XML:', props.xmlPath);
          result = await parseAnnotationXml(props.xmlPath);
        } else {
          throw new Error('未提供 XML 数据或路径');
        }
        
        console.log('解析结果:', result);
        
        if (!result || !result.annotations || result.annotations.length === 0) {
          console.warn('未找到任何标注');
        }
        
        annotations.value = result.annotations || [];
        
        // 如果没有提供图像路径，则使用 XML 中的路径
        if (!props.imagePath && result.imagePath) {
          console.log('使用 XML 中的图像路径:', result.imagePath);
          imageSrc.value = result.imagePath;
        }
      } catch (err) {
        console.error('加载标注失败:', err);
        error.value = `加载标注失败: ${err.message}`;
      } finally {
        loading.value = false;
      }
    };
    
    // 图像加载完成后的处理
    const onImageLoad = () => {
      if (image.value) {
        imageWidth.value = image.value.naturalWidth;
        imageHeight.value = image.value.naturalHeight;
        imageLoaded.value = true;
        console.log('图像加载完成:', imageWidth.value, 'x', imageHeight.value);
      }
    };
    
    // 图像加载错误处理
    const onImageError = (e) => {
      console.error('图像加载失败:', e);
      error.value = '图像加载失败';
      loading.value = false;
    };
    
    // 计算标注框的样式
    const getBoxStyle = (annotation) => {
      if (!imageLoaded.value) return {};
      
      const { box } = annotation;
      const wrapperWidth = imageWrapper.value?.clientWidth || 0;
      const wrapperHeight = imageWrapper.value?.clientHeight || 0;
      
      // 计算缩放比例
      const scaleX = wrapperWidth / imageWidth.value;
      const scaleY = wrapperHeight / imageHeight.value;
      
      return {
        left: `${box.xmin * scaleX}px`,
        top: `${box.ymin * scaleY}px`,
        width: `${(box.xmax - box.xmin) * scaleX}px`,
        height: `${(box.ymax - box.ymin) * scaleY}px`
      };
    };
    
    // 监听 props 变化
    watch(() => props.xmlPath, () => {
      if (props.xmlPath) {
        loadAnnotations();
      }
    });
    
    watch(() => props.imagePath, () => {
      if (props.imagePath) {
        imageSrc.value = props.imagePath;
      }
    });
    
    // 添加 watch 监听 xmlData 变化
    watch(() => props.xmlData, (newVal) => {
      if (newVal) {
        console.log('XML 数据已更新，重新加载');
        loadAnnotations();
      }
    });
    
    // 修改 onMounted 钩子
    onMounted(() => {
      console.log('组件已挂载，XML 路径:', props.xmlPath);
      console.log('组件已挂载，XML 数据:', props.xmlData ? '有数据' : '无数据');
      console.log('组件已挂载，图像路径:', props.imagePath);
      
      if (props.xmlPath || props.xmlData) {
        loadAnnotations();
      } else {
        console.warn('未提供 XML 数据或路径');
        error.value = '未提供 XML 数据或路径';
        loading.value = false;
      }
    });
    
    return {
      image,
      imageWrapper,
      annotations,
      imageSrc,
      loading,
      imageLoaded,
      imageWidth,
      imageHeight,
      error,
      onImageLoad,
      onImageError,
      getBoxStyle
    };
  }
}
</script>

<style scoped>
.annotated-image-container {
  position: relative;
  width: 100%;
  height: 100%;
}

.image-wrapper {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.base-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.annotation-box {
  position: absolute;
  border: 2px solid #ff0000;
  background-color: rgba(255, 0, 0, 0.2);
  pointer-events: none;
}

.annotation-label {
  position: absolute;
  top: -20px;
  left: 0;
  background-color: #ff0000;
  color: white;
  padding: 2px 5px;
  font-size: 12px;
  white-space: nowrap;
}

.loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.error-message {
  color: red;
  padding: 20px;
  text-align: center;
  background-color: #ffeeee;
  border: 1px solid #ffcccc;
  border-radius: 4px;
}

.debug-info {
  margin-top: 10px;
  padding: 10px;
  background-color: #f0f0f0;
  border: 1px solid #ddd;
  font-size: 12px;
  font-family: monospace;
}
</style> 