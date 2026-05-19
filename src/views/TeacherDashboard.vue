<template>
  <div class="dashboard-container">
    <div class="background-layer">
      <div class="floating-element element-1"></div>
      <div class="floating-element element-2"></div>
      <div class="floating-element element-3"></div>
      <div class="floating-element element-4"></div>
    </div>
    
    <aside class="sidebar">
      <div class="sidebar-header">
        <div class="logo-wrapper">
          <svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#3b82f6"/>
                <stop offset="50%" stop-color="#6366f1"/>
                <stop offset="100%" stop-color="#8b5cf6"/>
              </linearGradient>
            </defs>
            <rect x="6" y="6" width="36" height="36" rx="12" fill="url(#logoGrad)"/>
            <rect x="14" y="14" width="20" height="20" rx="6" fill="white"/>
            <path d="M24 18L20 26H28L24 18Z" fill="url(#logoGrad)"/>
          </svg>
        </div>
        <div class="logo-text-container">
          <span class="logo-title">AIGC实训</span>
          <span class="logo-subtitle">教师平台</span>
        </div>
      </div>
      
      <nav class="sidebar-nav">
        <div class="nav-section">
          <div class="nav-item" :class="{ active: activeMenu === 'dashboard' }" @click="activeMenu = 'dashboard'">
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="3" width="7" height="7" rx="1"/>
              <rect x="14" y="3" width="7" height="7" rx="1"/>
              <rect x="14" y="14" width="7" height="7" rx="1"/>
              <rect x="3" y="14" width="7" height="7" rx="1"/>
            </svg>
            <span class="nav-label">数据概览</span>
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
          
          <div class="nav-item" :class="{ active: activeMenu === 'students' }" @click="activeMenu = 'students'">
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
              <circle cx="9" cy="7" r="4"/>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
            </svg>
            <span class="nav-label">学生管理</span>
            <div class="nav-indicator"></div>
          </div>
        </div>
        
        <div class="nav-section-divider"></div>
        
        <div class="nav-section">
          <div class="nav-item" :class="{ active: activeMenu === 'resources' }" @click="activeMenu = 'resources'">
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
              <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
            </svg>
            <span class="nav-label">教学资源</span>
            <div class="nav-indicator"></div>
          </div>
          
          <div class="nav-item" :class="{ active: activeMenu === 'settings' }" @click="activeMenu = 'settings'">
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="3"/>
              <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06 2 3.46a1 1 0 0 1-.24 1.22l-.12.14c-.37.38-.93.38-1.31.02l-2.12-1.24a1.8 1.8 0 0 0-2.22.23l-.09-.07a1.72 1.72 0 0 0-1.88 0l-.09.07a1.8 1.8 0 0 0-2.22-.23l-2.12 1.24a1 1 0 0 1-1.31-.02l-.12-.14a1 1 0 0 1-.24-1.22l.06-.06a1.65 1.65 0 0 0 .33-1.82l-.03-.06a1.7 1.7 0 0 0 0-1.94l-.06-.07-2-3.46a1 1 0 0 1 .24-1.22l.12-.14c.37-.38.93-.38 1.31-.02l2.12 1.24a1.8 1.8 0 0 0 2.22-.23l.09.07a1.72 1.72 0 0 0 1.88 0l.09-.07a1.8 1.8 0 0 0 2.22.23l2.12-1.24a1 1 0 0 1 1.31.02l.12.14a1 1 0 0 1 .24 1.22l-.06.06a1.65 1.65 0 0 0-.33 1.82l.03.06a1.7 1.7 0 0 0 0 1.94z"/>
            </svg>
            <span class="nav-label">系统设置</span>
            <div class="nav-indicator"></div>
          </div>
        </div>
      </nav>
      
      <div class="sidebar-footer">
        <div class="user-card">
          <div class="user-avatar">
            <svg class="avatar-svg" width="56" height="56" viewBox="0 0 56 56" fill="none">
              <defs>
                <linearGradient id="avatarGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#6366f1"/>
                  <stop offset="100%" stop-color="#ec4899"/>
                </linearGradient>
              </defs>
              <circle cx="28" cy="28" r="26" fill="url(#avatarGrad)"/>
              <circle cx="28" cy="22" r="8" fill="white" opacity="0.9"/>
              <ellipse cx="28" cy="38" rx="12" ry="8" fill="white" opacity="0.9"/>
            </svg>
            <div class="avatar-badge">
              <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="4 8 7 11 12 5"></polyline>
              </svg>
            </div>
          </div>
          <div class="user-info">
            <span class="user-name">{{ currentUser }}</span>
            <span class="user-role">高级讲师</span>
          </div>
          <button class="menu-dots">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="5" r="1"></circle>
              <circle cx="12" cy="12" r="1"></circle>
              <circle cx="12" cy="19" r="1"></circle>
            </svg>
          </button>
        </div>
        
        <button class="logout-btn" @click="handleLogout">
          <svg class="logout-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
            <polyline points="16 17 21 12 16 7"></polyline>
            <line x1="21" y1="12" x2="9" y2="12"></line>
          </svg>
          <span>退出登录</span>
        </button>
      </div>
    </aside>

    <main class="main-content">
      <header class="header">
        <div class="header-left">
          <div class="greeting-card">
            <div class="greeting-icon-container">
              <svg class="greeting-svg" viewBox="0 0 64 64" fill="none">
                <defs>
                  <linearGradient id="greetGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#fbbf24"/>
                    <stop offset="100%" stop-color="#f59e0b"/>
                  </linearGradient>
                </defs>
                <circle cx="32" cy="32" r="28" fill="url(#greetGrad)" opacity="0.15"/>
                <circle cx="32" cy="32" r="20" fill="url(#greetGrad)" opacity="0.25"/>
                <path d="M32 16 C40 16 48 24 48 32 C48 40 40 48 32 48 C24 48 16 40 16 32 C16 24 24 16 32 16 Z" fill="url(#greetGrad)" opacity="0.8"/>
                <circle cx="26" cy="28" r="3" fill="white"/>
                <circle cx="38" cy="28" r="3" fill="white"/>
                <path d="M24 38 Q32 44 40 38" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round"/>
              </svg>
            </div>
            <div class="greeting-text">
              <h1 class="page-title">下午好，{{ currentUser }} 🌤️</h1>
              <p class="page-desc">今天有 32 份作业等待您的批改，让我们开始吧！</p>
            </div>
          </div>
        </div>
        
        <div class="header-right">
          <div class="action-buttons">
            <button class="header-btn icon-btn notification-btn" @click="showNotification">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
              </svg>
              <span class="notification-badge">5</span>
            </button>
            
            <button class="header-btn icon-btn search-btn">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="11" cy="11" r="8"></circle>
                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
              </svg>
            </button>
            
            <div class="header-date-picker">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="16" y1="2" x2="16" y2="6"></line>
                <line x1="8" y1="2" x2="8" y2="6"></line>
                <line x1="3" y1="10" x2="21" y2="10"></line>
              </svg>
              <span class="date-text">2024年1月15日</span>
            </div>
            
            <button class="header-btn primary-btn export-btn" @click="exportReport">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                <polyline points="17 10 12 15 7 10"></polyline>
              </svg>
              <span>导出报表</span>
            </button>
          </div>
        </div>
      </header>

      <template v-if="activeMenu === 'dashboard'">
        <div class="stats-grid">
        <div class="stat-card primary" @click="onStatClick('total')">
          <div class="stat-decoration"></div>
          <div class="stat-content">
            <div class="stat-icon-wrapper">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="3" width="7" height="7" rx="1"></rect>
                <rect x="14" y="3" width="7" height="7" rx="1"></rect>
                <rect x="14" y="14" width="7" height="7" rx="1"></rect>
                <rect x="3" y="14" width="7" height="7" rx="1"></rect>
              </svg>
            </div>
            <div class="stat-info">
              <span class="stat-value animate-number" :data-value="128">128</span>
              <span class="stat-label">总实训任务</span>
            </div>
          </div>
          <div class="stat-trend positive">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline>
              <polyline points="17 6 23 6 23 12"></polyline>
            </svg>
            <span>↑ 12%</span>
          </div>
        </div>

        <div class="stat-card success" @click="onStatClick('completed')">
          <div class="stat-decoration"></div>
          <div class="stat-content">
            <div class="stat-icon-wrapper">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                <polyline points="22 4 12 14.01 9 11.01"></polyline>
              </svg>
            </div>
            <div class="stat-info">
              <span class="stat-value animate-number" :data-value="96">96</span>
              <span class="stat-label">已完成任务</span>
            </div>
          </div>
          <div class="stat-trend positive">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline>
              <polyline points="17 6 23 6 23 12"></polyline>
            </svg>
            <span>↑ 8%</span>
          </div>
        </div>

        <div class="stat-card warning" @click="onStatClick('students')">
          <div class="stat-decoration"></div>
          <div class="stat-content">
            <div class="stat-icon-wrapper">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
              </svg>
            </div>
            <div class="stat-info">
              <span class="stat-value animate-number" :data-value="45">45</span>
              <span class="stat-label">班级学生</span>
            </div>
          </div>
          <div class="stat-trend neutral">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="5" y1="12" x2="19" y2="12"></line>
            </svg>
            <span>稳定</span>
          </div>
        </div>

        <div class="stat-card danger" @click="onStatClick('pending')">
          <div class="stat-decoration"></div>
          <div class="stat-content">
            <div class="stat-icon-wrapper">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <polyline points="12 6 12 12 16 14"></polyline>
              </svg>
            </div>
            <div class="stat-info">
              <span class="stat-value animate-number" :data-value="32">32</span>
              <span class="stat-label">待批改任务</span>
            </div>
          </div>
          <div class="stat-trend negative">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="1 6 9.5 15.5 14.5 10.5 22 18"></polyline>
              <polyline points="7 18 1 18 1 12"></polyline>
            </svg>
            <span>↓ 5%</span>
          </div>
        </div>
      </div>

      <div class="charts-section">
        <div class="chart-card line-chart-card">
          <div class="card-header">
            <div class="card-title-section">
              <div class="card-icon-wrapper">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="18" y1="20" x2="18" y2="10"></line>
                  <line x1="12" y1="20" x2="12" y2="4"></line>
                  <line x1="6" y1="20" x2="6" y2="14"></line>
                </svg>
              </div>
              <div class="card-title-text">
                <h3>实训完成趋势</h3>
                <div class="card-subtitle">近7天学生完成情况</div>
              </div>
            </div>
            <div class="chart-controls">
              <div class="period-selector">
                <button class="period-btn active">本周</button>
                <button class="period-btn">本月</button>
                <button class="period-btn">本季度</button>
              </div>
            </div>
          </div>
          <div class="chart-container">
            <svg viewBox="0 0 520 280" class="line-chart">
              <defs>
                <linearGradient id="chartGrad1" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%" stop-color="#6366f1" stop-opacity="0.3"/>
                  <stop offset="100%" stop-color="#6366f1" stop-opacity="0"/>
                </linearGradient>
                <linearGradient id="chartGrad2" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%" stop-color="#10b981" stop-opacity="0.3"/>
                  <stop offset="100%" stop-color="#10b981" stop-opacity="0"/>
                </linearGradient>
                <linearGradient id="lineGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#6366f1"/>
                  <stop offset="100%" stop-color="#8b5cf6"/>
                </linearGradient>
                <linearGradient id="lineGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#10b981"/>
                  <stop offset="100%" stop-color="#34d399"/>
                </linearGradient>
                <filter id="glowSoft">
                  <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
                  <feMerge>
                    <feMergeNode in="coloredBlur"/>
                    <feMergeNode in="SourceGraphic"/>
                  </feMerge>
                </filter>
              </defs>
              
              <g class="grid-lines">
                <line x1="40" y1="40" x2="480" y2="40" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="5,5"/>
                <line x1="40" y1="85" x2="480" y2="85" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="5,5"/>
                <line x1="40" y1="130" x2="480" y2="130" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="5,5"/>
                <line x1="40" y1="175" x2="480" y2="175" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="5,5"/>
                <line x1="40" y1="220" x2="480" y2="220" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="5,5"/>
              </g>
              
              <path d="M40 180 L100 160 L160 140 L220 170 L280 120 L340 150 L400 100 L480 130" fill="none" stroke="url(#lineGrad1)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" filter="url(#glowSoft)"/>
              <path d="M40 180 L100 160 L160 140 L220 170 L280 120 L340 150 L400 100 L480 130 L480 220 L40 220 Z" fill="url(#chartGrad1)"/>
              
              <path d="M40 200 L100 190 L160 180 L220 195 L280 160 L340 175 L400 145 L480 165" fill="none" stroke="url(#lineGrad2)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" filter="url(#glowSoft)"/>
              <path d="M40 200 L100 190 L160 180 L220 195 L280 160 L340 175 L400 145 L480 165 L480 220 L40 220 Z" fill="url(#chartGrad2)"/>
              
              <g class="data-points">
                <circle cx="40" cy="180" r="6" fill="white" stroke="url(#lineGrad1)" stroke-width="3"/>
                <circle cx="100" cy="160" r="6" fill="white" stroke="url(#lineGrad1)" stroke-width="3"/>
                <circle cx="160" cy="140" r="6" fill="white" stroke="url(#lineGrad1)" stroke-width="3"/>
                <circle cx="220" cy="170" r="6" fill="white" stroke="url(#lineGrad1)" stroke-width="3"/>
                <circle cx="280" cy="120" r="6" fill="white" stroke="url(#lineGrad1)" stroke-width="3"/>
                <circle cx="340" cy="150" r="6" fill="white" stroke="url(#lineGrad1)" stroke-width="3"/>
                <circle cx="400" cy="100" r="6" fill="white" stroke="url(#lineGrad1)" stroke-width="3"/>
                <circle cx="480" cy="130" r="6" fill="white" stroke="url(#lineGrad1)" stroke-width="3"/>
              </g>
              
              <g class="axis-labels">
                <text x="40" y="250" fill="#64748b" font-size="12" font-weight="600">周一</text>
                <text x="100" y="250" fill="#64748b" font-size="12" font-weight="600">周二</text>
                <text x="160" y="250" fill="#64748b" font-size="12" font-weight="600">周三</text>
                <text x="220" y="250" fill="#64748b" font-size="12" font-weight="600">周四</text>
                <text x="280" y="250" fill="#64748b" font-size="12" font-weight="600">周五</text>
                <text x="340" y="250" fill="#64748b" font-size="12" font-weight="600">周六</text>
                <text x="400" y="250" fill="#64748b" font-size="12" font-weight="600">周日</text>
              </g>
            </svg>
          </div>
          <div class="chart-legend">
            <div class="legend-item">
              <div class="legend-dot" style="background: linear-gradient(135deg, #6366f1, #8b5cf6);"></div>
              <span class="legend-text">完成任务</span>
            </div>
            <div class="legend-item">
              <div class="legend-dot" style="background: linear-gradient(135deg, #10b981, #34d399);"></div>
              <span class="legend-text">提交作业</span>
            </div>
          </div>
        </div>

        <div class="chart-card pie-chart-card">
          <div class="card-header">
            <div class="card-title-section">
              <div class="card-icon-wrapper success">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"></circle>
                  <path d="M12 16v-4"></path>
                  <path d="M12 8h.01"></path>
                </svg>
              </div>
              <div class="card-title-text">
                <h3>模块使用分布</h3>
                <div class="card-subtitle">各模块任务占比</div>
              </div>
            </div>
          </div>
          <div class="chart-container">
            <div class="pie-chart-wrapper">
              <svg viewBox="0 0 240 240" class="pie-chart">
                <defs>
                  <filter id="pieGlowSoft">
                    <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
                    <feMerge>
                      <feMergeNode in="coloredBlur"/>
                      <feMergeNode in="SourceGraphic"/>
                    </feMerge>
                  </filter>
                </defs>
                <circle cx="120" cy="120" r="85" fill="none" stroke="#f1f5f9" stroke-width="28"/>
                <circle cx="120" cy="120" r="85" fill="none" stroke="#6366f1" stroke-width="28" stroke-dasharray="267 534" stroke-dashoffset="0" transform="rotate(-90 120 120)" filter="url(#pieGlowSoft)"/>
                <circle cx="120" cy="120" r="85" fill="none" stroke="#ec4899" stroke-width="28" stroke-dasharray="160 534" stroke-dashoffset="-267" transform="rotate(-90 120 120)" filter="url(#pieGlowSoft)"/>
                <circle cx="120" cy="120" r="85" fill="none" stroke="#10b981" stroke-width="28" stroke-dasharray="80 534" stroke-dashoffset="-427" transform="rotate(-90 120 120)" filter="url(#pieGlowSoft)"/>
                <circle cx="120" cy="120" r="85" fill="none" stroke="#f59e0b" stroke-width="28" stroke-dasharray="27 534" stroke-dashoffset="-507" transform="rotate(-90 120 120)" filter="url(#pieGlowSoft)"/>
                <circle cx="120" cy="120" r="58" fill="white"/>
                <circle cx="120" cy="120" r="52" fill="url(#chartGrad1)" opacity="0.08"/>
                <text x="120" y="105" fill="#1e293b" font-size="32" font-weight="800" text-anchor="middle">128</text>
                <text x="120" y="135" fill="#64748b" font-size="14" font-weight="600" text-anchor="middle">总任务</text>
              </svg>
            </div>
            <div class="pie-legend">
              <div class="legend-item">
                <div class="legend-color" style="background: linear-gradient(135deg, #6366f1, #8b5cf6);"></div>
                <span class="legend-label">生文本</span>
                <span class="legend-value">50%</span>
              </div>
              <div class="legend-item">
                <div class="legend-color" style="background: linear-gradient(135deg, #ec4899, #f472b6);"></div>
                <span class="legend-label">生图片</span>
                <span class="legend-value">30%</span>
              </div>
              <div class="legend-item">
                <div class="legend-color" style="background: linear-gradient(135deg, #10b981, #34d399);"></div>
                <span class="legend-label">生视频</span>
                <span class="legend-value">15%</span>
              </div>
              <div class="legend-item">
                <div class="legend-color" style="background: linear-gradient(135deg, #f59e0b, #fbbf24);"></div>
                <span class="legend-label">生音频</span>
                <span class="legend-value">5%</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="tasks-section">
        <div class="section-header">
          <div class="section-title-wrapper">
            <div class="section-icon-wrapper">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
                <polyline points="10 9 9 9 8 9"></polyline>
              </svg>
            </div>
            <div class="section-title-text">
              <h2>待批改任务</h2>
              <span class="task-count">共 5 项任务</span>
            </div>
          </div>
          <button class="add-task-btn" @click="showAddTaskModal = true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="12" y1="5" x2="12" y2="19"></line>
              <line x1="5" y1="12" x2="19" y2="12"></line>
            </svg>
            <span>发布新任务</span>
          </button>
        </div>
        
        <div class="tasks-table">
          <div class="table-header">
            <div class="table-cell task-name-cell">任务名称</div>
            <div class="table-cell module-cell">所属模块</div>
            <div class="table-cell students-cell">提交人数</div>
            <div class="table-cell deadline-cell">截止日期</div>
            <div class="table-cell status-cell">状态</div>
            <div class="table-cell actions-cell">操作</div>
          </div>
          
          <div class="table-body">
            <div class="table-row" v-for="(task, index) in pendingTasks" :key="task.id">
              <div class="table-cell task-name-cell">
                <div class="task-info">
                  <div class="task-icon" :style="{background: getModuleColor(task.module)}">
                    <svg v-if="task.module === '生文本'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                      <polyline points="14 2 14 8 20 8"></polyline>
                      <line x1="16" y1="13" x2="8" y2="13"></line>
                      <line x1="16" y1="17" x2="8" y2="17"></line>
                    </svg>
                    <svg v-else-if="task.module === '生图片'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                      <circle cx="8.5" cy="8.5" r="1.5"></circle>
                      <polyline points="21 15 16 10 5 21"></polyline>
                    </svg>
                    <svg v-else-if="task.module === '生视频'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <polygon points="23 7 16 12 23 17 23 7"></polygon>
                      <rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect>
                    </svg>
                    <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                      <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>
                    </svg>
                  </div>
                  <span class="task-name">{{ task.name }}</span>
                </div>
              </div>
              <div class="table-cell module-cell">
                <span class="module-tag" :class="'module-' + getModuleTagType(task.module)">
                  {{ task.module }}
                </span>
              </div>
              <div class="table-cell students-cell">
                <div class="students-display">
                  <div class="mini-avatars">
                    <div class="mini-avatar" v-for="i in 3" :key="i"></div>
                  </div>
                  <span class="students-text">{{ task.students }} 人</span>
                </div>
              </div>
              <div class="table-cell deadline-cell">
                <div class="deadline-display">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                    <line x1="16" y1="2" x2="16" y2="6"></line>
                    <line x1="8" y1="2" x2="8" y2="6"></line>
                    <line x1="3" y1="10" x2="21" y2="10"></line>
                  </svg>
                  <span>{{ task.deadline }}</span>
                </div>
              </div>
              <div class="table-cell status-cell">
                <span class="status-badge" :class="'status-' + task.status">
                  {{ task.status === 'pending' ? '待批改' : '已完成' }}
                </span>
              </div>
              <div class="table-cell actions-cell">
                <button class="action-btn view-btn" @click="viewTask(task)">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M1 12s4-8 11-8 11 8-11 8-11-8z"></path>
                    <circle cx="12" cy="12" r="3"></circle>
                  </svg>
                  <span>查看</span>
                </button>
                <button class="action-btn grade-btn" @click="gradeTask(task)">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                    <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                  </svg>
                  <span>批改</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      </template>

      <template v-else-if="activeMenu === 'tasks'">
        <div class="page-container">
          <div class="page-header">
            <h2 class="page-title">实训任务</h2>
            <p class="page-desc">管理和发布实训任务</p>
          </div>
          <div class="task-list-container">
            <div class="task-table">
              <div class="table-header">
                <div class="table-cell">任务名称</div>
                <div class="table-cell">所属模块</div>
                <div class="table-cell">参与学生</div>
                <div class="table-cell">截止日期</div>
                <div class="table-cell">状态</div>
                <div class="table-cell">操作</div>
              </div>
              <div class="table-body">
                <div class="table-row" v-for="task in pendingTasks" :key="task.id">
                  <div class="table-cell">
                    <div class="task-name-display">
                      <div class="task-icon" :style="{background: getModuleColor(task.module)}">
                        <svg v-if="task.module === '生文本'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                          <polyline points="14 2 14 8 20 8"></polyline>
                        </svg>
                        <svg v-else-if="task.module === '生图片'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                          <circle cx="8.5" cy="8.5" r="1.5"></circle>
                        </svg>
                        <svg v-else-if="task.module === '生视频'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <polygon points="23 7 16 12 23 17 23 7"></polygon>
                          <rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect>
                        </svg>
                        <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                        </svg>
                      </div>
                      <span class="task-name">{{ task.name }}</span>
                    </div>
                  </div>
                  <div class="table-cell">
                    <span class="module-tag" :class="'module-' + getModuleTagType(task.module)">{{ task.module }}</span>
                  </div>
                  <div class="table-cell">{{ task.students }} 人</div>
                  <div class="table-cell">{{ task.deadline }}</div>
                  <div class="table-cell">
                    <span class="status-badge" :class="'status-' + task.status">{{ task.status === 'pending' ? '待批改' : '已完成' }}</span>
                  </div>
                  <div class="table-cell">
                    <button class="action-btn view-btn" @click="viewTask(task)">查看</button>
                    <button class="action-btn grade-btn" @click="gradeTask(task)">批改</button>
                  </div>
                </div>
              </div>
            </div>
            <button class="add-task-btn" @click="showAddTaskModal = true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="12" y1="5" x2="12" y2="19"></line>
                <line x1="5" y1="12" x2="19" y2="12"></line>
              </svg>
              <span>发布新任务</span>
            </button>
          </div>
        </div>
      </template>

      <template v-else-if="activeMenu === 'students'">
        <div class="page-container">
          <div class="page-header">
            <h2 class="page-title">学生管理</h2>
            <p class="page-desc">管理班级学生信息</p>
          </div>
          <div class="students-container">
            <div class="students-grid">
              <div class="student-card" v-for="i in 6" :key="i">
                <div class="student-avatar">
                  <svg viewBox="0 0 48 48" fill="none">
                    <defs>
                      <linearGradient :id="'grad-' + i" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" :stop-color="['#6366f1', '#ec4899', '#10b981', '#f59e0b', '#8b5cf6', '#3b82f6'][i-1]"/>
                        <stop offset="100%" :stop-color="['#8b5cf6', '#f472b6', '#34d399', '#fbbf24', '#a78bfa', '#60a5fa'][i-1]"/>
                      </linearGradient>
                    </defs>
                    <circle cx="24" cy="24" r="22" :fill="'url(#grad-' + i + ')'"/>
                    <circle cx="24" cy="18" r="7" fill="white" opacity="0.9"/>
                    <ellipse cx="24" cy="32" rx="10" ry="6" fill="white" opacity="0.9"/>
                  </svg>
                </div>
                <div class="student-info">
                  <span class="student-name">学生{{ i }}</span>
                  <span class="student-class">实训班{{ Math.ceil(i/2) }}组</span>
                </div>
                <div class="student-score">
                  <span class="score-label">综合评分</span>
                  <span class="score-value">{{ 75 + i * 4 }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </template>

      <template v-else-if="activeMenu === 'resources'">
        <div class="page-container">
          <div class="page-header">
            <h2 class="page-title">教学资源</h2>
            <p class="page-desc">管理教学资料和素材</p>
          </div>
          <div class="resources-container">
            <div class="resources-grid">
              <div class="resource-card" v-for="i in 4" :key="i">
                <div class="resource-icon" :style="{background: ['linear-gradient(135deg, #6366f1, #8b5cf6)', 'linear-gradient(135deg, #ec4899, #f472b6)', 'linear-gradient(135deg, #10b981, #34d399)', 'linear-gradient(135deg, #f59e0b, #fbbf24)'][i-1]}">
                  <svg v-if="i === 1" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                    <polyline points="14 2 14 8 20 8"></polyline>
                  </svg>
                  <svg v-else-if="i === 2" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                    <circle cx="8.5" cy="8.5" r="1.5"></circle>
                  </svg>
                  <svg v-else-if="i === 3" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                    <polygon points="23 7 16 12 23 17 23 7"></polygon>
                    <rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect>
                  </svg>
                  <svg v-else viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                    <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                  </svg>
                </div>
                <div class="resource-info">
                  <span class="resource-name">{{ ['文本创作指南', '图像生成教程', '视频剪辑技巧', '音频合成手册'][i-1] }}</span>
                  <span class="resource-desc">{{ ['详细的文本创作技巧和方法', '图像生成的基础知识', '视频剪辑的实用技巧', '音频合成的入门指南'][i-1] }}</span>
                </div>
                <button class="resource-action" @click="viewResource(i-1)">查看</button>
              </div>
            </div>
          </div>
        </div>
      </template>

      <template v-else-if="activeMenu === 'settings'">
        <div class="page-container">
          <div class="page-header">
            <h2 class="page-title">系统设置</h2>
            <p class="page-desc">配置平台参数和个人设置</p>
          </div>
          <div class="settings-container">
            <div class="settings-section">
              <h3 class="section-title">个人信息</h3>
              <div class="settings-form">
                <div class="form-row">
                  <div class="form-group">
                    <label>用户名</label>
                    <input type="text" class="form-input" :value="currentUser" readonly>
                  </div>
                  <div class="form-group">
                    <label>角色</label>
                    <input type="text" class="form-input" value="教师" readonly>
                  </div>
                </div>
              </div>
            </div>
            <div class="settings-section">
              <h3 class="section-title">平台设置</h3>
              <div class="settings-form">
                <div class="form-row">
                  <div class="form-group">
                    <label>主题模式</label>
                    <select class="form-select">
                      <option>亮色模式</option>
                      <option>暗色模式</option>
                      <option>跟随系统</option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label>语言</label>
                    <select class="form-select">
                      <option>简体中文</option>
                      <option>English</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </template>

      <div class="modal-overlay" v-if="showResourceModal" @click="showResourceModal = false">
        <div class="modal-content resource-modal" @click.stop>
          <div class="modal-header">
            <div class="modal-title-section">
              <div class="modal-icon" v-if="selectedResource" :style="{background: selectedResource.color}">
                <svg v-if="selectedResource.icon === 'text'" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                  <polyline points="14 2 14 8 20 8"></polyline>
                </svg>
                <svg v-else-if="selectedResource.icon === 'image'" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                  <circle cx="8.5" cy="8.5" r="1.5"></circle>
                </svg>
                <svg v-else-if="selectedResource.icon === 'video'" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                  <polygon points="23 7 16 12 23 17 23 7"></polygon>
                  <rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect>
                </svg>
                <svg v-else viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
                  <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                </svg>
              </div>
              <div class="modal-title-text">
                <h2>{{ selectedResource?.name }}</h2>
                <p>{{ selectedResource?.description }}</p>
              </div>
            </div>
            <button class="modal-close" @click="showResourceModal = false">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
            </button>
          </div>
          
          <div class="modal-body">
            <div class="resource-content" v-if="selectedResource">
              <div class="resource-content-inner" v-html="renderMarkdown(selectedResource.content)"></div>
            </div>
          </div>
          
          <div class="modal-footer">
            <button class="modal-btn cancel-btn" @click="showResourceModal = false">关闭</button>
          </div>
        </div>
      </div>

      <div class="modal-overlay" v-if="showAddTaskModal" @click="showAddTaskModal = false">
        <div class="modal-content" @click.stop>
          <div class="modal-header">
            <div class="modal-title-section">
              <div class="modal-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
                </svg>
              </div>
              <div class="modal-title-text">
                <h2>发布新任务</h2>
                <p>创建一个新的实训任务给学生</p>
              </div>
            </div>
            <button class="modal-close" @click="showAddTaskModal = false">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
            </button>
          </div>
          
          <div class="modal-body">
            <form class="task-form">
              <div class="form-group">
                <label class="form-label">任务名称</label>
                <input type="text" class="form-input" v-model="newTask.name" placeholder="请输入任务名称">
              </div>
              
              <div class="form-group">
                <label class="form-label">所属模块</label>
                <div class="module-selector">
                  <div class="module-option" v-for="module in ['生文本', '生图片', '生视频', '生音频']" :key="module" @click="newTask.module = module" :class="{active: newTask.module === module}">
                    <div class="module-option-icon" :style="{background: getModuleColor(module)}">
                      <svg v-if="module === '生文本'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                        <polyline points="14 2 14 8 20 8"></polyline>
                      </svg>
                      <svg v-else-if="module === '生图片'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                        <circle cx="8.5" cy="8.5" r="1.5"></circle>
                      </svg>
                      <svg v-else-if="module === '生视频'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <polygon points="23 7 16 12 23 17 23 7"></polygon>
                        <rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect>
                      </svg>
                      <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                      </svg>
                    </div>
                    <span>{{ module }}</span>
                  </div>
                </div>
              </div>
              
              <div class="form-group">
                <label class="form-label">任务描述</label>
                <textarea class="form-textarea" v-model="newTask.description" placeholder="请详细描述任务要求..."></textarea>
              </div>
              
              <div class="form-row">
                <div class="form-group">
                  <label class="form-label">截止日期</label>
                  <input type="date" class="form-input" v-model="newTask.deadline">
                </div>
                <div class="form-group">
                  <label class="form-label">评分标准</label>
                  <select class="form-select" v-model="newTask.criteria">
                    <option value="standard">标准评分</option>
                    <option value="detailed">详细评分</option>
                    <option value="simple">简单评分</option>
                  </select>
                </div>
              </div>
            </form>
          </div>
          
          <div class="modal-footer">
            <button class="modal-btn cancel-btn" @click="showAddTaskModal = false">取消</button>
            <button class="modal-btn confirm-btn" @click="addTask">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="12" y1="5" x2="12" y2="19"></line>
                <line x1="5" y1="12" x2="19" y2="12"></line>
              </svg>
              <span>发布任务</span>
            </button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const activeMenu = ref('dashboard')
const showAddTaskModal = ref(false)
const currentUser = ref(localStorage.getItem('currentUsername') || '李老师')

const newTask = reactive({
  name: '',
  module: '生文本',
  description: '',
  deadline: '',
  criteria: 'standard'
})

const pendingTasks = [
  { id: 1, name: '产品宣传文案创作', module: '生文本', students: 42, deadline: '2024-01-20', status: 'pending' },
  { id: 2, name: '校园海报设计', module: '生图片', students: 38, deadline: '2024-01-18', status: 'pending' },
  { id: 3, name: '视频剪辑实训', module: '生视频', students: 25, deadline: '2024-01-22', status: 'pending' },
  { id: 4, name: '旁白配音练习', module: '生音频', students: 40, deadline: '2024-01-19', status: 'pending' },
  { id: 5, name: '学术论文摘要', module: '生文本', students: 45, deadline: '2024-01-21', status: 'pending' },
]

const getModuleTagType = (module) => {
  const types = {
    '生文本': 'primary',
    '生图片': 'pink',
    '生视频': 'green',
    '生音频': 'yellow'
  }
  return types[module] || 'default'
}

const getModuleColor = (module) => {
  const colors = {
    '生文本': 'linear-gradient(135deg, #6366f1, #8b5cf6)',
    '生图片': 'linear-gradient(135deg, #ec4899, #f472b6)',
    '生视频': 'linear-gradient(135deg, #10b981, #34d399)',
    '生音频': 'linear-gradient(135deg, #f59e0b, #fbbf24)'
  }
  return colors[module] || 'linear-gradient(135deg, #6366f1, #8b5cf6)'
}

const resources = [
  {
    id: 1,
    name: '文本创作指南',
    icon: 'text',
    description: '详细的文本创作技巧和方法',
    color: 'linear-gradient(135deg, #6366f1, #8b5cf6)',
    content: `# 文本创作指南

## 一、创作基础

### 1.1 写作准备
- 明确写作目的和受众
- 收集相关资料和素材
- 制定写作大纲

### 1.2 结构规划
- 引言：吸引读者注意力
- 正文：详细阐述主题
- 结论：总结要点

## 二、写作技巧

### 2.1 语言表达
- 使用简洁明了的语言
- 避免冗长复杂的句子
- 保持段落短小精悍

### 2.2 内容组织
- 逻辑清晰，层次分明
- 重点突出，详略得当
- 过渡自然，衔接流畅

## 三、实战练习

尝试完成以下练习：
1. 写一篇200字的短文介绍你的专业
2. 撰写产品描述文案
3. 创作一篇故事开头

---
*持续练习，不断提升写作能力！*`
  },
  {
    id: 2,
    name: '图像生成教程',
    icon: 'image',
    description: '图像生成的基础知识',
    color: 'linear-gradient(135deg, #ec4899, #f472b6)',
    content: `# 图像生成教程

## 一、基础概念

### 1.1 图像生成技术
- 基于扩散模型的生成技术
- 提示词的重要性
- 常用参数设置

### 1.2 提示词技巧
- 主体描述要明确
- 添加风格和氛围描述
- 使用专业术语提升质量

## 二、实战指南

### 2.1 提示词结构
\`\`\`
主体 + 风格 + 细节 + 参数
\`\`\`

### 2.2 示例提示词
\`\`\`
beautiful landscape with mountains and lake, 
cinematic lighting, photorealistic, 8k, 
detailed, professional photography
\`\`\`

## 三、进阶技巧

- 尝试不同的模型风格
- 使用负提示词排除不想要的元素
- 调整分辨率和比例

---
*多实践，探索无限创意可能！*`
  },
  {
    id: 3,
    name: '视频剪辑技巧',
    icon: 'video',
    description: '视频剪辑的实用技巧',
    color: 'linear-gradient(135deg, #10b981, #34d399)',
    content: `# 视频剪辑技巧

## 一、剪辑基础

### 1.1 软件选择
- Premiere Pro：专业级剪辑工具
- After Effects：特效制作
- CapCut：移动端剪辑

### 1.2 基本操作
- 剪切与拼接
- 转场效果
- 音频处理

## 二、节奏把控

### 2.1 镜头时长
- 根据内容调整节奏
- 保持观众注意力
- 避免冗长镜头

### 2.2 音乐配合
- 选择合适的背景音乐
- 卡点剪辑增强节奏感
- 音量平衡调节

## 三、调色技巧

- 统一画面风格
- 调整对比度和饱和度
- 添加滤镜增强氛围

---
*剪辑让故事更精彩！*`
  },
  {
    id: 4,
    name: '音频合成手册',
    icon: 'audio',
    description: '音频合成的入门指南',
    color: 'linear-gradient(135deg, #f59e0b, #fbbf24)',
    content: `# 音频合成手册

## 一、语音合成基础

### 1.1 TTS技术
- 文字转语音原理
- 不同音色选择
- 语速和语调调节

### 1.2 参数设置
- 选择合适的声音类型
- 调整语速适应场景
- 添加背景音乐

## 二、实践应用

### 2.1 场景选择
- 旁白配音：清晰正式
- 角色对话：生动自然
- 广告宣传：活力充沛

### 2.2 后期处理
- 添加背景音乐
- 调整音量平衡
- 降噪处理

## 三、高级技巧

- 多角色对话合成
- 情感语气调整
- 音频格式转换

---
*让声音为内容增色！*`
  }
]

const showResourceModal = ref(false)
const selectedResource = ref(null)

const onStatClick = (type) => {
  switch(type) {
    case 'total':
    case 'completed':
    case 'pending':
      activeMenu.value = 'tasks'
      break
    case 'students':
      activeMenu.value = 'students'
      break
    default:
      break
  }
}

const showNotification = () => {
  console.log('Notification clicked')
}

const exportReport = () => {
  console.log('Export report')
}

const viewTask = (task) => {
  console.log('View task:', task)
}

const gradeTask = (task) => {
  console.log('Grade task:', task)
}

const addTask = () => {
  console.log('Add task:', newTask)
  showAddTaskModal.value = false
}

const viewResource = (index) => {
  selectedResource.value = resources[index]
  showResourceModal.value = true
}

const renderMarkdown = (content) => {
  let html = content
    .replace(/^### (.*$)/gim, '<h3>$1</h3>')
    .replace(/^## (.*$)/gim, '<h2>$1</h2>')
    .replace(/^# (.*$)/gim, '<h1>$1</h1>')
    .replace(/\*\*(.*)\*\*/gim, '<strong>$1</strong>')
    .replace(/\*(.*)\*/gim, '<em>$1</em>')
    .replace(/`([^`]+)`/gim, '<code>$1</code>')
    .replace(/```[\s\S]*?```/gim, (match) => {
      const code = match.replace(/```/g, '')
      return `<pre><code>${code}</code></pre>`
    })
    .replace(/^- (.*$)/gim, '<li>$1</li>')
    .replace(/^(\d+)\. (.*$)/gim, '<li>$1. $2</li>')
    .replace(/(<li>[\s\S]*?<\/li>)/gim, '<ul>$1</ul>')
    .replace(/\n/gim, '<br>')
  return html
}

