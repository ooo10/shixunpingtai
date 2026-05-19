<template>
  <div class="video-module">
    <div class="module-header">
      <div class="header-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polygon points="5 3 19 12 5 21 5 3"/>
          <line x1="19" y1="12" x2="23" y2="12"/>
        </svg>
      </div>
      <div class="header-text">
        <h2>视频生成</h2>
        <p>基于AI的智能视频生成工具</p>
      </div>
    </div>

    <div class="tabs-container">
      <button 
        v-for="tab in tabs" 
        :key="tab.key"
        :class="['tab-btn', { active: activeTab === tab.key }]"
        @click="activeTab = tab.key"
      >
        {{ tab.label }}
      </button>
    </div>

    <div class="content-area">
      <div class="input-section">
        <label class="input-label">{{ currentTabConfig.label }}</label>
        <textarea
          v-model="inputText"
          :placeholder="currentTabConfig.placeholder"
          :maxlength="500"
          class="text-input"
          rows="4"
        ></textarea>
        <span class="char-count">{{ inputText.length }}/500</span>
      </div>

      <div class="params-section">
        <div class="param-row">
          <label class="param-label">视频时长</label>
          <select v-model="selectedDuration" class="param-select">
            <option value="short">15秒</option>
            <option value="medium">30秒</option>
            <option value="long">60秒</option>
          </select>
        </div>
        <div class="param-row">
          <label class="param-label">视频风格</label>
          <select v-model="selectedStyle" class="param-select">
            <option value="realistic">写实风格</option>
            <option value="cartoon">卡通风格</option>
            <option value="cinematic">电影风格</option>
            <option value="minimalist">极简风格</option>
          </select>
        </div>
        <div class="param-row">
          <label class="param-label">分辨率</label>
          <select v-model="selectedResolution" class="param-select">
            <option value="720p">720P</option>
            <option value="1080p">1080P</option>
            <option value="4k">4K</option>
          </select>
        </div>
      </div>

      <button 
        class="generate-btn"
        :disabled="!inputText.trim() || isLoading"
        :class="{ loading: isLoading }"
        @click="handleGenerate"
      >
        <span>{{ isLoading ? '生成中...' : currentTabConfig.buttonText }}</span>
      </button>

      <div v-if="resultVideo" class="result-section">
        <div class="result-header">
          <span class="result-title">生成结果</span>
          <span class="response-time">响应时间: {{ responseTime }}ms</span>
        </div>
        <div class="video-container">
          <video controls :src="resultVideo" class="result-video" crossOrigin="anonymous" muted playsinline>
            您的浏览器不支持视频播放
          </video>
        </div>
        <div class="result-actions">
          <button class="action-btn" @click="downloadVideo">下载视频</button>
          <button class="action-btn" @click="copyVideoUrl">复制链接</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const tabs = [
  { key: 'text2video', label: '文本生成视频' },
  { key: 'videoedit', label: '视频编辑' }
]

const activeTab = ref('text2video')
const inputText = ref('')
const selectedDuration = ref('medium')
const selectedStyle = ref('realistic')
const selectedResolution = ref('1080p')
const isLoading = ref(false)
const resultVideo = ref('')
const responseTime = ref(0)

const currentTabConfig = computed(() => {
  const configs = {
    text2video: { label: '输入视频描述', placeholder: '请描述您想要生成的视频内容...', buttonText: '生成视频' },
    videoedit: { label: '输入编辑需求', placeholder: '请描述您想要如何编辑视频...', buttonText: '编辑视频' }
  }
  return configs[activeTab.value] || configs.text2video
})

const handleGenerate = async () => {
  if (!inputText.value.trim()) return
  
  isLoading.value = true
  resultVideo.value = ''
  const startTime = Date.now()
  
  // Mock 优先模式 - 直接生成模拟视频，不依赖后端
  await new Promise(resolve => setTimeout(resolve, Math.random() * 1500 + 800))
  responseTime.value = Date.now() - startTime
  resultVideo.value = generateMockVideo()
  
  // 保存历史记录
  const history = JSON.parse(localStorage.getItem('creationHistory') || '[]')
  history.unshift({
    id: Date.now(),
    type: 'video',
    title: inputText.value.substring(0, 30) + (inputText.value.length > 30 ? '...' : ''),
    imageUrl: null,
    content: resultVideo.value,
    time: getTimeAgo(),
    createdAt: new Date().toISOString()
  })
  localStorage.setItem('creationHistory', JSON.stringify(history.slice(0, 50)))
  
  isLoading.value = false
}

const generateMockVideo = () => {
  const videos = [
    'https://www.w3schools.com/html/mov_bbb.mp4',
    'https://www.w3schools.com/html/movie.mp4'
  ]
  return videos[Math.floor(Math.random() * videos.length)]
}

const downloadVideo = () => {
  const link = document.createElement('a')
  link.href = resultVideo.value
  link.download = `video_${Date.now()}.mp4`
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
}

const copyVideoUrl = async () => {
  try {
    await navigator.clipboard.writeText(resultVideo.value)
    alert('已复制视频链接')
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
.video-module {
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
  background: linear-gradient(135deg, #22c55e, #16a34a);
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
  border-color: #22c55e;
  color: #22c55e;
}

.tab-btn.active {
  border-color: #22c55e;
  background: rgba(34, 197, 94, 0.1);
  color: #22c55e;
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
  border-color: #22c55e;
  box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.1);
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
  border-color: #22c55e;
}

.generate-btn {
  width: 100%;
  padding: 16px;
  border: none;
  border-radius: 12px;
  background: linear-gradient(135deg, #22c55e, #16a34a);
  color: white;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.generate-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(34, 197, 94, 0.4);
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

.video-container {
  background: #1e293b;
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 16px;
}

.result-video {
  width: 100%;
  height: auto;
  max-height: 400px;
}

.result-actions {
  display: flex;
  gap: 12px;
}

.action-btn {
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

.action-btn:hover {
  border-color: #22c55e;
  color: #22c55e;
}
</style>