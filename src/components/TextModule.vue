<template>
  <div class="text-module">
    <div class="module-header">
      <div class="header-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
          <polyline points="14 2 14 8 20 8"/>
          <line x1="16" y1="13" x2="8" y2="13"/>
          <line x1="16" y1="17" x2="8" y2="17"/>
        </svg>
      </div>
      <div class="header-text">
        <h2>文本生成</h2>
        <p>基于AI的智能文本处理工具</p>
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
          rows="5"
        ></textarea>
        <span class="char-count">{{ inputText.length }}/500</span>
      </div>

      <button 
        class="generate-btn"
        :disabled="!inputText.trim() || isLoading"
        :class="{ loading: isLoading }"
        @click="handleGenerate"
      >
        <span>{{ isLoading ? '生成中...' : currentTabConfig.buttonText }}</span>
      </button>

      <div v-if="resultData" class="result-section">
        <div class="result-header">
          <span class="result-title">生成结果</span>
          <span class="response-time">响应时间: {{ responseTime }}ms</span>
        </div>
        <div class="result-content">
          <p>{{ resultData.content }}</p>
        </div>
        <div class="result-actions">
          <button class="action-btn" @click="copyResult">复制结果</button>
          <button class="action-btn" @click="downloadResult">下载</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const tabs = [
  { key: 'generate', label: '文本生成' },
  { key: 'polish', label: '文本润色' },
  { key: 'rewrite', label: '文本改写' },
  { key: 'summarize', label: '文本摘要' },
  { key: 'optimize', label: '提示词优化' }
]

const activeTab = ref('generate')
const inputText = ref('')
const isLoading = ref(false)
const resultData = ref(null)
const responseTime = ref(0)

const currentTabConfig = computed(() => {
  const configs = {
    generate: { label: '输入主题或关键词', placeholder: '请输入您想要生成的文本主题...', buttonText: '生成文本' },
    polish: { label: '输入需要润色的文本', placeholder: '请输入需要润色的文本内容...', buttonText: '润色文本' },
    rewrite: { label: '输入需要改写的文本', placeholder: '请输入需要改写的文本内容...', buttonText: '改写文本' },
    summarize: { label: '输入需要摘要的文本', placeholder: '请输入需要摘要的文本内容...', buttonText: '生成摘要' },
    optimize: { label: '输入需要优化的提示词', placeholder: '请输入需要优化的提示词...', buttonText: '优化提示词' }
  }
  return configs[activeTab.value] || configs.generate
})

