import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

// GitHub Pages SPA 404 插件：构建时自动生成 404.html（内容与 index.html 一致）
function spaFallbackPlugin() {
  return {
    name: 'spa-fallback',
    closeBundle() {
      const fs = require('fs')
      const path = require('path')
      const indexHtml = path.resolve(__dirname, 'dist/index.html')
      const fallbackHtml = path.resolve(__dirname, 'dist/404.html')
      if (fs.existsSync(indexHtml)) {
        fs.copyFileSync(indexHtml, fallbackHtml)
        console.log('\n✓ 404.html SPA fallback generated')
      }
    }
  }
}

export default defineConfig({
  plugins: [vue(), spaFallbackPlugin()],
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src')
    }
  },
  base: '/stuu/',
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
})
