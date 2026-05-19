<template>
  <div class="workspace-container">
    <aside class="sidebar">
      <div class="sidebar-header">
        <div class="logo-wrapper">
          <svg width="40" height="40" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="sidebarLogoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#3b82f6"/>
                <stop offset="50%" stop-color="#6366f1"/>
                <stop offset="100%" stop-color="#8b5cf6"/>
              </linearGradient>
            </defs>
            <rect x="6" y="6" width="36" height="36" rx="12" fill="url(#sidebarLogoGrad)"/>
            <rect x="14" y="14" width="20" height="20" rx="6" fill="white"/>
            <path d="M24 18L20 26H28L24 18Z" fill="url(#sidebarLogoGrad)"/>
          </svg>
        </div>
        <div class="logo-text-container">
          <span class="logo-title">AIGC实训</span>
          <span class="logo-subtitle">学生平台</span>
        </div>
      </div>
      
      <nav class="sidebar-nav">
        <div class="nav-item" :class="{ active: activeMenu === 'workspace' }" @click="activeMenu = 'workspace'">
          <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="7" height="7" rx="1"/>
            <rect x="14" y="3" width="7" height="7" rx="1"/>
            <rect x="14" y="14" width="7" height="7" rx="1"/>
            <rect x="3" y="14" width="7" height="7" rx="1"/>
          </svg>
          <span class="nav-label">工作台</span>
          <div class="nav-indicator"></div>
        </div>
        
        <div class="nav-item" :class="{ active: activeMenu === 'tasks' }" @click="activeMenu = 'tasks'">
          <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 11l3 3L22 4"/>
            <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>
          </svg>
          <span class="nav-label">实训任务</span>
          <div class="nav-indicator"></div>
        </div>
        
        <div class="nav-item" :class="{ active: activeMenu === 'history' }" @click="activeMenu = 'history'">
          <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
            <line x1="16" y1="2" x2="16" y2="6"/>
            <line x1="8" y1="2" x2="8" y2="6"/>
            <line x1="3" y1="10" x2="21" y2="10"/>
          </svg>
          <span class="nav-label">创作历史</span>
          <div class="nav-indicator"></div>
        </div>
        
        <div class="nav-item" :class="{ active: activeMenu === 'resources' }" @click="activeMenu = 'resources'">
          <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
          </svg>
          <span class="nav-label">学习资源</span>
          <div class="nav-indicator"></div>
        </div>
      </nav>
      
      <div class="sidebar-footer">
        <div class="user-profile">
          <div class="avatar-container">
            <svg width="48" height="48" viewBox="0 0 48 48" fill="none">
              <defs>
                <linearGradient id="avatarGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#3b82f6"/>
                  <stop offset="100%" stop-color="#6366f1"/>
                </linearGradient>
              </defs>
              <circle cx="24" cy="24" r="22" fill="url(#avatarGrad)"/>
              <circle cx="24" cy="18" r="6" fill="white"/>
              <ellipse cx="24" cy="32" rx="8" ry="6" fill="white"/>
            </svg>
            <div class="status-dot online"></div>
          </div>
          <div class="user-info">
            <span class="user-name">{{ currentUsername }}</span>
            <span class="user-class">人工智能2班</span>
          </div>
        </div>
        
        <button class="logout-button" @click="handleLogout">
          <span>退出登录</span>
        </button>
      </div>
    </aside>
    
    <main class="main-content">
      <header class="header">
        <div class="header-greeting">
          <div class="greeting-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"/>
              <path d="M8 14s1.5 2 4 2 4-2 4-2"/>
              <circle cx="9" cy="9" r="1"/>
              <circle cx="15" cy="9" r="1"/>
            </svg>
          </div>
          <div class="greeting-text">
            <h1 class="page-title">你好，{{ currentUsername }}</h1>
            <p class="page-subtitle">今天也要继续努力学习哦！</p>
          </div>
        </div>
        
        <div class="header-actions">
          <button class="action-btn notification-btn">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
              <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
            </svg>
            <span class="badge">3</span>
          </button>
          <button class="action-btn settings-btn">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="3"/>
              <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06 2 3.46a1 1 0 0 1-.24 1.22l-.12.14c-.37.38-.93.38-1.31.02l-2.12-1.24a1.8 1.8 0 0 0-2.22.23l-.09-.07a1.72 1.72 0 0 0-1.88 0l-.09.07a1.8 1.8 0 0 0-2.22-.23l-2.12 1.24a1 1 0 0 1-1.31-.02l-.12-.14a1 1 0 0 1-.24-1.22l.06-.06a1.65 1.65 0 0 0 .33-1.82l-.06-.06-2-3.46a1 1 0 0 1 .24-1.22l.12-.14c.37-.38.93-.38 1.31-.02l2.12 1.24a1.8 1.8 0 0 0 2.22-.23l.09.07a1.72 1.72 0 0 0 1.88 0l.09-.07a1.8 1.8 0 0 0 2.22.23l2.12-1.24a1 1 0 0 1 1.31.02l.12.14a1 1 0 0 1 .24 1.22l-.06.06z"/>
            </svg>
          </button>
        </div>
      </header>

      <div v-if="selectedModule === 'text'" class="module-view">
        <button class="back-btn" @click="selectedModule = null">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M15 19l-7-7 7-7"/>
          </svg>
          返回模块选择
        </button>
        <TextModule />
      </div>
      
      <div v-if="selectedModule === 'image'" class="module-view">
        <button class="back-btn" @click="selectedModule = null">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M15 19l-7-7 7-7"/>
          </svg>
          返回模块选择
        </button>
        <ImageModule />
      </div>
      
      <div v-if="selectedModule === 'video'" class="module-view">
        <button class="back-btn" @click="selectedModule = null">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M15 19l-7-7 7-7"/>
          </svg>
          返回模块选择
        </button>
        <VideoModule />
      </div>
      
      <div v-if="selectedModule === 'audio'" class="module-view">
        <button class="back-btn" @click="selectedModule = null">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M15 19l-7-7 7-7"/>
          </svg>
          返回模块选择
        </button>
        <AudioModule />
      </div>
      
      <template v-if="activeMenu === 'workspace'">
        <div class="modules-section">
          <div class="section-header">
            <h2 class="section-title">实训模块</h2>
            <span class="section-desc">选择一个模块开始你的创作之旅</span>
          </div>
          
          <div class="modules-grid">
            <div class="module-card text-card" @click="openModule('text')">
              <div class="module-icon-wrapper">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                  <polyline points="14 2 14 8 20 8"/>
                  <line x1="16" y1="13" x2="8" y2="13"/>
                  <line x1="16" y1="17" x2="8" y2="17"/>
                </svg>
              </div>
              <div class="module-content">
                <h3 class="module-title">生文本</h3>
                <p class="module-desc">文本生成、润色、改写、摘要</p>
              </div>
              <div class="module-arrow">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M9 18l6-6-6-6"/>
                </svg>
              </div>
            </div>
            
            <div class="module-card image-card" @click="openModule('image')">
              <div class="module-icon-wrapper">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                  <circle cx="8.5" cy="8.5" r="1.5"/>
                  <polyline points="21 15 16 10 5 21"/>
                </svg>
              </div>
              <div class="module-content">
                <h3 class="module-title">生图片</h3>
                <p class="module-desc">文生图、图生图、风格转换</p>
              </div>
              <div class="module-arrow">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M9 18l6-6-6-6"/>
                </svg>
              </div>
            </div>
            
            <div class="module-card video-card" @click="openModule('video')">
              <div class="module-icon-wrapper">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polygon points="23 7 16 12 23 17 23 7"/>
                  <rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>
                </svg>
              </div>
              <div class="module-content">
                <h3 class="module-title">生视频</h3>
                <p class="module-desc">文本生成视频、视频编辑</p>
              </div>
              <div class="module-arrow">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M9 18l6-6-6-6"/>
                </svg>
              </div>
            </div>
            
            <div class="module-card audio-card" @click="openModule('audio')">
              <div class="module-icon-wrapper">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
                  <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/>
                </svg>
              </div>
              <div class="module-content">
                <h3 class="module-title">生音频</h3>
                <p class="module-desc">语音合成、背景音乐生成</p>
              </div>
              <div class="module-arrow">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M9 18l6-6-6-6"/>
                </svg>
              </div>
            </div>
          </div>
        </div>
        
        <div class="stats-section">
          <div class="stat-card task-stat">
            <div class="stat-icon-wrapper">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M9 11l3 3L22 4"/>
                <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>
              </svg>
            </div>
            <div class="stat-info">
              <span class="stat-value">{{ pendingTasksCount }}</span>
              <span class="stat-label">待完成任务</span>
            </div>
            <div class="stat-progress">
              <div class="progress-bar">
                <div class="progress-fill" :style="{ width: progressPercent + '%' }"></div>
              </div>
              <span class="progress-text">本周进度 {{ progressPercent }}%</span>
            </div>
          </div>
          
          <div class="stat-card completed-stat">
            <div class="stat-icon-wrapper">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                <polyline points="22 4 12 14.01 9 11.01"/>
              </svg>
            </div>
            <div class="stat-info">
              <span class="stat-value">{{ completedTasksCount }}</span>
              <span class="stat-label">已完成任务</span>
            </div>
            <div class="stat-trend positive">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/>
                <polyline points="17 6 23 6 23 12"/>
              </svg>
              <span>↑ {{ completedTasksCount * 5 }}%</span>
            </div>
          </div>
          
          <div class="stat-card project-stat">
            <div class="stat-icon-wrapper">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                <path d="M16 7a4 4 0 1 1-8 0 4 4 0 0 1 8 0z"/>
              </svg>
            </div>
            <div class="stat-info">
              <span class="stat-value">{{ portfolioCount }}</span>
              <span class="stat-label">作品集</span>
            </div>
            <div class="stat-badge" @click="activeMenu = 'history'">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 8v4l3 3"/>
              </svg>
              <span>查看</span>
            </div>
          </div>
          
          <div class="stat-card score-stat">
            <div class="stat-icon-wrapper">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
              </svg>
            </div>
            <div class="stat-info">
              <span class="stat-value">{{ overallScore }}</span>
              <span class="stat-label">综合评分</span>
            </div>
            <div class="stat-rating">
              <svg v-for="i in 5" :key="i" viewBox="0 0 24 24" :fill="i <= starRating ? 'currentColor' : 'none'" stroke="currentColor" stroke-width="2">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
              </svg>
            </div>
          </div>
        </div>
        
        <div class="recent-activity-section">
          <div class="section-header">
            <h2 class="section-title">最近活动</h2>
            <button class="view-all-btn">查看全部</button>
          </div>
          
          <div v-if="recentActivities.length > 0" class="activity-list">
            <div class="activity-item" v-for="(item, index) in recentActivities" :key="index">
              <div class="activity-icon-wrapper" :class="item.type">
                <svg v-if="item.type === 'text'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                  <polyline points="14 2 14 8 20 8"/>
                </svg>
                <svg v-else-if="item.type === 'image'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                  <circle cx="8.5" cy="8.5" r="1.5"/>
                </svg>
                <svg v-else-if="item.type === 'video'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polygon points="23 7 16 12 23 17 23 7"/>
                  <rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>
                </svg>
                <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
                </svg>
              </div>
              <div class="activity-content">
                <p class="activity-title">{{ item.title }}</p>
                <p class="activity-time">{{ item.time }}</p>
              </div>
              <div class="activity-status" :class="item.status">
                {{ item.statusText }}
              </div>
            </div>
          </div>
          
          <div v-else class="empty-activities">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 8v4l3 3"/>
              <circle cx="12" cy="12" r="9"/>
            </svg>
            <p>暂无活动记录</p>
            <span>完成任务或进行创作后，活动记录将显示在这里</span>
          </div>
        </div>
      </template>

      <template v-else-if="activeMenu === 'tasks'">
        <div class="page-container">
          <div class="page-header">
            <h2 class="page-title">实训任务</h2>
            <p class="page-desc">查看和管理你的实训任务</p>
          </div>
          
          <div class="task-filters">
            <button 
              v-for="filter in taskFilters" 
              :key="filter.value"
              :class="['filter-btn', { active: activeTaskFilter === filter.value }]"
              @click="activeTaskFilter = filter.value"
            >
              {{ filter.label }}
              <span v-if="filter.count" class="filter-count">{{ filter.count }}</span>
            </button>
          </div>
          
          <div v-if="filteredTasks.length > 0" class="task-list">
            <div v-for="task in filteredTasks" :key="task.id" class="task-card" @click="openTaskDetail(task)">
              <div class="task-status" :class="task.status"></div>
              <div class="task-content">
                <h3 class="task-title">{{ task.title }}</h3>
                <p class="task-desc">{{ task.description }}</p>
                <div class="task-meta">
                  <span class="task-tag">{{ task.category }}</span>
                  <span class="task-deadline">截止日期: {{ task.deadline }}</span>
                </div>
              </div>
              <div class="task-actions">
                <button class="action-btn primary" @click.stop="startTask(task)">
                  {{ task.status === 'completed' ? '重新完成' : '开始任务' }}
                </button>
              </div>
              <div class="task-arrow">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M9 18l6-6-6-6"/>
                </svg>
              </div>
            </div>
          </div>
          <div v-else class="empty-tasks">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 11l3 3L22 4"/>
              <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>
            </svg>
            <p>暂无实训任务</p>
            <span>完成创作后会自动生成相关任务</span>
          </div>
        </div>
      </template>

      <template v-else-if="activeMenu === 'history'">
        <div class="page-container">
          <div class="page-header">
            <h2 class="page-title">创作历史</h2>
            <p class="page-desc">回顾你的创作记录</p>
          </div>
          
          <div class="history-tabs">
            <button 
              v-for="tab in historyTabs" 
              :key="tab.value"
              :class="['history-tab', { active: activeHistoryTab === tab.value }]"
              @click="activeHistoryTab = tab.value"
            >
              {{ tab.label }}
            </button>
          </div>
          
          <div v-if="filteredHistoryItems.length > 0" class="history-grid">
            <div v-for="item in filteredHistoryItems" :key="item.id" class="history-card">
              <div class="history-thumbnail" :style="{ backgroundImage: item.imageUrl ? `url(${item.imageUrl})` : 'none' }">
                <svg v-if="!item.imageUrl && item.type === 'text'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                  <polyline points="14 2 14 8 20 8"/>
                </svg>
                <svg v-else-if="!item.imageUrl && item.type === 'image'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                  <circle cx="8.5" cy="8.5" r="1.5"/>
                </svg>
                <svg v-else-if="!item.imageUrl && item.type === 'video'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polygon points="23 7 16 12 23 17 23 7"/>
                  <rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>
                </svg>
                <svg v-else-if="!item.imageUrl" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
                </svg>
              </div>
              <div class="history-info">
                <h4 class="history-title">{{ item.title }}</h4>
                <p class="history-time">{{ item.time }}</p>
              </div>
              <div class="history-actions">
                <button class="action-btn">查看</button>
              </div>
            </div>
          </div>
          <div v-else class="empty-history">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
              <line x1="16" y1="2" x2="16" y2="6"/>
              <line x1="8" y1="2" x2="8" y2="6"/>
              <line x1="3" y1="10" x2="21" y2="10"/>
            </svg>
            <p>暂无创作记录</p>
            <span>在工作台中完成创作后，记录将显示在这里</span>
          </div>
        </div>
      </template>

      <template v-else-if="activeMenu === 'resources'">
        <div class="page-container">
          <div class="page-header">
            <h2 class="page-title">学习资源</h2>
            <p class="page-desc">探索学习材料和教程</p>
          </div>
          
          <div class="resource-categories">
            <button 
              v-for="cat in resourceCategories" 
              :key="cat.value"
              :class="['category-btn', { active: activeResourceCategory === cat.value }]"
              @click="activeResourceCategory = cat.value"
            >
              {{ cat.icon }} {{ cat.label }}
            </button>
          </div>
          
          <div class="resource-list">
            <div 
              v-for="resource in filteredResources" 
              :key="resource.id" 
              class="resource-card"
              @click="openResourceDetail(resource)"
            >
              <div class="resource-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                  <polyline points="7 10 12 15 17 10"/>
                  <line x1="12" y1="15" x2="12" y2="3"/>
                </svg>
              </div>
              <div class="resource-content">
                <h3 class="resource-title">{{ resource.title }}</h3>
                <p class="resource-desc">{{ resource.description }}</p>
                <div class="resource-meta">
                  <span class="resource-type">{{ resource.type }}</span>
                  <span class="resource-duration">{{ resource.duration }}</span>
                </div>
              </div>
              <div class="resource-progress">
                <div class="progress-bar">
                  <div class="progress-fill" :style="{ width: resource.progress + '%' }"></div>
                </div>
                <span class="progress-text">{{ resource.progress }}%</span>
              </div>
              <div class="resource-arrow">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polyline points="9 18 15 12 9 6"/>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </template>
    </main>

    <div v-if="showResourceModal" class="modal-overlay" @click.self="closeResourceModal">
      <div class="modal-content">
        <div class="modal-header">
          <div class="modal-title">{{ selectedResource?.title }}</div>
          <button class="modal-close" @click="closeResourceModal">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="18" y1="6" x2="6" y2="18"/>
              <line x1="6" y1="6" x2="18" y2="18"/>
            </svg>
          </button>
        </div>
        <div class="modal-body">
          <div class="resource-detail">
            <div class="detail-meta">
              <span class="detail-type">{{ selectedResource?.type }}</span>
              <span class="detail-duration">{{ selectedResource?.duration }}</span>
            </div>
            <div class="detail-description">{{ selectedResource?.description }}</div>
            <div class="detail-content" v-html="renderMarkdown(selectedResource?.content)"></div>
          </div>
        </div>
        <div class="modal-footer">
          <button class="modal-button" @click="closeResourceModal">关闭</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import TextModule from '../components/TextModule.vue'
