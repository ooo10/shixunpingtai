<template>
  <div class="image-module">
    <div class="module-header">
      <div class="header-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
          <circle cx="8.5" cy="8.5" r="1.5"/>
          <polyline points="21 15 16 10 5 21"/>
        </svg>
      </div>
      <div class="header-text">
        <h2>图片生成</h2>
        <p>基于AI的智能图片生成工具</p>
      </div>
    </div>

    <div class="tabs-container">
      <button 
        v-for="tab in tabs" 
        :key="tab.key"
        :class="['tab-btn', { active: activeTab === tab.key }]"
        @click="switchTab(tab.key)"
      >
        {{ tab.label }}
      </button>
    </div>

    <div class="content-area">
      <div v-if="activeTab === 'text2img'" class="input-section">
        <label class="input-label">输入图片描述</label>
        <textarea
          v-model="inputText"
          placeholder="请描述您想要生成的图片..."
          :maxlength="500"
          class="text-input"
          rows="4"
        ></textarea>
        <span class="char-count">{{ inputText.length }}/500</span>
      </div>

      <div v-if="activeTab === 'img2img'" class="input-section">
        <label class="input-label">上传参考图片</label>
        <div class="upload-area" @click="triggerFileInput" @dragover.prevent @drop.prevent="handleDrop">
          <input 
            type="file" 
            ref="fileInput" 
            accept="image/*" 
            class="file-input"
            @change="handleFileSelect"
          />
          <div v-if="!uploadedImage" class="upload-placeholder">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
              <polyline points="17 8 12 3 7 8"/>
              <line x1="12" y1="3" x2="12" y2="15"/>
            </svg>
            <p>点击或拖拽上传图片</p>
            <p class="upload-hint">支持 JPG、PNG 格式</p>
          </div>
          <div v-else class="upload-preview">
            <img :src="uploadedImage" alt="上传的图片" />
            <button class="remove-btn" @click="clearUpload">移除</button>
          </div>
        </div>
        <label class="input-label mt-2">描述词（可选）</label>
        <textarea
          v-model="img2imgPrompt"
          placeholder="添加额外的描述词..."
          :maxlength="200"
          class="text-input"
          rows="2"
        ></textarea>
      </div>

      <div v-if="activeTab === 'style'" class="input-section">
        <label class="input-label">上传图片</label>
        <div class="upload-area" @click="triggerStyleFileInput" @dragover.prevent @drop.prevent="handleStyleDrop">
          <input 
            type="file" 
            ref="styleFileInput" 
            accept="image/*" 
            class="file-input"
            @change="handleStyleFileSelect"
          />
          <div v-if="!styleImage" class="upload-placeholder">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
              <circle cx="8.5" cy="8.5" r="1.5"/>
              <polyline points="21 15 16 10 5 21"/>
            </svg>
            <p>点击或拖拽上传图片</p>
            <p class="upload-hint">支持 JPG、PNG 格式</p>
          </div>
          <div v-else class="upload-preview">
            <img :src="styleImage" alt="原图" />
            <button class="remove-btn" @click="clearStyleImage">移除</button>
          </div>
        </div>
        <label class="input-label">选择目标风格</label>
        <div class="style-options">
          <button 
            v-for="style in styleOptions" 
            :key="style.value"
            :class="['style-option', { active: selectedStyleForTransfer === style.value }]"
            @click="selectedStyleForTransfer = style.value"
          >
            <span class="style-icon">{{ style.icon }}</span>
            <span class="style-name">{{ style.label }}</span>
          </button>
        </div>
      </div>

      <div v-if="activeTab === 'text2img'" class="params-section">
        <div class="param-row">
          <label class="param-label">图片风格</label>
          <select v-model="selectedStyle" class="param-select">
            <option value="realistic">写实风格</option>
            <option value="cartoon">卡通风格</option>
            <option value="abstract">抽象风格</option>
            <option value="anime">动漫风格</option>
            <option value="photographic">摄影风格</option>
          </select>
        </div>
        <div class="param-row">
          <label class="param-label">图片尺寸</label>
          <select v-model="selectedSize" class="param-select">
            <option value="512x512">512×512</option>
            <option value="1024x1024">1024×1024</option>
            <option value="1024x1792">1024×1792</option>
          </select>
        </div>
        <div class="param-row">
          <label class="param-label">生成数量</label>
          <select v-model="selectedCount" class="param-select">
            <option :value="1">1张</option>
            <option :value="2">2张</option>
            <option :value="3">3张</option>
            <option :value="4">4张</option>
          </select>
        </div>
      </div>

      <button 
        class="generate-btn"
        :disabled="!canGenerate || isLoading"
        :class="{ loading: isLoading }"
        @click="handleGenerate"
      >
        <span>{{ isLoading ? '生成中...' : currentTabButtonText }}</span>
      </button>

      <div v-if="resultImages.length > 0" class="result-section">
        <div class="result-header">
          <span class="result-title">生成结果</span>
          <span class="response-time">响应时间: {{ responseTime }}ms</span>
        </div>
        <div class="image-grid">
          <div v-for="(img, index) in resultImages" :key="index" class="image-item">
            <img :src="img" :alt="`图片${index+1}`" />
            <div class="image-actions">
              <button class="action-btn" @click="downloadImage(img)">下载</button>
              <button class="action-btn" @click="copyImageUrl(img)">复制链接</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const tabs = [
  { key: 'text2img', label: '文生图' },
  { key: 'img2img', label: '图生图' },
  { key: 'style', label: '风格转换' }
]