const handleLogout = () => {
  localStorage.removeItem('currentRole')
  router.push('/')
}
</script>

<style scoped>
.dashboard-container {
  display: flex;
  height: 100vh;
  background: #f8fafc;
  position: relative;
  overflow: hidden;
}

.background-layer {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  overflow: hidden;
  z-index: 0;
  pointer-events: none;
}

.floating-element {
  position: absolute;
  border-radius: 50%;
  opacity: 0.05;
  animation: float 15s infinite ease-in-out;
}

.element-1 {
  width: 400px;
  height: 400px;
  background: linear-gradient(135deg, #3b82f6, #6366f1);
  top: -150px;
  right: -100px;
  animation-delay: 0s;
}

.element-2 {
  width: 280px;
  height: 280px;
  background: linear-gradient(135deg, #8b5cf6, #ec4899);
  bottom: -80px;
  left: -60px;
  animation-delay: -5s;
}

.element-3 {
  width: 180px;
  height: 180px;
  background: linear-gradient(135deg, #ec4899, #f472b6);
  top: 40%;
  right: 30%;
  animation-delay: -10s;
}

.element-4 {
  width: 220px;
  height: 220px;
  background: linear-gradient(135deg, #06b6d4, #10b981);
  bottom: 20%;
  right: 15%;
  animation-delay: -7s;
}

@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg) scale(1); }
  33% { transform: translateY(-30px) rotate(120deg) scale(1.05); }
  66% { transform: translateY(-15px) rotate(240deg) scale(0.95); }
}

.sidebar {
  width: 290px;
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(30px);
  display: flex;
  flex-direction: column;
  box-shadow: 6px 0 40px rgba(99, 102, 241, 0.08);
  z-index: 1;
  border-right: 1px solid rgba(99, 102, 241, 0.06);
}

.sidebar-header {
  padding: 28px 24px;
  display: flex;
  align-items: center;
  gap: 14px;
  border-bottom: 1px solid rgba(226, 232, 240, 0.6);
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.03), rgba(236, 72, 153, 0.03));
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
  padding: 20px 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.nav-section {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.nav-section-divider {
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(226, 232, 240, 0.8), transparent);
  margin: 12px 8px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 16px;
  border-radius: 14px;
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
  transform: translateX(4px);
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
  flex-shrink: 0;
}

