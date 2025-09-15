<template>
  <div class="design-space-container">
    <div class="design-space-image">
      <img src="../assets/designSpace.png" alt="Design Space" />
    </div>
    <div class="design-space-description">
      <p>
        We present a comprehensive design space for MOOC video augmentation,
        categorizing different visualization techniques and their applications
        in educational content. This design space helps in understanding the
        various approaches to enhance learning through visual elements.
      </p>
    </div>
  </div>
</template>

<script setup>
// 可以在这里定义props和其他逻辑
</script>

<style scoped>
.design-space-container {
  display: flex;
  flex-direction: column;
  gap: 30px;
  width: 100%;
  padding: 0 20px;
  box-sizing: border-box;
}

.design-space-image {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin: 0 auto;
  max-width: calc(100% - 40px);
}

.design-space-image img {
  width: 100%;
  height: auto;
  object-fit: contain;
  display: block;
}

.design-space-table {
  width: 100%;
  background: #fff;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
  table-layout: fixed;
}

th, td {
  border: 1px solid #ddd;
  padding: 12px;
  text-align: left;
  word-wrap: break-word;
  font-size: 0.9em;
}

th {
  background-color: #f4f4f4;
  font-weight: 600;
  color: #333;
  width: 9.09%;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}

.design-space-description {
  background: #fff;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.design-space-description p {
  color: #666;
  line-height: 1.6;
  margin: 0;
  text-align: justify;
}

@media (max-width: 768px) {
  .design-space-table {
    font-size: 14px;
  }
  
  th, td {
    padding: 8px;
  }
}
</style> 