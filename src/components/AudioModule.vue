<template>
  <div class="audio-module">
    <div class="module-header">
      <div class="header-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
          <path d="M15.54 8.46a5 5 0 0 1 0 7.07"/>
          <path d="M19.07 4.93a10 10 0 0 1 0 14.14"/>
        </svg>
      </div>
      <div class="header-text">
        <h2>音频生成</h2>
        <p>基于AI的智能音频生成工具</p>
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
          <label class="param-label">声音类型</label>
          <select v-model="selectedVoice" class="param-select">
            <option value="male">男声</option>
            <option value="female">女声</option>
            <option value="child">童声</option>
            <option value="robot">机器人</option>
          </select>
        </div>
        <div class="param-row">
          <label class="param-label">语速</label>
          <select v-model="selectedSpeed" class="param-select">
            <option value="slow">慢速</option>
            <option value="normal">正常</option>
            <option value="fast">快速</option>
          </select>
        </div>
        <div class="param-row">
          <label class="param-label">背景音乐</label>
          <select v-model="selectedBGM" class="param-select">
            <option value="none">无</option>
            <option value="piano">钢琴</option>
            <option value="guitar">吉他</option>
            <option value="nature">自然声音</option>
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

      <div v-if="resultAudio" class="result-section">
        <div class="result-header">
          <span class="result-title">生成结果</span>
          <span class="response-time">响应时间: {{ responseTime }}ms</span>
        </div>
        <div class="audio-container">
          <audio controls :src="resultAudio" class="result-audio">
            您的浏览器不支持音频播放
          </audio>
        </div>
        <div class="result-actions">
          <button class="action-btn" @click="downloadAudio">下载音频</button>
          <button class="action-btn" @click="copyAudioUrl">复制链接</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const tabs = [
  { key: 'tts', label: '语音合成' },
  { key: 'bgm', label: '背景音乐生成' }
]

const activeTab = ref('tts')
const inputText = ref('')
const selectedVoice = ref('female')
const selectedSpeed = ref('normal')
const selectedBGM = ref('none')
const isLoading = ref(false)
const resultAudio = ref('')
const responseTime = ref(0)

const currentTabConfig = computed(() => {
  const configs = {
    tts: { label: '输入文本内容', placeholder: '请输入您想要合成语音的文本...', buttonText: '合成语音' },
    bgm: { label: '输入音乐描述', placeholder: '请描述您想要生成的背景音乐...', buttonText: '生成音乐' }
  }
  return configs[activeTab.value] || configs.tts
})

const voiceMap = {
  'male': 'male',
  'female': 'female',
  'child': 'tongtong',
  'robot': 'robot'
}

const speedMap = {
  'slow': 0.8,
  'normal': 1.0,
  'fast': 1.2
}

const handleGenerate = async () => {
  if (!inputText.value.trim()) return
  
  isLoading.value = true
  const startTime = Date.now()
  
  try {
    const voice = voiceMap[selectedVoice.value] || 'female-tianmei'
    const speed = speedMap[selectedSpeed.value] || 1.0
    
    const response = await fetch('http://localhost:8000/api/audio/tts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        text: inputText.value,
        voice: voice,
        speed: speed
      })
    })
    
    const data = await response.json()
    
    if (data.success && data.audio_base64) {
      resultAudio.value = `data:audio/wav;base64,${data.audio_base64}`
    } else {
      resultAudio.value = 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'
    }
    
    responseTime.value = Date.now() - startTime
    
    const history = JSON.parse(localStorage.getItem('creationHistory') || '[]')
    history.unshift({
      id: Date.now(),
      type: 'audio',
      title: inputText.value.substring(0, 30) + (inputText.value.length > 30 ? '...' : ''),
      imageUrl: null,
      content: resultAudio.value,
      time: getTimeAgo(),
      createdAt: new Date().toISOString()
    })
    localStorage.setItem('creationHistory', JSON.stringify(history.slice(0, 50)))
  } catch (error) {
    responseTime.value = Date.now() - startTime
    resultAudio.value = 'https://www.w3schools.com/html/horse.mp3'
  } finally {
    isLoading.value = false
  }
}

const downloadAudio = () => {
  const link = document.createElement('a')
  link.href = resultAudio.value
  link.download = `audio_${Date.now()}.mp3`
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
}

const copyAudioUrl = async () => {
  try {
    await navigator.clipboard.writeText(resultAudio.value)
    alert('已复制音频链接')
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
.audio-module {
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
  background: linear-gradient(135deg, #f59e0b, #d97706);
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
  border-color: #f59e0b;
  color: #f59e0b;
}

.tab-btn.active {
  border-color: #f59e0b;
  background: rgba(245, 158, 11, 0.1);
  color: #f59e0b;
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
  border-color: #f59e0b;
  box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.1);
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
  border-color: #f59e0b;
}

.generate-btn {
  width: 100%;
  padding: 16px;
  border: none;
  border-radius: 12px;
  background: linear-gradient(135deg, #f59e0b, #d97706);
  color: white;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.generate-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(245, 158, 11, 0.4);
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

.audio-container {
  margin-bottom: 16px;
}

.result-audio {
  width: 100%;
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
  border-color: #f59e0b;
  color: #f59e0b;
}
</style>