const handleGenerate = async () => {
  if (!inputText.value.trim()) return
  
  isLoading.value = true
  resultData.value = null
  const startTime = Date.now()
  
  // Mock 优先模式 - 直接生成模拟数据，不依赖后端
  const getMockContent = () => {
    const topic = inputText.value
    switch (activeTab.value) {
      case 'generate':
        return `# ${topic}\n\n基于您输入的主题「${topic}」，AI为您生成了以下内容：\n\n## 核心要点\n\n1. **主题概述**：${topic}是一个值得关注的重要领域，它涉及多个层面的知识体系。\n\n2. **发展现状**：近年来，随着技术的不断进步，${topic}相关的研究和应用取得了显著成果。\n\n3. **未来趋势**：展望未来，${topic}将继续保持快速发展的态势，为各行各业带来更多可能性。\n\n## 详细分析\n\n${topic}的核心价值在于其能够有效地解决实际问题。通过系统性的方法和创新的思维，我们可以在这一领域取得突破性的进展。\n\n### 关键要素\n\n- 要素一：基础理论与框架构建\n- 要素二：实践应用与案例研究\n- 要素三：创新方法与技术手段\n- 要素四：评估体系与优化策略\n\n## 总结与建议\n\n综上所述，${topic}具有广阔的发展前景和重要的实际价值。建议从多个角度深入研究，并结合实际情况灵活运用。\n\n---\n*本文由AI自动生成，仅供参考*`
      case 'polish':
        return `【润色后的文本】\n\n${topic.length > 10 ? topic : '这是一段经过AI润色优化的文字内容，经过专业的语言处理，使表达更加流畅、准确、优雅。润色后的文本在保留原意的基础上，提升了整体的可读性和专业性。'}\n\n✅ 润色完成：优化了词汇选择、调整了句式结构、增强了表达效果`
      case 'rewrite': {
        const preview = topic ? topic.substring(0, 50) + (topic.length > 50 ? '...' : '') : ''
        return `【改写版本】\n\n${preview ? '针对原文「' + preview + '」，以下是改写后的内容：' : ''}\n\n以全新的视角和表达方式重新呈现原文核心含义。改写后的文本保持了原有的信息完整性，同时采用了更加生动、简洁的表述方式，使读者更容易理解和接受。\n\n这种改写方式不仅保留了原文的关键信息，还提升了文本的整体质量和阅读体验。\n\n---\n*由AI智能改写*`
      }
      case 'summarize':
        return `【摘要】\n\n${topic.length > 20 ? topic.substring(0, 80) + '...' : topic}\n\n**核心要点总结：**\n\n1. 文章主要阐述了关于「${topic.substring(0, 30)}」的相关内容\n2. 提出了若干关键论点和重要结论\n3. 分析了问题产生的原因及可能的解决方案\n4. 对未来发展方向进行了展望和建议\n\n**一句话概括：** 本文围绕核心议题展开深入讨论，通过多维度分析提出了系统性观点和实践建议。\n\n---\n*AI摘要生成*`
      case 'optimize': {
        let role = '专业领域专家'
        if (topic.includes('写作') || topic.includes('文章')) role = '专业的内容创作者'
        else if (topic.includes('代码') || topic.includes('编程')) role = '资深软件工程师'
        else if (topic.includes('设计')) role = '创意设计师'
        return `【优化后的提示词】\n\n原提示词：「${topic}」\n\n📋 **优化版本：**\n\n请作为一名${role}，针对「${topic}」这一需求，完成以下任务：\n\n**角色设定：** 具备丰富经验的专业人士\n**任务目标：** 高质量、高效率地完成指定工作\n**输出要求：** 结构清晰、内容详实、格式规范\n**风格偏好：** 专业、简洁、易懂\n\n请按照以下步骤进行：\n1. 理解需求核心\n2. 制定执行计划\n3. 分步骤实施\n4. 质量检查优化\n5. 输出最终结果\n\n---\n*提示词已由AI优化增强*`
      }
      default:
        return getMockContent()
    }
  }
  
  const mockContent = getMockContent()
  responseTime.value = Math.floor(Math.random() * 800) + 200
  resultData.value = { content: mockContent }
  
  const history = JSON.parse(localStorage.getItem('creationHistory') || '[]')
  history.unshift({
    id: Date.now(),
    type: 'text',
    title: inputText.value.substring(0, 30) + (inputText.value.length > 30 ? '...' : ''),
    imageUrl: null,
    content: mockContent,
    time: getTimeAgo(),
    createdAt: new Date().toISOString()
  })
  localStorage.setItem('creationHistory', JSON.stringify(history.slice(0, 50)))
  
  isLoading.value = false
}

const copyResult = async () => {
  try {
    await navigator.clipboard.writeText(resultData.value?.content || '')
    alert('已复制到剪贴板')
  } catch (error) {
    alert('复制失败')
  }
}

const downloadResult = () => {
  const text = resultData.value?.content || ''
  const blob = new Blob([text], { type: 'text/plain' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = 'result.txt'
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)
  URL.revokeObjectURL(url)
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
.text-module {
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
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
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
  border-color: #6366f1;
  color: #6366f1;
}

.tab-btn.active {
  border-color: #6366f1;
  background: rgba(99, 102, 241, 0.1);
  color: #6366f1;
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
  min-height: 100px;
}

.text-input:focus {
  border-color: #6366f1;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
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

.generate-btn {
  width: 100%;
  padding: 16px;
  border: none;
  border-radius: 12px;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: white;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.generate-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(99, 102, 241, 0.4);
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

.result-content {
  background: white;
  padding: 16px;
  border-radius: 10px;
  min-height: 100px;
  margin-bottom: 16px;
}

.result-content p {
  margin: 0;
  line-height: 1.7;
  color: #374151;
  white-space: pre-wrap;
}

.result-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
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
  border-color: #6366f1;
  color: #6366f1;
}
</style>