.nav-label {
  flex: 1;
}

.nav-indicator {
  width: 6px;
  height: 6px;
  background: white;
  border-radius: 50%;
  opacity: 0;
}

.nav-item.active .nav-indicator {
  opacity: 1;
  animation: pulseDot 2s infinite;
}

.sidebar-footer {
  padding: 20px 16px;
  border-top: 1px solid rgba(226, 232, 240, 0.6);
  background: linear-gradient(135deg, rgba(236, 72, 153, 0.02), rgba(99, 102, 241, 0.03));
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.user-card {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px;
  border-radius: 16px;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.7));
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
  border: 1px solid rgba(99, 102, 241, 0.08);
}

.user-avatar {
  position: relative;
}

.avatar-svg {
  filter: drop-shadow(0 6px 20px rgba(99, 102, 241, 0.3));
}

.avatar-badge {
  position: absolute;
  bottom: -2px;
  right: -2px;
  width: 20px;
  height: 20px;
  background: linear-gradient(135deg, #10b981, #34d399);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  border: 3px solid white;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);
}

.avatar-badge svg {
  width: 12px;
  height: 12px;
  stroke-width: 3;
}

.user-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.user-name {
  font-weight: 700;
  color: #1e293b;
  font-size: 15px;
}

.user-role {
  font-size: 12px;
  color: #64748b;
  font-weight: 600;
}

.menu-dots {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  border: none;
  background: rgba(99, 102, 241, 0.06);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  color: #64748b;
}

.menu-dots:hover {
  background: rgba(99, 102, 241, 0.12);
  transform: scale(1.05);
}

.logout-btn {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 16px;
  border-radius: 14px;
  border: none;
  background: linear-gradient(135deg, rgba(239, 68, 68, 0.06), rgba(220, 38, 38, 0.04));
  cursor: pointer;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  color: #ef4444;
  font-weight: 600;
  font-size: 14px;
  width: 100%;
}

.logout-btn:hover {
  background: linear-gradient(135deg, rgba(239, 68, 68, 0.12), rgba(220, 38, 38, 0.08));
  transform: translateX(4px);
}

.logout-icon {
  width: 20px;
  height: 20px;
  stroke-width: 2.2px;
}

.main-content {
  flex: 1;
  overflow-y: auto;
  padding: 32px;
  z-index: 1;
}

.main-content::-webkit-scrollbar {
  width: 8px;
}

.main-content::-webkit-scrollbar-track {
  background: transparent;
}

.main-content::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, #6366f1, #ec4899);
  border-radius: 4px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 32px;
  gap: 20px;
}

