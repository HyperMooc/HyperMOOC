<template>
  <div class="simple-test">
    <h3>简单测试</h3>
    <div class="test-image" style="width: 400px; height: 300px; border: 1px solid #ccc;">
      <img ref="testImage" :src="imagePath" @load="onImageLoad" style="width: 100%; height: 100%; object-fit: contain;" />
      
      <div 
        v-for="(box, index) in boxes" 
        :key="index"
        class="test-box"
        :style="{
          left: `${box.x}px`,
          top: `${box.y}px`,
          width: `${box.width}px`,
          height: `${box.height}px`
        }"
      >
        <span class="test-label">标注 {{ index + 1 }}</span>
      </div>
    </div>
    <div class="controls">
      <button @click="addBox">添加标注框</button>
      <button @click="clearBoxes">清除所有</button>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'SimpleTest',
  setup() {
    const imagePath = ref(new URL('../assets/corpusImages/T1.png', import.meta.url).href);
    const testImage = ref(null);
    const boxes = ref([]);
    
    const onImageLoad = () => {
      console.log('测试图像已加载');
      // 添加一个默认标注框
      addBox();
    };
    
    const addBox = () => {
      const width = Math.floor(Math.random() * 100) + 50;
      const height = Math.floor(Math.random() * 100) + 50;
      const x = Math.floor(Math.random() * (400 - width));
      const y = Math.floor(Math.random() * (300 - height));
      
      boxes.value.push({ x, y, width, height });
    };
    
    const clearBoxes = () => {
      boxes.value = [];
    };
    
    return {
      imagePath,
      testImage,
      boxes,
      onImageLoad,
      addBox,
      clearBoxes
    };
  }
});
</script>

<style scoped>
.simple-test {
  margin: 20px;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 8px;
}

.test-image {
  position: relative;
  margin: 20px 0;
  background-color: white;
}

.test-box {
  position: absolute;
  border: 2px solid red;
  background-color: rgba(255, 0, 0, 0.2);
  pointer-events: none;
}

.test-label {
  position: absolute;
  top: -20px;
  left: 0;
  background-color: red;
  color: white;
  padding: 2px 5px;
  font-size: 12px;
}

.controls {
  margin-top: 10px;
}

button {
  margin-right: 10px;
  padding: 5px 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
</style> 