import ImageModule from '../components/ImageModule.vue'
import VideoModule from '../components/VideoModule.vue'
import AudioModule from '../components/AudioModule.vue'

const router = useRouter()

const initializeData = () => {
  const initialTasks = [
    { id: 1, title: '文本生成基础训练', description: '学习使用AI生成高质量文本内容', category: '文本生成', deadline: '2024-01-20', status: 'pending' },
    { id: 2, title: '产品宣传文案创作', description: '为产品撰写吸引人的宣传文案', category: '文本生成', deadline: '2024-01-22', status: 'pending' },
    { id: 3, title: '图片生成实践', description: '掌握文生图、图生图等功能', category: '图像生成', deadline: '2024-01-25', status: 'pending' },
    { id: 4, title: '校园海报设计', description: '设计一张精美的校园活动海报', category: '图像生成', deadline: '2024-01-28', status: 'pending' },
    { id: 5, title: '视频剪辑实训', description: '学习视频合成和剪辑技术', category: '视频生成', deadline: '2024-02-01', status: 'pending' },
    { id: 6, title: '音频合成练习', description: '练习语音合成和背景音乐生成', category: '音频生成', deadline: '2024-02-05', status: 'pending' },
  ]

  const initialActivities = [
    { type: 'text', title: '开始任务：文本生成基础训练', time: '5分钟前', status: 'pending', statusText: '进行中' },
    { type: 'image', title: '完成任务：校园海报设计', time: '30分钟前', status: 'success', statusText: '已完成' },
    { type: 'video', title: '开始任务：视频剪辑实训', time: '1小时前', status: 'pending', statusText: '进行中' },
    { type: 'audio', title: '创作记录：生成背景音乐', time: '2小时前', status: 'success', statusText: '已完成' },
    { type: 'text', title: '创作记录：生成产品文案', time: '3小时前', status: 'success', statusText: '已完成' },
  ]

  if (!localStorage.getItem('tasks')) {
    localStorage.setItem('tasks', JSON.stringify(initialTasks))
  }
  if (!localStorage.getItem('historyItems')) {
    localStorage.setItem('historyItems', JSON.stringify([]))
  }
  if (!localStorage.getItem('recentActivities')) {
    localStorage.setItem('recentActivities', JSON.stringify(initialActivities))
  }
}