.greeting-card {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 20px 24px;
  background: rgba(255, 255, 255, 0.92);
  border-radius: 20px;
  box-shadow: 0 8px 32px rgba(99, 102, 241, 0.06);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(99, 102, 241, 0.08);
}

.greeting-icon-container {
  width: 64px;
  height: 64px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, rgba(251, 191, 36, 0.1), rgba(245, 158, 11, 0.06));
  animation: pulse 3s infinite ease-in-out;
}

.greeting-svg {
  width: 56px;
  height: 56px;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

.page-title {
  font-size: 26px;
  font-weight: 800;
  background: linear-gradient(135deg, #1e293b, #475569);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: 0;
}

.page-desc {
  color: #64748b;
  font-size: 14px;
  font-weight: 500;
  margin: 4px 0 0 0;
}

.header-right {
  display: flex;
  align-items: center;
}

.action-buttons {
  display: flex;
  align-items: center;
  gap: 12px;
}

.header-btn {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 18px;
  background: rgba(255, 255, 255, 0.92);
  border-radius: 14px;
  cursor: pointer;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.04);
  border: 1px solid rgba(99, 102, 241, 0.06);
  color: #475569;
  font-weight: 600;
  font-size: 14px;
}

.header-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 32px rgba(99, 102, 241, 0.12);
}