const styleOptions = [
  { value: 'oil', label: '油画', icon: '🖼️' },
  { value: 'watercolor', label: '水彩', icon: '🎨' },
  { value: 'sketch', label: '素描', icon: '✏️' },
  { value: 'anime', label: '动漫', icon: '✨' },
  { value: 'pixel', label: '像素风', icon: '🖼️' },
  { value: 'vintage', label: '复古', icon: '📸' }
]

const activeTab = ref('text2img')
const inputText = ref('')
const img2imgPrompt = ref('')
const selectedStyle = ref('realistic')
const selectedSize = ref('512x512')
const selectedCount = ref(1)
const isLoading = ref(false)
const resultImages = ref([])
const responseTime = ref(0)
const uploadedImage = ref('')
const styleImage = ref('')
const selectedStyleForTransfer = ref('oil')
const fileInput = ref(null)
const styleFileInput = ref(null)

const currentTabButtonText = computed(() => {
  const texts = {
    text2img: '生成图片',
    img2img: '图生图',
    style: '风格转换'
  }
  return texts[activeTab.value] || '生成图片'
})

const canGenerate = computed(() => {
  if (activeTab.value === 'text2img') {
    return inputText.value.trim().length > 0
  } else if (activeTab.value === 'img2img') {
    return uploadedImage.value.length > 0
  } else if (activeTab.value === 'style') {
    return styleImage.value.length > 0
  }
  return false
})

const switchTab = (tabKey) => {
  activeTab.value = tabKey
  resultImages.value = []
}

const triggerFileInput = () => {
  fileInput.value?.click()
}

const triggerStyleFileInput = () => {
  styleFileInput.value?.click()
}

const handleFileSelect = (event) => {
  const file = event.target.files?.[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (e) => {
      uploadedImage.value = e.target?.result
    }
    reader.readAsDataURL(file)
  }
}

const handleStyleFileSelect = (event) => {
  const file = event.target.files?.[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (e) => {
      styleImage.value = e.target?.result
    }
    reader.readAsDataURL(file)
  }
}

const handleDrop = (event) => {
  const file = event.dataTransfer?.files?.[0]
  if (file && file.type.startsWith('image/')) {
    const reader = new FileReader()
    reader.onload = (e) => {
      uploadedImage.value = e.target?.result
    }
    reader.readAsDataURL(file)
  }
}