onMounted(() => {
  // 清理旧的最近活动数据，确保显示示例
  localStorage.removeItem('recentActivities')
  initializeData()
})

const activeMenu = ref('workspace')
const selectedModule = ref(null)
const activeTaskFilter = ref('all')
const activeHistoryTab = ref('all')
const activeResourceCategory = ref('all')
const showResourceModal = ref(false)
const selectedResource = ref(null)

const currentUsername = computed(() => {
  return localStorage.getItem('currentUsername') || '同学'
})

const recentActivities = computed(() => {
  const stored = localStorage.getItem('recentActivities')
  if (stored) {
    return JSON.parse(stored)
  }
  return []
})

const tasks = computed(() => {
  const stored = localStorage.getItem('tasks')
  if (stored) {
    try {
      const parsed = JSON.parse(stored)
      if (parsed && Array.isArray(parsed) && parsed.length > 0) {
        return parsed
      }
    } catch (e) {
      console.error('Failed to parse tasks:', e)
    }
  }
  return []
})

const taskFilters = computed(() => [
  { value: 'all', label: '全部', count: tasks.value.length },
  { value: 'pending', label: '待完成', count: tasks.value.filter(t => t.status === 'pending').length },
  { value: 'in-progress', label: '进行中', count: tasks.value.filter(t => t.status === 'in-progress').length },
  { value: 'completed', label: '已完成', count: tasks.value.filter(t => t.status === 'completed').length },
])