.header-btn.icon-btn {
  padding: 12px 14px;
  position: relative;
}

.header-btn.primary-btn {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: white;
  border: none;
  box-shadow: 0 8px 32px rgba(99, 102, 241, 0.3);
}

.header-btn.primary-btn:hover {
  box-shadow: 0 12px 40px rgba(99, 102, 241, 0.4);
}

.header-btn svg {
  width: 20px;
  height: 20px;
  stroke-width: 2.2px;
}

.notification-badge {
  position: absolute;
  top: 8px;
  right: 8px;
  width: 20px;
  height: 20px;
  background: linear-gradient(135deg, #ec4899, #f472b6);
  color: white;
  border-radius: 50%;
  font-size: 11px;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid white;
  box-shadow: 0 4px 12px rgba(236, 72, 153, 0.4);
  animation: pulseDot 2s infinite;
}

@keyframes pulseDot {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.15); opacity: 0.8; }
}

.header-date-picker {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 18px;
  background: rgba(255, 255, 255, 0.92);
  border-radius: 14px;
  border: 1px solid rgba(99, 102, 241, 0.06);
  color: #475569;
  font-weight: 600;
  font-size: 14px;
}

.header-date-picker svg {
  width: 20px;
  height: 20px;
  stroke-width: 2.2px;
  color: #f59e0b;
}

