import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  // 配置别名，使得可以通过 @/ 访问 src 目录
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  },
  base: '/HyperMOOC/',
})