const filteredTasks = computed(() => {
  if (activeTaskFilter.value === 'all') return tasks.value
  return tasks.value.filter(task => task.status === activeTaskFilter.value)
})

const pendingTasksCount = computed(() => {
  return tasks.value.filter(t => t.status === 'pending').length
})

const completedTasksCount = computed(() => {
  return tasks.value.filter(t => t.status === 'completed').length
})

const totalTasksCount = computed(() => {
  return tasks.value.length
})

const progressPercent = computed(() => {
  if (totalTasksCount.value === 0) return 0
  return Math.round((completedTasksCount.value / totalTasksCount.value) * 100)
})

const portfolioCount = computed(() => {
  return historyItems.value.length
})

const overallScore = computed(() => {
  const baseScore = 60
  const completionBonus = completedTasksCount.value * 5
  const maxScore = 100
  return Math.min(baseScore + completionBonus, maxScore)
})

const starRating = computed(() => {
  return Math.min(Math.floor(overallScore.value / 20), 5)
})

const historyTabs = [
  { value: 'all', label: '全部' },
  { value: 'text', label: '文本' },
  { value: 'image', label: '图片' },
  { value: 'video', label: '视频' },
  { value: 'audio', label: '音频' },
]

const historyItems = computed(() => {
  const stored = localStorage.getItem('creationHistory')
  if (stored) {
    return JSON.parse(stored)
  }
  return []
})

const filteredHistoryItems = computed(() => {
  if (activeHistoryTab.value === 'all') return historyItems.value
  return historyItems.value.filter(item => item.type === activeHistoryTab.value)
})

const resourceCategories = [
  { value: 'all', label: '全部', icon: '📚' },
  { value: 'text', label: '文本', icon: '📝' },
  { value: 'image', label: '图片', icon: '🖼️' },
  { value: 'video', label: '视频', icon: '🎬' },
  { value: 'audio', label: '音频', icon: '🎵' },
]

const resources = [
  { id: 1, title: 'AI文本生成入门指南', description: '学习如何使用AI生成高质量文本内容', type: '教程', duration: '30分钟', progress: 75, category: 'text', content: '## AI文本生成入门指南\n\n### 第一章：什么是AI文本生成\n\nAI文本生成是指利用人工智能模型自动生成人类可读文本的技术。近年来，随着Transformer架构的发展，AI文本生成技术取得了突破性进展。\n\n### 第二章：主要应用场景\n\n1. **内容创作**：自动生成文章、故事、诗歌等\n2. **代码生成**：根据描述生成代码\n3. **对话系统**：智能客服、聊天机器人\n4. **摘要生成**：自动生成文本摘要\n\n### 第三章：常用提示词技巧\n\n- 使用明确的指令\n- 提供示例\n- 设定格式要求\n- 控制输出长度\n\n### 第四章：实践练习\n\n尝试使用文本生成功能，输入以下提示词：\n- \"写一篇关于人工智能的短文\"\n- \"生成一段产品描述\"\n- \"创作一首诗\"' },
  { id: 2, title: 'Prompt工程最佳实践', description: '掌握编写有效提示词的技巧', type: '教程', duration: '45分钟', progress: 50, category: 'text', content: '## Prompt工程最佳实践\n\n### 什么是Prompt工程\n\nPrompt工程是指设计和优化提示词以获得更好的AI模型输出的过程。\n\n### 基本原则\n\n1. **清晰明确**：使用精确的语言\n2. **提供上下文**：给出必要的背景信息\n3. **设定格式**：指定输出格式要求\n4. **使用示例**：提供输入输出示例\n\n### 高级技巧\n\n- 链式思考（Chain of Thought）\n- 角色设定\n- 约束条件\n- 多模态提示\n\n### 常见错误\n\n- 提示过于模糊\n- 缺乏上下文\n- 格式不明确' },
  { id: 3, title: '图片风格转换技术', description: '学习不同风格的图片生成方法', type: '教程', duration: '1小时', progress: 30, category: 'image', content: '## 图片风格转换技术\n\n### 概述\n\n图片风格转换是指将一张图片的风格应用到另一张图片上的技术。\n\n### 主要技术方法\n\n1. **神经网络风格迁移**\n2. **基于GAN的风格转换**\n3. **扩散模型风格控制**\n\n### 实践指南\n\n尝试生成不同风格的图片：\n- 写实风格\n- 卡通风格\n- 油画风格\n- 像素风格\n\n### 提示词示例\n\n\"一只可爱的猫，水彩风格\"\n\"城市夜景，赛博朋克风格\"\n\"风景照片，印象派油画风格\"' },
  { id: 4, title: '视频生成基础', description: '了解AI视频生成的基本原理', type: '教程', duration: '50分钟', progress: 10, category: 'video', content: '## 视频生成基础\n\n### AI视频生成技术\n\nAI视频生成是近年来发展迅速的领域，允许用户从文本描述生成视频内容。\n\n### 主要应用\n\n1. **内容创作**：快速生成视频素材\n2. **教育视频**：自动生成教学内容\n3. **广告制作**：快速制作产品展示\n\n### 使用建议\n\n- 保持描述简洁明确\n- 指定视频时长\n- 选择合适的风格\n\n### 实践练习\n\n尝试输入不同的视频描述：\n- \"一只小猫在草地上玩耍\"\n- \"城市日落的延时摄影\"\n- \"海洋波浪的慢动作\"' },
  { id: 5, title: '音频合成原理', description: '学习语音合成和音频处理技术', type: '教程', duration: '40分钟', progress: 25, category: 'audio', content: '## 音频合成原理\n\n### 语音合成技术\n\n语音合成（TTS）是将文本转换为语音的技术。\n\n### 主要技术\n\n1. **基于规则的合成**\n2. **统计参数合成**\n3. **神经网络合成**\n\n### 音频处理\n\n- 语音转换\n- 音频降噪\n- 音效添加\n\n### 实践指南\n\n尝试将文本转换为语音：\n- 选择不同的音色\n- 调整语速\n- 添加背景音乐' },
  { id: 6, title: 'AI写作技巧', description: '掌握AI辅助写作的实用技巧', type: '教程', duration: '35分钟', progress: 60, category: 'text', content: '## AI写作技巧\n\n### AI辅助写作工作流程\n\n1. **构思阶段**：使用AI生成创意\n2. **初稿阶段**：快速生成初稿\n3. **修改阶段**：AI辅助润色\n4. **校对阶段**：检查语法和风格\n\n### 实用技巧\n\n- 使用AI生成大纲\n- 让AI提供多个版本\n- 使用AI进行改写和润色\n- 结合人类创意和AI效率\n\n### 写作提示词示例\n\n\"写一篇关于人工智能未来发展的文章大纲\"\n\"将以下文本改写得更正式\"\n\"为这篇文章添加引言和结论\"' },
  { id: 7, title: '图像风格迁移', description: '深入学习图像风格迁移算法', type: '教程', duration: '55分钟', progress: 15, category: 'image', content: '## 图像风格迁移\n\n### 深度卷积神经网络风格迁移\n\n2015年提出的Neural Style Transfer是图像风格迁移的里程碑。\n\n### 算法原理\n\n1. 使用预训练的CNN提取特征\n2. 定义内容损失和风格损失\n3. 通过优化生成风格化图像\n\n### 现代方法\n\n- 实时风格迁移\n- 基于风格向量的方法\n- 扩散模型风格控制\n\n### 实践练习\n\n尝试不同的风格组合，探索图像生成的无限可能。' },
  { id: 8, title: '视频剪辑AI工具', description: '掌握AI视频剪辑工具的使用', type: '教程', duration: '1小时10分钟', progress: 40, category: 'video', content: '## 视频剪辑AI工具\n\n### AI辅助视频剪辑\n\n人工智能正在改变视频制作的方式。\n\n### AI视频工具功能\n\n1. **自动剪辑**：AI识别精彩片段\n2. **智能配音**：自动生成旁白\n3. **场景识别**：自动分割场景\n4. **风格转换**：更改视频风格\n\n### 学习路径\n\n1. 了解视频基础概念\n2. 学习AI工具使用\n3. 实践视频创作\n4. 掌握高级技巧\n\n### 实践项目\n\n尝试使用视频生成功能创建你的第一个AI视频作品！' },
]