.date-text {
  white-space: nowrap;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-bottom: 28px;
}

.stat-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 22px;
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 8px 32px rgba(99, 102, 241, 0.06);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(99, 102, 241, 0.08);
}

.stat-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 20px 48px rgba(99, 102, 241, 0.15);
}

.stat-decoration {
  position: absolute;
  top: -20px;
  right: -20px;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  opacity: 0.1;
  transition: all 0.4s ease;
}

.stat-card.primary .stat-decoration {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
}

.stat-card.success .stat-decoration {
  background: linear-gradient(135deg, #10b981, #34d399);
}

.stat-card.warning .stat-decoration {
  background: linear-gradient(135deg, #f59e0b, #fbbf24);
}

.stat-card.danger .stat-decoration {
  background: linear-gradient(135deg, #ef4444, #dc2626);
}

.stat-card:hover .stat-decoration {
  transform: scale(1.2);
  opacity: 0.15;
}

.stat-content {
  display: flex;
  align-items: center;
  gap: 16px;
  z-index: 1;
}

.stat-icon-wrapper {
  width: 64px;
  height: 64px;
  border-radius: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.stat-card.primary .stat-icon-wrapper {
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(139, 92, 246, 0.08));
  color: #6366f1;
}

.stat-card.success .stat-icon-wrapper {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(52, 211, 153, 0.08));
  color: #10b981;
}

.stat-card.warning .stat-icon-wrapper {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.12), rgba(251, 191, 36, 0.08));
  color: #f59e0b;
}

.stat-card.danger .stat-icon-wrapper {
  background: linear-gradient(135deg, rgba(239, 68, 68, 0.12), rgba(220, 38, 38, 0.08));
  color: #ef4444;
}

.stat-icon-wrapper svg {
  width: 28px;
  height: 28px;
  stroke-width: 2.2px;
}

.stat-info {
  flex: 1;
}

.stat-value {
  font-size: 36px;
  font-weight: 800;
  line-height: 1;
  display: block;
  transition: all 0.3s ease;
}

.stat-card.primary .stat-value {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.stat-card.success .stat-value {
  background: linear-gradient(135deg, #10b981, #34d399);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.stat-card.warning .stat-value {
  background: linear-gradient(135deg, #f59e0b, #fbbf24);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.stat-card.danger .stat-value {
  background: linear-gradient(135deg, #ef4444, #dc2626);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.stat-label {
  font-size: 14px;
  color: #64748b;
  margin-top: 6px;
  font-weight: 600;
}

.stat-trend {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: 12px;
  font-size: 13px;
  font-weight: 700;
  align-self: flex-start;
  z-index: 1;
}

.stat-trend.positive {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(52, 211, 153, 0.08));
  color: #10b981;
}

.stat-trend.negative {
  background: linear-gradient(135deg, rgba(239, 68, 68, 0.12), rgba(220, 38, 38, 0.08));
  color: #ef4444;
}

.stat-trend.neutral {
  background: linear-gradient(135deg, rgba(148, 163, 184, 0.12), rgba(100, 116, 139, 0.08));
  color: #64748b;
}

.stat-trend svg {
  width: 16px;
  height: 16px;
  stroke-width: 2.5px;
}

.charts-section {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 24px;
  margin-bottom: 28px;
}

.chart-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 24px;
  padding: 28px;
  box-shadow: 0 8px 32px rgba(99, 102, 241, 0.06);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(99, 102, 241, 0.08);
  transition: all 0.4s ease;
}

.chart-card:hover {
  box-shadow: 0 16px 48px rgba(99, 102, 241, 0.12);
  transform: translateY(-4px);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  gap: 16px;
}

.card-title-section {
  display: flex;
  align-items: center;
  gap: 14px;
}

.card-icon-wrapper {
  width: 48px;
  height: 48px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(139, 92, 246, 0.08));
  color: #6366f1;
}

.card-icon-wrapper.success {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(52, 211, 153, 0.08));
  color: #10b981;
}