const handleStyleDrop = (event) => {
  const file = event.dataTransfer?.files?.[0]
  if (file && file.type.startsWith('image/')) {
    const reader = new FileReader()
    reader.onload = (e) => {
      styleImage.value = e.target?.result
    }
    reader.readAsDataURL(file)
  }
}

const clearUpload = () => {
  uploadedImage.value = ''
  if (fileInput.value) {
    fileInput.value.value = ''
  }
}

const clearStyleImage = () => {
  styleImage.value = ''
  if (styleFileInput.value) {
    styleFileInput.value.value = ''
  }
}

const handleGenerate = async () => {
  if (!canGenerate.value) return
  
  isLoading.value = true
  resultImages.value = []
  const startTime = Date.now()
  
  // Mock 优先模式 - 直接生成模拟图片，不依赖后端
  await new Promise(resolve => setTimeout(resolve, Math.random() * 1000 + 500))
  responseTime.value = Date.now() - startTime
  resultImages.value = generateMockImages()
  
  // 保存历史记录
  const history = JSON.parse(localStorage.getItem('creationHistory') || '[]')
  const title = activeTab.value === 'text2img' 
    ? inputText.value.substring(0, 30) + (inputText.value.length > 30 ? '...' : '')
    : (activeTab.value === 'img2img' ? '图生图结果' : `风格转换-${selectedStyleForTransfer.value}`)
  history.unshift({
    id: Date.now(),
    type: 'image',
    title: title,
    imageUrl: resultImages.value[0],
    content: resultImages.value[0],
    time: getTimeAgo(),
    createdAt: new Date().toISOString()
  })
  localStorage.setItem('creationHistory', JSON.stringify(history.slice(0, 50)))
  
  isLoading.value = false
}

const generateMockImages = () => {
  const seed = activeTab.value === 'style' ? selectedStyleForTransfer.value : inputText.value
  const hash = seed ? sum(seed) : Date.now()
  const images = [
    `https://picsum.photos/512/512?seed=${(hash + 1) % 10000}`,
    `https://picsum.photos/512/512?seed=${(hash + 2) % 10000}`,
    `https://picsum.photos/512/512?seed=${(hash + 3) % 10000}`,
    `https://picsum.photos/512/512?seed=${(hash + 4) % 10000}`
  ]
  return images.slice(0, selectedCount.value)
}

const sum = (str) => {
  return str.split('').reduce((acc, char) => acc + char.charCodeAt(0), 0)
}

const downloadImage = (url) => {
  const link = document.createElement('a')
  link.href = url
  link.download = `image_${Date.now()}.png`
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
}

const copyImageUrl = async (url) => {
  try {
    await navigator.clipboard.writeText(url)
    alert('已复制图片链接')
  } catch (error) {
    alert('复制失败')
  }
}

const getTimeAgo = () => {
  const now = new Date()
  const minutes = Math.floor(Math.random() * 60)
  const hours = Math.floor(Math.random() * 24)
  if (hours === 0) return `${minutes}分钟前`
  if (hours < 24) return `${hours}小时前`
  return `${Math.floor(hours / 24)}天前`
}
</script>

<style scoped>
.image-module {
  background: white;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.module-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
  padding-bottom: 20px;
  border-bottom: 1px solid #e2e8f0;
}

.header-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: linear-gradient(135deg, #ec4899, #f43f5e);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.header-text h2 {
  margin: 0;
  font-size: 20px;
  font-weight: 700;
  color: #1e293b;
}

.header-text p {
  margin: 4px 0 0;
  font-size: 14px;
  color: #64748b;
}

.tabs-container {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}

.tab-btn {
  padding: 10px 20px;
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  background: white;
  font-size: 14px;
  font-weight: 500;
  color: #475569;
  cursor: pointer;
  transition: all 0.3s;
}

.tab-btn:hover {
  border-color: #ec4899;
  color: #ec4899;
}

.tab-btn.active {
  border-color: #ec4899;
  background: rgba(236, 72, 153, 0.1);
  color: #ec4899;
}

