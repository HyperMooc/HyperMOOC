<template>
  <div class="test-container">
    <h2>测试标注</h2>
    <div class="annotation-test" style="width: 800px; height: 600px;">
      <annotated-image 
        :xml-data="testXmlData" 
        :image-path="testImagePath"
        :show-debug="true"
      />
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue';
import AnnotatedImage from './AnnotatedImage.vue';

export default defineComponent({
  name: 'TestAnnotation',
  components: {
    AnnotatedImage
  },
  setup() {
    // 测试图像路径
    const testImagePath = ref(new URL('../assets/corpusImages/T1.png', import.meta.url).href);
    
    // 测试 XML 数据
    const testXmlData = ref(`<?xml version="1.0" encoding="UTF-8"?>
<annotation>
  <folder>images</folder>
  <filename>test.png</filename>
  <path>${testImagePath.value}</path>
  <size>
    <width>800</width>
    <height>600</height>
    <depth>3</depth>
  </size>
  <object>
    <name>测试标注</name>
    <bndbox>
      <xmin>100</xmin>
      <ymin>100</ymin>
      <xmax>300</xmax>
      <ymax>300</ymax>
    </bndbox>
  </object>
</annotation>`);
    
    return {
      testImagePath,
      testXmlData
    };
  }
});
</script> 