.card-icon-wrapper svg {
  width: 24px;
  height: 24px;
  stroke-width: 2.2px;
}

.card-title-text {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.card-title-text h3 {
  font-size: 20px;
  font-weight: 800;
  color: #1e293b;
  margin: 0;
}

.card-subtitle {
  font-size: 13px;
  color: #64748b;
  font-weight: 500;
}

.chart-controls {
  display: flex;
  align-items: center;
  gap: 12px;
}

.period-selector {
  display: flex;
  background: rgba(148, 163, 184, 0.08);
  padding: 4px;
  border-radius: 12px;
  gap: 4px;
}

.period-btn {
  padding: 8px 16px;
  border: none;
  background: transparent;
  color: #64748b;
  font-weight: 600;
  font-size: 13px;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.period-btn:hover {
  background: rgba(99, 102, 241, 0.08);
  color: #1e293b;
}

.period-btn.active {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: white;
  box-shadow: 0 4px 16px rgba(99, 102, 241, 0.25);
}

.chart-container {
  height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.line-chart {
  width: 100%;
  height: 100%;
}

.chart-legend {
  display: flex;
  gap: 24px;
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid rgba(226, 232, 240, 0.6);
}

.chart-legend .legend-item {
  display: flex;
  align-items: center;
  gap: 8px;
}

.chart-legend .legend-dot {
  width: 12px;
  height: 12px;
  border-radius: 4px;
}

.chart-legend .legend-text {
  color: #475569;
  font-weight: 600;
  font-size: 13px;
}

.pie-chart-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 220px;
  margin-bottom: 8px;
}

.pie-chart {
  width: 220px;
  height: 220px;
}

.pie-legend {
  display: flex;
  flex-direction: column;
  gap: 14px;
  padding: 8px 0;
}

.pie-legend .legend-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 14px;
  border-radius: 12px;
  transition: all 0.3s ease;
  cursor: pointer;
}

.pie-legend .legend-item:hover {
  background: rgba(99, 102, 241, 0.06);
  transform: translateX(4px);
}

.pie-legend .legend-color {
  width: 14px;
  height: 14px;
  border-radius: 5px;
}

.pie-legend .legend-label {
  flex: 1;
  color: #475569;
  font-size: 14px;
  font-weight: 600;
}

.pie-legend .legend-value {
  font-weight: 800;
  color: #1e293b;
  font-size: 15px;
}

.tasks-section {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 24px;
  padding: 28px;
  box-shadow: 0 8px 32px rgba(99, 102, 241, 0.06);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(99, 102, 241, 0.08);
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  gap: 16px;
}

.section-title-wrapper {
  display: flex;
  align-items: center;
  gap: 14px;
}

.section-icon-wrapper {
  width: 48px;
  height: 48px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(139, 92, 246, 0.08));
  color: #6366f1;
}

.section-icon-wrapper svg {
  width: 24px;
  height: 24px;
  stroke-width: 2.2px;
}

.section-title-text {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.section-title-text h2 {
  font-size: 22px;
  font-weight: 800;
  color: #1e293b;
  margin: 0;
}

.task-count {
  padding: 6px 12px;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(139, 92, 246, 0.08));
  color: #6366f1;
  font-weight: 700;
  font-size: 13px;
  border-radius: 10px;
}

.add-task-btn {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 24px;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: white;
  border: none;
  border-radius: 14px;
  cursor: pointer;
  font-weight: 700;
  font-size: 14px;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 8px 32px rgba(99, 102, 241, 0.3);
}

.add-task-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 40px rgba(99, 102, 241, 0.4);
}

.add-task-btn svg {
  width: 20px;
  height: 20px;
  stroke-width: 2.2px;
}

.tasks-table {
  overflow-x: auto;
}

.table-header {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr 1fr 1fr;
  gap: 16px;
  padding: 16px 20px;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.06), rgba(139, 92, 246, 0.04));
  border-radius: 14px;
  margin-bottom: 8px;
}

.table-header .table-cell {
  font-weight: 700;
  color: #334155;
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.table-body {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.table-row {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr 1fr 1fr;
  gap: 16px;
  padding: 16px 20px;
  background: rgba(248, 250, 252, 0.6);
  border-radius: 14px;
  transition: all 0.3s ease;
  cursor: pointer;
  border: 1px solid transparent;
}

.table-row:hover {
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.04), rgba(139, 92, 246, 0.02));
  border-color: rgba(99, 102, 241, 0.1);
  transform: translateX(4px);
}

.task-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.task-icon {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  flex-shrink: 0;
}

.task-icon svg {
  width: 20px;
  height: 20px;
  stroke-width: 2.2px;
  color: white;
}

.task-name {
  font-weight: 700;
  color: #1e293b;
  font-size: 14px;
}

.module-tag {
  padding: 6px 12px;
  border-radius: 10px;
  font-weight: 700;
  font-size: 12px;
  display: inline-block;
}

.module-primary {
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(139, 92, 246, 0.08));
  color: #6366f1;
}

.module-pink {
  background: linear-gradient(135deg, rgba(236, 72, 153, 0.12), rgba(244, 114, 182, 0.08));
  color: #ec4899;
}

.module-green {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(52, 211, 153, 0.08));
  color: #10b981;
}

.module-yellow {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.12), rgba(251, 191, 36, 0.08));
  color: #f59e0b;
}

.students-display {
  display: flex;
  align-items: center;
  gap: 10px;
}

.mini-avatars {
  display: flex;
}

.mini-avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  border: 3px solid white;
  margin-left: -10px;
  box-shadow: 0 2px 8px rgba(99, 102, 241, 0.2);
}

.mini-avatar:first-child {
  margin-left: 0;
}

.students-text {
  color: #475569;
  font-weight: 600;
  font-size: 13px;
}

.deadline-display {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #64748b;
  font-weight: 600;
  font-size: 13px;
}

.deadline-display svg {
  width: 16px;
  height: 16px;
  stroke-width: 2.2px;
  color: #f59e0b;
}

.status-badge {
  padding: 6px 14px;
  border-radius: 10px;
  font-weight: 700;
  font-size: 12px;
  display: inline-block;
}

.status-pending {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.12), rgba(251, 191, 36, 0.08));
  color: #f59e0b;
}

.status-completed {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(52, 211, 153, 0.08));
  color: #10b981;
}

.table-cell.actions-cell {
  display: flex;
  gap: 8px;
  align-items: center;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  font-size: 13px;
  border: none;
  background: transparent;
}

.view-btn {
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.06));
  color: #6366f1;
}

.view-btn:hover {
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(139, 92, 246, 0.1));
  transform: translateY(-2px);
}

.grade-btn {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(52, 211, 153, 0.06));
  color: #10b981;
}

.grade-btn:hover {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(52, 211, 153, 0.1));
  transform: translateY(-2px);
}