const filteredResources = computed(() => {
  if (activeResourceCategory.value === 'all') return resources
  return resources.filter(r => r.category === activeResourceCategory.value)
})

const openResourceDetail = (resource) => {
  selectedResource.value = resource
  showResourceModal.value = true
}

const closeResourceModal = () => {
  showResourceModal.value = false
  selectedResource.value = null
}

const renderMarkdown = (content) => {
  if (!content) return ''
  let html = content
    .replace(/^### (.+)$/gm, '<h3>$1</h3>')
    .replace(/^## (.+)$/gm, '<h2>$1</h2>')
    .replace(/^# (.+)$/gm, '<h1>$1</h1>')
    .replace(/^\- (.+)$/gm, '<li>$1</li>')
    .replace(/^\d+\. (.+)$/gm, '<li>$1</li>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\n\n/g, '</p><p>')
    .replace(/\n/g, '<br>')
  return `<p>${html}</p>`
}

const openModule = (module) => {
  selectedModule.value = module
}

const openTaskDetail = (task) => {
  selectedModule.value = getModuleFromCategory(task.category)
}

const getModuleFromCategory = (category) => {
  if (category.includes('文本')) return 'text'
  if (category.includes('图像') || category.includes('图片')) return 'image'
  if (category.includes('视频')) return 'video'
  if (category.includes('音频')) return 'audio'
  return 'text'
}

const startTask = (task) => {
  const allTasks = JSON.parse(localStorage.getItem('tasks') || '[]')
  const taskIndex = allTasks.findIndex(t => t.id === task.id)
  if (taskIndex !== -1) {
    allTasks[taskIndex].status = task.status === 'completed' ? 'pending' : 'in-progress'
    localStorage.setItem('tasks', JSON.stringify(allTasks))
    addActivity(task.title, task.status === 'completed' ? 'restart' : 'start')
  }
}

const completeTask = (taskId) => {
  const allTasks = JSON.parse(localStorage.getItem('tasks') || '[]')
  const taskIndex = allTasks.findIndex(t => t.id === taskId)
  if (taskIndex !== -1) {
    allTasks[taskIndex].status = 'completed'
    localStorage.setItem('tasks', JSON.stringify(allTasks))
  }
}

const addHistoryItem = (type, title, imageUrl = null) => {
  const items = JSON.parse(localStorage.getItem('creationHistory') || '[]')
  const newItem = {
    id: Date.now(),
    type,
    title,
    time: getTimeAgo(),
    imageUrl
  }
  items.unshift(newItem)
  localStorage.setItem('creationHistory', JSON.stringify(items.slice(0, 20)))
}

const addActivity = (title, action) => {
  const activities = JSON.parse(localStorage.getItem('recentActivities') || '[]')
  const newActivity = {
    id: Date.now(),
    type: action === 'complete' ? 'text' : 'video',
    title: `${action === 'start' ? '开始任务' : action === 'complete' ? '完成任务' : '重新开始'}: ${title}`,
    time: getTimeAgo(),
    status: action === 'complete' ? 'success' : 'pending',
    statusText: action === 'complete' ? '已完成' : '进行中'
  }
  activities.unshift(newActivity)
  localStorage.setItem('recentActivities', JSON.stringify(activities.slice(0, 10)))
}

const addNewTask = (type, title, description) => {
  const tasks = JSON.parse(localStorage.getItem('tasks') || '[]')
  const categories = {
    text: '文本生成',
    image: '图像生成',
    video: '视频生成',
    audio: '音频生成'
  }
  const newTask = {
    id: Date.now(),
    title,
    description,
    category: categories[type] || '综合训练',
    deadline: getNextWeekDate(),
    status: 'pending'
  }
  tasks.push(newTask)
  localStorage.setItem('tasks', JSON.stringify(tasks))
  addActivity(title, 'new')
}

const getNextWeekDate = () => {
  const date = new Date()
  date.setDate(date.getDate() + 7)
  return date.toISOString().split('T')[0]
}

const getTimeAgo = () => {
  const now = new Date()
  const minutes = Math.floor(Math.random() * 60)
  const hours = Math.floor(Math.random() * 24)
  if (hours === 0) return `${minutes}分钟前`
  if (hours < 24) return `${hours}小时前`
  return `${Math.floor(hours / 24)}天前`
}

const handleLogout = () => {
  localStorage.removeItem('currentRole')
  router.push('/')
}
</script>

<style scoped>
.workspace-container {
  display: flex;
  height: 100vh;
  background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
}

.sidebar {
  width: 280px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  display: flex;
  flex-direction: column;
  box-shadow: 6px 0 40px rgba(99, 102, 241, 0.06);
  border-right: 1px solid rgba(99, 102, 241, 0.08);
}

.sidebar-header {
  padding: 24px;
  display: flex;
  align-items: center;
  gap: 14px;
  border-bottom: 1px solid rgba(226, 232, 240, 0.6);
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.04), rgba(99, 102, 241, 0.03));
}

.logo-text-container {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.logo-title {
  font-size: 18px;
  font-weight: 800;
  background: linear-gradient(135deg, #3b82f6, #6366f1);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.logo-subtitle {
  font-size: 11px;
  color: #94a3b8;
  font-weight: 600;
  letter-spacing: 0.5px;
}

.sidebar-nav {
  flex: 1;
  padding: 20px 12px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 16px;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  color: #64748b;
  font-weight: 600;
  font-size: 14px;
  position: relative;
  overflow: hidden;
}

.nav-item::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background: linear-gradient(135deg, #3b82f6, #6366f1);
  border-radius: 0 2px 2px 0;
  opacity: 0;
  transform: scaleY(0);
  transition: all 0.3s ease;
}

.nav-item:hover {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.06), rgba(99, 102, 241, 0.04));
  color: #1e293b;
}

.nav-item:hover::before {
  opacity: 0.5;
  transform: scaleY(0.6);
}

.nav-item.active {
  background: linear-gradient(135deg, #3b82f6, #6366f1);
  color: white;
  box-shadow: 0 8px 24px rgba(59, 130, 246, 0.3);
}

.nav-item.active::before {
  opacity: 1;
  transform: scaleY(1);
}

.nav-icon {
  width: 22px;
  height: 22px;
  stroke-width: 2.2px;
}

.nav-indicator {
  width: 6px;
  height: 6px;
  background: white;
  border-radius: 50%;
  margin-left: auto;
  opacity: 0;
}

.nav-item.active .nav-indicator {
  opacity: 1;
  animation: pulseDot 2s infinite;
}

@keyframes pulseDot {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.3); opacity: 0.7; }
}

.sidebar-footer {
  padding: 20px;
  border-top: 1px solid rgba(226, 232, 240, 0.6);
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.02), rgba(59, 130, 246, 0.03));
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  background: rgba(248, 250, 252, 0.8);
  border-radius: 14px;
  border: 1px solid rgba(59, 130, 246, 0.08);
}

