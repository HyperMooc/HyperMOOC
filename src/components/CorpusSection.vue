<template>
  <div class="corpus-section" id="corpus">
    <h2>Corpus</h2>
    <div class="filter-container">
      <div class="filter-box">
        <label for="category-select">类别:</label>
        <select id="category-select" v-model="selectedCategory" @change="filterItems">
          <option value="all">全部</option>
          <option value="videos">Videos</option>
          <option value="training-images">Training Images</option>
        </select>
      </div>
      
      <div class="filter-box">
        <label for="type-select">类型:</label>
        <select id="type-select" v-model="selectedType" @change="filterItems">
          <option value="all">全部</option>
          <option v-for="type in availableTypes" :key="type" :value="type">{{ type }}</option>
        </select>
      </div>
    </div>
    
    <div class="corpus-items">
      <div v-if="filteredItems.length === 0" class="no-items">
        没有符合条件的项目
      </div>
      <div v-else class="items-grid">
        <div v-for="(item, index) in paginatedItems" :key="index" class="corpus-item" @click="selectItem(item)">
          <div class="item-preview">
            <img 
              v-if="item.category === 'training-images'" 
              :src="item.labeledPath || item.path" 
              :alt="item.title"
            >
            <video v-else-if="item.category === 'videos'" controls>
              <source :src="item.path" type="video/mp4">
              您的浏览器不支持视频标签
            </video>
            <div v-else class="no-preview">无预览</div>
          </div>
        </div>
      </div>
      
      <!-- 分页控制 -->
      <div class="pagination" v-if="totalPages > 1">
        <button 
          @click="currentPage = Math.max(currentPage - 1, 1)" 
          :disabled="currentPage === 1"
          class="page-btn"
        >
          上一页
        </button>
        <span class="page-info">{{ currentPage }} / {{ totalPages }}</span>
        <button 
          @click="currentPage = Math.min(currentPage + 1, totalPages)" 
          :disabled="currentPage === totalPages"
          class="page-btn"
        >
          下一页
        </button>
      </div>
    </div>
    
    <!-- 详细查看模态框 -->
    <div v-if="selectedItem" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <button class="close-btn" @click="closeModal">×</button>
        
        <div v-if="selectedItem.category === 'training-images'" class="image-container">
          <h3>{{ selectedItem.title }}</h3>
          <div class="image-controls">
            <button @click="showLabeled = !showLabeled" class="toggle-btn">
              {{ showLabeled ? '显示原图' : '显示标注' }}
            </button>
          </div>
          <img 
            :src="showLabeled && selectedItem.labeledPath ? selectedItem.labeledPath : selectedItem.path" 
            :alt="selectedItem.title" 
            class="full-image"
          >
        </div>
        
        <div v-else-if="selectedItem.category === 'videos'" class="video-container">
          <h3>{{ selectedItem.title }}</h3>
          <video controls class="full-video">
            <source :src="selectedItem.path" type="video/mp4">
            您的浏览器不支持视频标签
          </video>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, computed, watch, onMounted } from 'vue';
import { allResources } from '../assets/corpusResources';

export default defineComponent({
  name: 'CorpusSection',
  setup() {
    const selectedCategory = ref('all');
    const selectedType = ref('all');
    const currentPage = ref(1);
    const itemsPerPage = ref(9);
    const corpusItems = ref(allResources);
    const filteredItems = ref([]);
    const selectedItem = ref(null);
    const showLabeled = ref(true);
    
    // 过滤项目
    const filterItems = () => {
      filteredItems.value = corpusItems.value.filter(item => {
        const categoryMatch = selectedCategory.value === 'all' || item.category === selectedCategory.value;
        const typeMatch = selectedType.value === 'all' || item.type === selectedType.value;
        return categoryMatch && typeMatch;
      });
      currentPage.value = 1; // 重置到第一页
    };
    
    // 计算可用类型
    const availableTypes = computed(() => {
      const types = new Set();
      corpusItems.value.forEach(item => {
        if (selectedCategory.value === 'all' || item.category === selectedCategory.value) {
          types.add(item.type);
        }
      });
      return Array.from(types);
    });
    
    // 计算总页数
    const totalPages = computed(() => {
      return Math.ceil(filteredItems.value.length / itemsPerPage.value);
    });
    
    // 计算当前页的项目
    const paginatedItems = computed(() => {
      const start = (currentPage.value - 1) * itemsPerPage.value;
      const end = start + itemsPerPage.value;
      return filteredItems.value.slice(start, end);
    });
    
    // 选择项目查看详情
    const selectItem = (item) => {
      selectedItem.value = item;
    };
    
    // 关闭模态框
    const closeModal = () => {
      selectedItem.value = null;
    };
    
    // 初始化
    onMounted(() => {
      filterItems();
    });
    
    return {
      selectedCategory,
      selectedType,
      currentPage,
      filteredItems,
      paginatedItems,
      totalPages,
      selectedItem,
      filterItems,
      selectItem,
      closeModal,
      showLabeled
    };
  }
});
</script>

<style scoped>
.corpus-section {
  padding: 2rem;
  background-color: #1a1a1a;
  border-radius: 8px;
  margin-bottom: 2rem;
}

.filter-container {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.filter-box {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.filter-box label {
  color: #fff;
  font-weight: bold;
}

.filter-box select {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
}

.items-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

.corpus-item {
  border: 1px solid #eee;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.corpus-item:hover {
  transform: translateY(-5px);
}

.item-preview {
  height: 220px;
  background-color: #f5f5f5;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.item-preview img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.item-preview video {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.no-preview {
  color: #999;
}

.no-items {
  text-align: center;
  padding: 2rem;
  color: #999;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 2rem;
  gap: 1rem;
}

.page-btn {
  padding: 0.5rem 1rem;
  background-color: #f0f0f0;
  border: 1px solid #ddd;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.page-btn:hover:not(:disabled) {
  background-color: #e0e0e0;
}

.page-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-info {
  font-size: 0.9rem;
  color: #666;
}

/* 添加模态框样式 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  max-width: 90%;
  max-height: 90%;
  overflow: auto;
  position: relative;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: #333;
}

.image-container {
  width: 800px;
  text-align: center;
}

.full-image {
  max-width: 100%;
  max-height: 600px;
  object-fit: contain;
}

.video-container {
  width: 800px;
}

.full-video {
  width: 100%;
  max-height: 600px;
}

.image-controls {
  margin-bottom: 10px;
}

.toggle-btn {
  padding: 0.5rem 1rem;
  background-color: #f0f0f0;
  border: 1px solid #ddd;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.toggle-btn:hover:not(:disabled) {
  background-color: #e0e0e0;
}

.toggle-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style> 