.content-area {
  animation: fadeIn 0.3s;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.input-section {
  margin-bottom: 20px;
}

.input-label {
  display: block;
  font-size: 14px;
  font-weight: 600;
  color: #374151;
  margin-bottom: 8px;
}

.mt-2 {
  margin-top: 16px;
}

.text-input {
  width: 100%;
  padding: 14px 16px;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 15px;
  resize: vertical;
  outline: none;
  transition: border-color 0.3s;
  min-height: 80px;
}

.text-input:focus {
  border-color: #ec4899;
  box-shadow: 0 0 0 3px rgba(236, 72, 153, 0.1);
}

.text-input::placeholder {
  color: #9ca3af;
}

.char-count {
  display: block;
  text-align: right;
  font-size: 12px;
  color: #9ca3af;
  margin-top: 6px;
}

.file-input {
  display: none;
}

.upload-area {
  width: 100%;
  min-height: 180px;
  border: 2px dashed #e5e7eb;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s;
  position: relative;
  overflow: hidden;
}

.upload-area:hover {
  border-color: #ec4899;
  background: rgba(236, 72, 153, 0.05);
}

.upload-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 180px;
  color: #9ca3af;
}

.upload-placeholder svg {
  margin-bottom: 12px;
}

.upload-placeholder p {
  margin: 4px 0;
  font-size: 14px;
}

.upload-hint {
  font-size: 12px !important;
  color: #d1d5db !important;
}

.upload-preview {
  position: relative;
  width: 100%;
  height: 180px;
}

.upload-preview img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  background: #f8fafc;
}

.remove-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 6px 12px;
  border: none;
  border-radius: 8px;
  background: rgba(0,0,0,0.5);
  color: white;
  font-size: 12px;
  cursor: pointer;
  transition: background 0.3s;
}

.remove-btn:hover {
  background: rgba(0,0,0,0.7);
}

.style-options {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}

.style-option {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 16px;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  background: white;
  cursor: pointer;
  transition: all 0.3s;
}

.style-option:hover {
  border-color: #ec4899;
}

.style-option.active {
  border-color: #ec4899;
  background: rgba(236, 72, 153, 0.1);
}

.style-icon {
  font-size: 28px;
}

.style-name {
  font-size: 13px;
  color: #374151;
  font-weight: 500;
}

.params-section {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.param-row {
  display: flex;
  align-items: center;
  gap: 10px;
}

.param-label {
  font-size: 14px;
  font-weight: 600;
  color: #374151;
}

.param-select {
  padding: 10px 14px;
  border: 2px solid #e5e7eb;
  border-radius: 10px;
  font-size: 14px;
  color: #374151;
  background: white;
  cursor: pointer;
  outline: none;
  transition: border-color 0.3s;
}

.param-select:focus {
  border-color: #ec4899;
}

.generate-btn {
  width: 100%;
  padding: 16px;
  border: none;
  border-radius: 12px;
  background: linear-gradient(135deg, #ec4899, #f43f5e);
  color: white;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.generate-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(236, 72, 153, 0.4);
}

.generate-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.generate-btn.loading {
  background: #94a3b8;
}

.result-section {
  margin-top: 24px;
  padding: 20px;
  background: #f8fafc;
  border-radius: 12px;
}

.result-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  flex-wrap: wrap;
  gap: 10px;
}

.result-title {
  font-size: 16px;
  font-weight: 600;
  color: #1e293b;
}

.response-time {
  font-size: 12px;
  color: #64748b;
  background: white;
  padding: 4px 12px;
  border-radius: 20px;
}

.image-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 16px;
}

.image-item {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.image-item img {
  width: 100%;
  height: 180px;
  object-fit: cover;
}

.image-actions {
  display: flex;
  gap: 8px;
  padding: 10px;
}

.action-btn {
  flex: 1;
  padding: 8px 12px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  background: white;
  font-size: 12px;
  color: #475569;
  cursor: pointer;
  transition: all 0.3s;
}

.action-btn:hover {
  border-color: #ec4899;
  color: #ec4899;
}
</style>