.avatar-container {
  position: relative;
}

.status-dot {
  position: absolute;
  bottom: 2px;
  right: 2px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: 2px solid white;
}

.status-dot.online {
  background: #10b981;
}

.user-info {
  flex: 1;
}

.user-name {
  display: block;
  font-weight: 700;
  color: #1e293b;
  font-size: 14px;
}

.user-class {
  font-size: 12px;
  color: #64748b;
  font-weight: 500;
}

.logout-button {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 14px 16px;
  border-radius: 12px;
  border: none;
  background: linear-gradient(135deg, rgba(239, 68, 68, 0.06), rgba(220, 38, 38, 0.04));
  color: #ef4444;
  font-weight: 600;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.logout-button:hover {
  background: linear-gradient(135deg, rgba(239, 68, 68, 0.12), rgba(220, 38, 38, 0.08));
}

.main-content {
  flex: 1;
  overflow-y: auto;
  padding: 32px;
}

.main-content::-webkit-scrollbar {
  width: 8px;
}

.main-content::-webkit-scrollbar-track {
  background: transparent;
}

.main-content::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, #3b82f6, #6366f1);
  border-radius: 4px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 32px;
  padding: 20px 24px;
  background: white;
  border-radius: 20px;
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.06);
}

.header-greeting {
  display: flex;
  align-items: center;
  gap: 16px;
}

.greeting-icon {
  width: 52px;
  height: 52px;
  border-radius: 14px;
  background: linear-gradient(135deg, rgba(251, 191, 36, 0.12), rgba(245, 158, 11, 0.08));
  display: flex;
  align-items: center;
  justify-content: center;
  color: #f59e0b;
}

.greeting-icon svg {
  width: 28px;
  height: 28px;
  stroke-width: 2.2px;
}

.page-title {
  font-size: 26px;
  font-weight: 800;
  color: #1e293b;
  margin: 0;
}

.page-subtitle {
  color: #64748b;
  font-size: 14px;
  margin: 4px 0 0 0;
}

.header-actions {
  display: flex;
  gap: 12px;
}

.action-btn {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  border: none;
  background: rgba(148, 163, 184, 0.08);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  transition: all 0.3s ease;
  color: #64748b;
}

.action-btn:hover {
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
  transform: translateY(-2px);
}

.action-btn svg {
  width: 20px;
  height: 20px;
  stroke-width: 2.2px;
}

.badge {
  position: absolute;
  top: 6px;
  right: 6px;
  min-width: 20px;
  height: 20px;
  background: linear-gradient(135deg, #ec4899, #f472b6);
  color: white;
  border-radius: 10px;
  font-size: 11px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 5px;
}

.modules-section {
  margin-bottom: 32px;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.section-title {
  font-size: 22px;
  font-weight: 800;
  color: #1e293b;
  margin: 0;
}

.section-desc {
  color: #64748b;
  font-size: 14px;
}

.modules-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
}

.module-card {
  background: white;
  border-radius: 20px;
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  border: 2px solid transparent;
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.04);
}

.module-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 20px 48px rgba(99, 102, 241, 0.12);
}

.module-icon-wrapper {
  width: 56px;
  height: 56px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.text-card .module-icon-wrapper {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.12), rgba(99, 102, 241, 0.08));
  color: #3b82f6;
}

.image-card .module-icon-wrapper {
  background: linear-gradient(135deg, rgba(236, 72, 153, 0.12), rgba(244, 114, 182, 0.08));
  color: #ec4899;
}

.video-card .module-icon-wrapper {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(52, 211, 153, 0.08));
  color: #10b981;
}

.audio-card .module-icon-wrapper {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.12), rgba(251, 191, 36, 0.08));
  color: #f59e0b;
}

.module-card:hover .module-icon-wrapper {
  transform: scale(1.15);
}

.module-icon-wrapper svg {
  width: 26px;
  height: 26px;
  stroke-width: 2.2px;
}

.module-content {
  flex: 1;
}

.module-title {
  font-size: 20px;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 4px;
}

.module-desc {
  font-size: 14px;
  color: #64748b;
}

.module-arrow {
  display: flex;
  justify-content: flex-end;
  color: #94a3b8;
  transition: all 0.3s ease;
}

.module-card:hover .module-arrow {
  color: #3b82f6;
  transform: translateX(4px);
}

.module-arrow svg {
  width: 20px;
  height: 20px;
}

.stats-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
  margin-bottom: 32px;
}

.stat-card {
  background: white;
  border-radius: 20px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.04);
  border: 1px solid rgba(99, 102, 241, 0.06);
}

.stat-icon-wrapper {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.task-stat .stat-icon-wrapper {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.12), rgba(99, 102, 241, 0.08));
  color: #3b82f6;
}

.completed-stat .stat-icon-wrapper {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(52, 211, 153, 0.08));
  color: #10b981;
}

.project-stat .stat-icon-wrapper {
  background: linear-gradient(135deg, rgba(236, 72, 153, 0.12), rgba(244, 114, 182, 0.08));
  color: #ec4899;
}

.score-stat .stat-icon-wrapper {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.12), rgba(251, 191, 36, 0.08));
  color: #f59e0b;
}

.stat-icon-wrapper svg {
  width: 24px;
  height: 24px;
  stroke-width: 2.2px;
}

.stat-info {
  display: flex;
  align-items: baseline;
  gap: 8px;
}

.stat-value {
  font-size: 32px;
  font-weight: 800;
  color: #1e293b;
}

.stat-label {
  color: #64748b;
  font-size: 14px;
  font-weight: 500;
}

.stat-progress {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.progress-bar {
  height: 6px;
  background: rgba(148, 163, 184, 0.12);
  border-radius: 3px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #3b82f6, #6366f1);
  border-radius: 3px;
  transition: width 0.6s ease;
}

.progress-text {
  font-size: 12px;
  color: #64748b;
  font-weight: 500;
}

.stat-trend {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 700;
  align-self: flex-start;
}

.stat-trend.positive {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(52, 211, 153, 0.08));
  color: #10b981;
}

.stat-trend svg {
  width: 16px;
  height: 16px;
}

