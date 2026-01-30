<script setup>
import HelloWorld from './components/HelloWorld.vue'
import ExamplesSection from './components/ExamplesSection.vue'
import CorpusSection from './components/CorpusSection.vue'
import ModelsSection from './components/ModelsSection.vue'
import DesignSpaceTable from './components/DesignSpaceTable.vue'
</script>

<template>
  <div class="app-container">
    <header class="header-with-bg">
      <div class="header-content">
        <h1>HyperMOOC: Augmenting MOOC Videos with Concept-based Embedded Visualizations</h1>
        <nav>
          <a href="#examples">Examples</a>
          <a href="#corpus">Corpus</a>
          <a href="#design-space">Design Space</a>
          <a href="#models">Data Processing</a>
          <a href="https://arxiv.org/pdf/2509.08404r">Paper</a>
        </nav>
      </div>
      <div class="teaser-image">
        <img src="./assets/teaser.png" alt="teaser" />
      </div>
    </header>

    <main>
      <section id="abstract">
        <h2>Abstract</h2>
        <p>
          Massive Open Online Courses (MOOCs) have become increasingly popular worldwide. However, learners primarily rely on watching videos, easily losing knowledge context and reducing learning effectiveness. We propose HyperMOOC, a novel approach augmenting MOOC videos with concept-based embedded visualizations to help learners maintain knowledge context. Informed by expert interviews and literature review, HyperMOOC employs multi-glyph designs for different knowledge types and multi-stage interactions for deeper understanding. Using a timeline-based radial visualization, learners can grasp cognitive paths of concepts and navigate courses through hyperlink-based interactions. We evaluated HyperMOOC through a user study with 36 MOOC learners and interviews with two instructors. Results demonstrate that HyperMOOC enhances learners' learning effect and efficiency on MOOCs, with participants showing higher satisfaction and improved course understanding compared to traditional video-based learning approache
        </p>
      </section>

      <section id="demo">
        <h2>Demo Application</h2>
        <p>
          Currently, online demo is not available due to the hardware limited (e.g., GPU required). 
          Source code will be released once paper accepted.
        </p>
      </section>

      <ExamplesSection />
      <CorpusSection />
      <section id="design-space">
        <h2>Design Space</h2>
        <div class="table-container">
          <DesignSpaceTable />
        </div>
      </section>
      <ModelsSection />
    </main>
  </div>
</template>

<style>
/* 全局样式 */
body {
  margin: 0;
  padding: 0;
  background-color: #1a1a1a;  /* 深色背景 */
}

h2 {
  color: #ffffff;
  border-bottom: 2px solid #42b883;
  padding-bottom: 10px;
  margin-bottom: 20px;
  display: inline-block;
  font-size: 1.8em;
  position: relative;
  text-align: center;
}
</style>

<style scoped>
.app-container {
  width: 100vw;  /* 设置为视窗宽度 */
  min-height: 100vh;  /* 确保最小高度占满视窗 */
  margin: 0;  /* 移除外边距 */
  padding: 0;  /* 移除内边距 */
  font-family: Arial, sans-serif;
  background-color: #1a1a1a;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
}

/* 添加一个内容容器来控制主要内容的宽度 */
main {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

header {
  text-align: center;
  margin-bottom: 40px;
}

h1 {
  font-size: 2.5em;
  color: #333;
  margin-bottom: 20px;
}

nav {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 20px;
}

nav a {
  color: #333;
  text-decoration: none;
  padding: 8px 16px;
  border-radius: 4px;
  transition: all 0.3s ease;
  background-color: rgba(255, 255, 255, 0.8);
  border: 2px solid transparent;  /* 初始透明边框 */
  position: relative;  /* 为伪元素定位 */
}

nav a:hover {
  background-color: #fff;
  color: #000;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-color: #42b883;  /* 悬停时显示边框颜色 */
  transform: translateY(-2px);  /* 轻微上浮效果 */
}

nav a::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 2px;
  background-color: #42b883;
  transition: width 0.3s ease;
}

nav a:hover::after {
  width: 100%;  /* 悬停时边框展开 */
}

section {
  margin-bottom: 40px;
}

h2 {
  color: #f8f8f8;
  margin-bottom: 20px;
}

p {
  line-height: 1.6;
  color: #666;
}

.table-container {
  overflow-x: auto;
  margin-top: 20px;
}

.header-with-bg {
  position: relative;
  margin: -31px 0px 0px 0px;
  padding: 20px;
  background: #f5f5f5;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 40px;
  padding-bottom: 40px;
}

.teaser-image {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  height: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 20px;
  box-sizing: border-box;
}

.teaser-image img {
  width: auto;
  height: auto;
  max-width: 100%;
  max-height: 300px;
  margin-top: -20px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.header-content {
  background: rgba(255, 255, 255, 0.95);
  padding: 30px;
  border-radius: 8px;
  max-width: 1000px;
  margin: 20px auto 0;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 2.5em;
  color: #333;
  margin-bottom: 20px;
  text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8);
}

nav {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 20px;
}

nav a {
  color: #333;
  text-decoration: none;
  padding: 8px 16px;
  border-radius: 4px;
  transition: all 0.3s ease;
  background-color: rgba(255, 255, 255, 0.8);
}

nav a:hover {
  background-color: #fff;
  color: #000;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

section#abstract {
  margin-bottom: 40px;
  text-align: center;
}

section#abstract h2 {
  margin-bottom: 20px;
}

section#abstract p {
  line-height: 1.6;
  color: #666;
  text-align: left;
  white-space: normal;
  margin: 0 auto;
  max-width: 800px;
}
</style>