.action-btn svg {
  width: 16px;
  height: 16px;
  stroke-width: 2.2px;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 20px;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.modal-content {
  background: rgba(255, 255, 255, 0.98);
  border-radius: 28px;
  width: 100%;
  max-width: 580px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 24px 80px rgba(0, 0, 0, 0.2);
  animation: slideUp 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

@keyframes slideUp {
  from { transform: translateY(20px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 28px 28px 20px;
  border-bottom: 1px solid rgba(226, 232, 240, 0.6);
}

.modal-title-section {
  display: flex;
  align-items: center;
  gap: 14px;
}

.modal-icon {
  width: 52px;
  height: 52px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(139, 92, 246, 0.08));
  color: #6366f1;
}

.modal-icon svg {
  width: 26px;
  height: 26px;
  stroke-width: 2.2px;
}

.modal-title-text h2 {
  font-size: 22px;
  font-weight: 800;
  color: #1e293b;
  margin: 0;
}

.modal-title-text p {
  color: #64748b;
  font-size: 13px;
  font-weight: 500;
  margin: 4px 0 0 0;
}

.modal-close {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  border: none;
  background: rgba(148, 163, 184, 0.12);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #64748b;
  transition: all 0.3s ease;
}

.modal-close:hover {
  background: rgba(239, 68, 68, 0.12);
  color: #ef4444;
  transform: rotate(90deg);
}

.modal-close svg {
  width: 20px;
  height: 20px;
  stroke-width: 2.2px;
}

.modal-body {
  padding: 24px 28px;
}

.task-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-label {
  font-weight: 700;
  color: #334155;
  font-size: 14px;
}

.form-input,
.form-textarea,
.form-select {
  padding: 14px 16px;
  border-radius: 14px;
  border: 2px solid rgba(99, 102, 241, 0.12);
  background: rgba(248, 250, 252, 0.8);
  font-size: 14px;
  font-weight: 500;
  color: #1e293b;
  transition: all 0.3s ease;
  font-family: inherit;
}

.form-input:focus,
.form-textarea:focus,
.form-select:focus {
  outline: none;
  border-color: #6366f1;
  background: white;
  box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.1);
}

.form-input::placeholder,
.form-textarea::placeholder {
  color: #94a3b8;
}

.form-textarea {
  resize: vertical;
  min-height: 100px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.module-selector {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
}

.module-option {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 16px 12px;
  border-radius: 14px;
  border: 2px solid rgba(99, 102, 241, 0.1);
  background: rgba(248, 250, 252, 0.6);
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 600;
  color: #475569;
  font-size: 13px;
}

.module-option:hover {
  border-color: rgba(99, 102, 241, 0.2);
  background: rgba(99, 102, 241, 0.04);
  transform: translateY(-2px);
}

.module-option.active {
  border-color: #6366f1;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(139, 92, 246, 0.06));
  color: #6366f1;
  box-shadow: 0 4px 16px rgba(99, 102, 241, 0.15);
}

.module-option-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.module-option-icon svg {
  width: 22px;
  height: 22px;
  stroke-width: 2.2px;
  color: white;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  padding: 20px 28px 28px;
  border-top: 1px solid rgba(226, 232, 240, 0.6);
}

.modal-btn {
  padding: 12px 28px;
  border-radius: 14px;
  cursor: pointer;
  font-weight: 700;
  font-size: 14px;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  display: flex;
  align-items: center;
  gap: 8px;
}

.modal-btn.cancel-btn {
  background: #f1f5f9;
  color: #475569;
  border: 1px solid #e2e8f0;
}

.modal-btn.cancel-btn:hover {
  background: #e2e8f0;
  transform: translateY(-2px);
}

.modal-btn.confirm-btn {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: white;
  border: none;
  box-shadow: 0 8px 32px rgba(99, 102, 241, 0.3);
}

.modal-btn.confirm-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 40px rgba(99, 102, 241, 0.4);
}

.modal-btn svg {
  width: 18px;
  height: 18px;
  stroke-width: 2.2px;
}

@media (max-width: 1400px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .charts-section {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 1024px) {
  .dashboard-container {
    flex-direction: column;
  }
  
  .sidebar {
    width: 100%;
    height: auto;
    position: relative;
  }
  
  .sidebar-nav {
    display: none;
  }
  
  .main-content {
    padding: 24px;
  }
  
  .header {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
  }
  
  .table-header,
  .table-row {
    grid-template-columns: 1.5fr 1fr 1fr;
  }
  
  .table-cell:nth-child(n+4) {
    display: none;
  }
}

@media (max-width: 640px) {
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .main-content {
    padding: 16px;
  }
  
  .action-buttons {
    flex-wrap: wrap;
    width: 100%;
  }
  
  .header-btn,
  .header-date-picker {
    flex: 1;
    justify-content: center;
  }
  
  .form-row {
    grid-template-columns: 1fr;
  }
  
  .module-selector {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .table-header,
  .table-row {
    grid-template-columns: 1fr;
    gap: 12px;
  }
  
  .table-cell:not(.task-name-cell) {
    display: none;
  }
}

.page-container {
  padding-top: 20px;
}

.page-header {
  margin-bottom: 32px;
}

.page-header .page-title {
  font-size: 26px;
  font-weight: 800;
  color: #1e293b;
  margin: 0;
}

.page-header .page-desc {
  color: #64748b;
  font-size: 14px;
  margin: 6px 0 0 0;
}

.students-container {
  padding: 20px 0;
}

.students-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 24px;
}

.student-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  padding: 28px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.06);
  border: 1px solid rgba(99, 102, 241, 0.08);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.student-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 16px 40px rgba(99, 102, 241, 0.12);
}

.student-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  overflow: hidden;
}

.student-avatar svg {
  width: 100%;
  height: 100%;
}

.student-info {
  text-align: center;
}

.student-name {
  display: block;
  font-size: 18px;
  font-weight: 700;
  color: #1e293b;
}

.student-class {
  font-size: 13px;
  color: #64748b;
  font-weight: 500;
}

.student-score {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background: rgba(99, 102, 241, 0.06);
  border-radius: 12px;
}

.score-label {
  font-size: 13px;
  color: #64748b;
}

.score-value {
  font-size: 18px;
  font-weight: 800;
  color: #6366f1;
}

.resources-container {
  padding: 20px 0;
}

.resources-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 24px;
}

.resource-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.06);
  border: 1px solid rgba(99, 102, 241, 0.08);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.resource-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 16px 40px rgba(99, 102, 241, 0.12);
}

.resource-icon {
  width: 64px;
  height: 64px;
  border-radius: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.resource-icon svg {
  width: 30px;
  height: 30px;
  stroke-width: 2.2px;
}

.resource-info {
  flex: 1;
}

.resource-name {
  display: block;
  font-size: 18px;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 6px;
}

.resource-desc {
  font-size: 14px;
  color: #64748b;
  line-height: 1.5;
}

.resource-action {
  align-self: flex-start;
  padding: 12px 24px;
  background: rgba(99, 102, 241, 0.08);
  border: none;
  border-radius: 12px;
  color: #6366f1;
  font-weight: 600;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.resource-action:hover {
  background: rgba(99, 102, 241, 0.15);
  transform: translateY(-2px);
}

.task-list-container {
  padding: 20px 0;
}

.add-task-btn {
  margin-top: 24px;
  padding: 16px 32px;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: white;
  border: none;
  border-radius: 16px;
  font-weight: 700;
  font-size: 15px;
  cursor: pointer;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 8px 32px rgba(99, 102, 241, 0.3);
  display: flex;
  align-items: center;
  gap: 10px;
}

.add-task-btn:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(99, 102, 241, 0.4);
}

.add-task-btn svg {
  width: 20px;
  height: 20px;
  stroke-width: 2.2px;
}

.settings-container {
  padding: 20px 0;
}

.settings-section {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  padding: 28px;
  margin-bottom: 24px;
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.06);
  border: 1px solid rgba(99, 102, 241, 0.08);
}

.section-title {
  font-size: 18px;
  font-weight: 700;
  color: #1e293b;
  margin: 0 0 20px 0;
}

.settings-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.settings-form .form-row {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.settings-form .form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.settings-form label {
  font-weight: 600;
  color: #475569;
  font-size: 14px;
}

.settings-form .form-input,
.settings-form .form-select {
  padding: 14px 18px;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  font-size: 14px;
  color: #1e293b;
  background: #f8fafc;
}

.settings-form .form-input:focus,
.settings-form .form-select:focus {
  outline: none;
  border-color: #6366f1;
  background: white;
}

.resource-modal {
  max-width: 800px;
}

.resource-content {
  padding: 10px 0;
}

.resource-content-inner {
  line-height: 1.8;
  color: #334155;
}

.resource-content-inner h1 {
  font-size: 24px;
  font-weight: 800;
  color: #1e293b;
  margin: 0 0 20px 0;
  padding-bottom: 12px;
  border-bottom: 2px solid #e2e8f0;
}

.resource-content-inner h2 {
  font-size: 20px;
  font-weight: 700;
  color: #1e293b;
  margin: 24px 0 12px 0;
}

.resource-content-inner h3 {
  font-size: 16px;
  font-weight: 600;
  color: #334155;
  margin: 16px 0 8px 0;
}

.resource-content-inner p {
  margin: 8px 0;
}

.resource-content-inner ul {
  margin: 8px 0 8px 24px;
  padding-left: 0;
}

.resource-content-inner li {
  margin-bottom: 6px;
  position: relative;
  padding-left: 20px;
}

.resource-content-inner li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 8px;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #6366f1;
}

.resource-content-inner strong {
  font-weight: 700;
  color: #1e293b;
}

.resource-content-inner code {
  background: rgba(99, 102, 241, 0.1);
  padding: 2px 8px;
  border-radius: 6px;
  font-family: 'Monaco', 'Menlo', monospace;
  font-size: 14px;
  color: #6366f1;
}

.resource-content-inner pre {
  background: #1e293b;
  padding: 16px;
  border-radius: 12px;
  overflow-x: auto;
  margin: 12px 0;
}

.resource-content-inner pre code {
  background: transparent;
  color: #e2e8f0;
  padding: 0;
}
</style>