.stat-badge {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  background: linear-gradient(135deg, rgba(236, 72, 153, 0.1), rgba(244, 114, 182, 0.06));
  color: #ec4899;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 600;
  align-self: flex-start;
  cursor: pointer;
  transition: all 0.3s ease;
}

.stat-badge:hover {
  background: linear-gradient(135deg, rgba(236, 72, 153, 0.15), rgba(244, 114, 182, 0.1));
  transform: translateY(-2px);
}

.stat-badge svg {
  width: 16px;
  height: 16px;
}

.stat-rating {
  display: flex;
  gap: 2px;
}

.stat-rating svg {
  width: 18px;
  height: 18px;
  color: #fbbf24;
}

.recent-activity-section {
  background: white;
  border-radius: 20px;
  padding: 28px;
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.04);
}

.view-all-btn {
  padding: 10px 20px;
  background: rgba(59, 130, 246, 0.08);
  color: #3b82f6;
  border: none;
  border-radius: 10px;
  font-weight: 600;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.view-all-btn:hover {
  background: rgba(59, 130, 246, 0.12);
}

.activity-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.activity-item {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 16px;
  border-radius: 14px;
  transition: all 0.3s ease;
  cursor: pointer;
}

.activity-item:hover {
  background: rgba(99, 102, 241, 0.04);
  transform: translateX(4px);
}

.activity-icon-wrapper {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.activity-icon-wrapper.text {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.12), rgba(99, 102, 241, 0.08));
  color: #3b82f6;
}

.activity-icon-wrapper.image {
  background: linear-gradient(135deg, rgba(236, 72, 153, 0.12), rgba(244, 114, 182, 0.08));
  color: #ec4899;
}

.activity-icon-wrapper.video {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(52, 211, 153, 0.08));
  color: #10b981;
}

.activity-icon-wrapper.audio {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.12), rgba(251, 191, 36, 0.08));
  color: #f59e0b;
}

.activity-icon-wrapper svg {
  width: 20px;
  height: 20px;
  stroke-width: 2.2px;
}

.activity-content {
  flex: 1;
}

.activity-title {
  font-weight: 600;
  color: #1e293b;
  margin: 0 0 4px 0;
}

.activity-time {
  font-size: 12px;
  color: #94a3b8;
  margin: 0;
}

.activity-status {
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 700;
}

.activity-status.success {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(52, 211, 153, 0.08));
  color: #10b981;
}

.activity-status.pending {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.12), rgba(251, 191, 36, 0.08));
  color: #f59e0b;
}

@media (max-width: 1024px) {
  .sidebar {
    width: 100%;
    position: fixed;
    z-index: 100;
    height: 100%;
    transform: translateX(-100%);
    transition: transform 0.35s ease;
  }
  
  .sidebar.open {
    transform: translateX(0);
  }
}

@media (max-width: 640px) {
  .main-content {
    padding: 16px;
  }
  
  .header {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
  }
  
  .modules-grid {
    grid-template-columns: 1fr;
  }
  
  .stats-section {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .section-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }
}

.page-container {
  animation: fadeIn 0.3s;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.page-header {
  margin-bottom: 24px;
}

.page-title {
  font-size: 26px;
  font-weight: 800;
  color: #1e293b;
  margin: 0 0 8px 0;
}

.page-desc {
  color: #64748b;
  font-size: 14px;
  margin: 0;
}

.task-filters {
  display: flex;
  gap: 10px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 10px 20px;
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  background: white;
  font-size: 14px;
  font-weight: 600;
  color: #64748b;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  gap: 8px;
}

.filter-btn:hover {
  border-color: #3b82f6;
  color: #3b82f6;
}

.filter-btn.active {
  border-color: #3b82f6;
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
}

.filter-count {
  background: rgba(148, 163, 184, 0.12);
  padding: 2px 10px;
  border-radius: 10px;
  font-size: 12px;
}

.filter-btn.active .filter-count {
  background: rgba(59, 130, 246, 0.2);
}

.task-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.task-card {
  background: white;
  border-radius: 16px;
  padding: 20px;
  display: flex;
  align-items: center;
  gap: 16px;
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.04);
  border: 1px solid rgba(99, 102, 241, 0.06);
  cursor: pointer;
  transition: all 0.3s ease;
}

.task-card:hover {
  transform: translateX(4px);
  box-shadow: 0 8px 30px rgba(99, 102, 241, 0.1);
  border-color: rgba(59, 130, 246, 0.2);
}

.task-status {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.task-status.pending {
  background: #f59e0b;
}

.task-status.in-progress {
  background: #3b82f6;
}

.task-status.completed {
  background: #10b981;
}

.task-content {
  flex: 1;
}

.task-title {
  font-size: 16px;
  font-weight: 700;
  color: #1e293b;
  margin: 0 0 6px 0;
}

.task-desc {
  font-size: 14px;
  color: #64748b;
  margin: 0 0 10px 0;
}

.task-meta {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.task-tag {
  padding: 4px 12px;
  background: rgba(59, 130, 246, 0.08);
  color: #3b82f6;
  border-radius: 8px;
  font-size: 12px;
  font-weight: 500;
}

.task-deadline {
  font-size: 12px;
  color: #94a3b8;
}

.task-actions {
  display: flex;
  gap: 10px;
}

.task-actions .action-btn {
  padding: 10px 20px;
  border: none;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.task-actions .action-btn.primary {
  background: linear-gradient(135deg, #3b82f6, #6366f1);
  color: white;
}

.task-actions .action-btn:hover {
  transform: translateY(-2px);
}

.task-arrow {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #94a3b8;
  transition: all 0.3s ease;
}

.task-card:hover .task-arrow {
  color: #3b82f6;
  transform: translateX(4px);
}

.task-arrow svg {
  width: 18px;
  height: 18px;
}

.empty-tasks {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  text-align: center;
}

.empty-tasks svg {
  width: 64px;
  height: 64px;
  color: #cbd5e1;
  margin-bottom: 16px;
}

.empty-tasks p {
  font-size: 18px;
  font-weight: 600;
  color: #64748b;
  margin: 0 0 8px 0;
}

.empty-tasks span {
  font-size: 14px;
  color: #94a3b8;
}

.history-tabs {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}

.history-tab {
  padding: 10px 20px;
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  background: white;
  font-size: 14px;
  font-weight: 600;
  color: #64748b;
  cursor: pointer;
  transition: all 0.3s;
}

.history-tab:hover {
  border-color: #ec4899;
  color: #ec4899;
}

.history-tab.active {
  border-color: #ec4899;
  background: rgba(236, 72, 153, 0.1);
  color: #ec4899;
}

.history-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 16px;
}

.history-card {
  background: white;
  border-radius: 16px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.04);
  border: 1px solid rgba(99, 102, 241, 0.06);
}

.history-thumbnail {
  width: 100%;
  height: 120px;
  border-radius: 12px;
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.08), rgba(99, 102, 241, 0.04));
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3b82f6;
}

.history-thumbnail svg {
  width: 40px;
  height: 40px;
}

.history-info {
  flex: 1;
}

.history-title {
  font-size: 15px;
  font-weight: 700;
  color: #1e293b;
  margin: 0 0 4px 0;
}

.history-time {
  font-size: 12px;
  color: #94a3b8;
  margin: 0;
}

.history-actions .action-btn {
  width: 100%;
  padding: 10px;
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  background: white;
  font-size: 14px;
  font-weight: 600;
  color: #64748b;
  cursor: pointer;
  transition: all 0.3s;
}

.history-actions .action-btn:hover {
  border-color: #3b82f6;
  color: #3b82f6;
}

.resource-categories {
  display: flex;
  gap: 10px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}

.category-btn {
  padding: 12px 20px;
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  background: white;
  font-size: 14px;
  font-weight: 600;
  color: #64748b;
  cursor: pointer;
  transition: all 0.3s;
}

.category-btn:hover {
  border-color: #10b981;
  color: #10b981;
}

.category-btn.active {
  border-color: #10b981;
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.resource-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.resource-card {
  background: white;
  border-radius: 16px;
  padding: 20px;
  display: flex;
  gap: 16px;
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.04);
  border: 1px solid rgba(99, 102, 241, 0.06);
}

.resource-icon {
  width: 56px;
  height: 56px;
  border-radius: 14px;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(52, 211, 153, 0.08));
  display: flex;
  align-items: center;
  justify-content: center;
  color: #10b981;
  flex-shrink: 0;
}

.resource-icon svg {
  width: 26px;
  height: 26px;
}

.resource-content {
  flex: 1;
}

.resource-title {
  font-size: 16px;
  font-weight: 700;
  color: #1e293b;
  margin: 0 0 6px 0;
}

.resource-desc {
  font-size: 14px;
  color: #64748b;
  margin: 0 0 10px 0;
}

.resource-meta {
  display: flex;
  gap: 12px;
}

.resource-type {
  padding: 4px 12px;
  background: rgba(16, 185, 129, 0.08);
  color: #10b981;
  border-radius: 8px;
  font-size: 12px;
  font-weight: 500;
}

.resource-duration {
  font-size: 12px;
  color: #94a3b8;
}

.resource-progress {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: center;
  gap: 6px;
}

.resource-progress .progress-bar {
  width: 80px;
  height: 8px;
  background: rgba(148, 163, 184, 0.12);
  border-radius: 4px;
  overflow: hidden;
}

.resource-progress .progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #10b981, #34d399);
  border-radius: 4px;
  transition: width 0.6s ease;
}

.resource-progress .progress-text {
  font-size: 13px;
  font-weight: 700;
  color: #10b981;
}

.empty-history {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  text-align: center;
}

.empty-history svg {
  width: 64px;
  height: 64px;
  color: #cbd5e1;
  margin-bottom: 16px;
}

.empty-history p {
  font-size: 18px;
  font-weight: 600;
  color: #64748b;
  margin: 0 0 8px 0;
}

.empty-history span {
  font-size: 14px;
  color: #94a3b8;
}

.history-thumbnail {
  width: 100%;
  height: 120px;
  border-radius: 12px;
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.08), rgba(99, 102, 241, 0.04));
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3b82f6;
  background-size: cover;
  background-position: center;
  position: relative;
}

.history-thumbnail::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0,0,0,0.3);
  border-radius: 12px;
  opacity: 0;
  transition: opacity 0.3s;
}

.history-thumbnail:hover::before {
  opacity: 1;
}

.history-thumbnail svg {
  width: 40px;
  height: 40px;
  position: relative;
  z-index: 1;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  animation: fadeIn 0.3s ease;
}

.modal-content {
  background: white;
  border-radius: 20px;
  width: 90%;
  max-width: 700px;
  max-height: 80vh;
  display: flex;
  flex-direction: column;
  box-shadow: 0 25px 50px rgba(99, 102, 241, 0.25);
  animation: slideUp 0.3s ease;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 24px;
  border-bottom: 1px solid #e2e8f0;
}

.modal-title {
  font-size: 20px;
  font-weight: 700;
  color: #1e293b;
}

.modal-close {
  width: 36px;
  height: 36px;
  border: none;
  background: rgba(148, 163, 184, 0.08);
  border-radius: 10px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #64748b;
  transition: all 0.3s ease;
}

.modal-close:hover {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
}

.modal-body {
  padding: 24px;
  overflow-y: auto;
  flex: 1;
}

.resource-detail {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.detail-meta {
  display: flex;
  gap: 12px;
}

.detail-type {
  padding: 6px 14px;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(52, 211, 153, 0.08));
  color: #10b981;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 600;
}

.detail-duration {
  padding: 6px 14px;
  background: rgba(148, 163, 184, 0.1);
  color: #64748b;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 500;
}

.detail-description {
  font-size: 15px;
  color: #64748b;
  line-height: 1.6;
}

.detail-content {
  background: #f8fafc;
  border-radius: 14px;
  padding: 20px;
  line-height: 1.8;
}

.detail-content h1 {
  font-size: 22px;
  font-weight: 700;
  color: #1e293b;
  margin: 0 0 16px 0;
}

.detail-content h2 {
  font-size: 18px;
  font-weight: 700;
  color: #1e293b;
  margin: 20px 0 12px 0;
  padding-bottom: 8px;
  border-bottom: 2px solid #e2e8f0;
}

.detail-content h3 {
  font-size: 16px;
  font-weight: 600;
  color: #334155;
  margin: 16px 0 8px 0;
}

.detail-content p {
  color: #475569;
  margin: 8px 0;
}

.detail-content strong {
  font-weight: 700;
  color: #1e293b;
}

.detail-content li {
  margin-left: 20px;
  margin-bottom: 6px;
  color: #475569;
}

.modal-footer {
  padding: 16px 24px;
  border-top: 1px solid #e2e8f0;
  display: flex;
  justify-content: flex-end;
}

.modal-button {
  padding: 12px 32px;
  background: linear-gradient(135deg, #3b82f6, #6366f1);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.modal-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(59, 130, 246, 0.3);
}

.resource-card {
  cursor: pointer;
  transition: all 0.3s ease;
}

.resource-card:hover {
  transform: translateX(4px);
  box-shadow: 0 8px 30px rgba(99, 102, 241, 0.1);
  border-color: rgba(16, 185, 129, 0.2);
}

.empty-activities {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  text-align: center;
  color: #94a3b8;
}

.empty-activities svg {
  width: 48px;
  height: 48px;
  margin-bottom: 16px;
  opacity: 0.5;
}

.back-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.08), rgba(99, 102, 241, 0.06));
  border: 1px solid rgba(59, 130, 246, 0.15);
  border-radius: 14px;
  color: #3b82f6;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 2px 8px rgba(59, 130, 246, 0.08);
}

.back-btn:hover {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.16), rgba(99, 102, 241, 0.12));
  border-color: rgba(59, 130, 246, 0.3);
  transform: translateX(-4px);
  box-shadow: 0 4px 16px rgba(59, 130, 246, 0.15);
}

.back-btn svg {
  width: 18px;
  height: 18px;
  stroke-width: 2.2px;
  transition: transform 0.3s ease;
}

.back-btn:hover svg {
  transform: translateX(-3px);
}

.empty-activities p {
  font-size: 16px;
  font-weight: 600;
  color: #64748b;
  margin: 0 0 8px 0;
}

.empty-activities span {
  font-size: 14px;
  color: #94a3b8;
}
</style>