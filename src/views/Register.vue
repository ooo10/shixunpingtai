<template>
  <div class="register-container">
    <div class="register-card">
      <div class="card-header">
        <div class="logo">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
            <path d="M12 2L2 7l10 5 10-5-10-5z"/>
            <path d="M2 17l10 5 10-5"/>
            <path d="M2 12l10 5 10-5"/>
          </svg>
        </div>
        <h1>AIGC实训平台</h1>
        <p>创建您的账号开始学习之旅</p>
      </div>

      <div class="form-group">
        <label>用户名</label>
        <input 
          v-model="username"
          type="text" 
          placeholder="请输入用户名"
          class="form-input"
        />
      </div>

      <div class="form-group">
        <label>密码</label>
        <input 
          v-model="password"
          type="password" 
          placeholder="请输入密码"
          class="form-input"
        />
      </div>

      <div class="form-group">
        <label>确认密码</label>
        <input 
          v-model="confirmPassword"
          type="password" 
          placeholder="请再次输入密码"
          class="form-input"
        />
      </div>

      <div class="form-group">
        <label>角色</label>
        <div class="role-buttons">
          <button 
            :class="['role-btn', { active: role === 'student' }]"
            @click="role = 'student'"
          >
            学生
          </button>
          <button 
            :class="['role-btn', { active: role === 'teacher' }]"
            @click="role = 'teacher'"
          >
            教师
          </button>
        </div>
      </div>

      <button class="register-btn" @click="handleRegister">
        立即注册
      </button>

      <div v-if="message" :class="['message', { error: isError, success: !isError }]">
        {{ message }}
      </div>

      <div class="login-link">
        <span>已有账号？</span>
        <button @click="goToLogin">立即登录</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const username = ref('')
const password = ref('')
const confirmPassword = ref('')
const role = ref('student')
const message = ref('')
const isError = ref(false)

const handleRegister = () => {
  message.value = ''
  
  if (!username.value.trim()) {
    message.value = '请输入用户名'
    isError.value = true
    return
  }
  
  if (username.value.length < 3) {
    message.value = '用户名至少需要3个字符'
    isError.value = true
    return
  }
  
  if (!password.value) {
    message.value = '请输入密码'
    isError.value = true
    return
  }
  
  if (password.value.length < 6) {
    message.value = '密码至少需要6个字符'
    isError.value = true
    return
  }
  
  if (confirmPassword.value !== password.value) {
    message.value = '两次输入的密码不一致'
    isError.value = true
    return
  }
  
  const users = JSON.parse(localStorage.getItem('users') || '[]')
  if (users.some(u => u.username === username.value)) {
    message.value = '用户名已存在'
    isError.value = true
    return
  }
  
  users.push({
    username: username.value,
    password: password.value,
    role: role.value
  })
  localStorage.setItem('users', JSON.stringify(users))
  
  message.value = '注册成功！正在跳转到登录页面...'
  isError.value = false
  
  setTimeout(() => {
    router.push('/')
  }, 2000)
}

const goToLogin = () => {
  router.push('/')
}
</script>

<style scoped>
.register-container {
  min-height: 100vh;
  background: #f8fafc;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.register-card {
  width: 100%;
  max-width: 400px;
  background: white;
  border-radius: 20px;
  padding: 40px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.1);
}

.card-header {
  text-align: center;
  margin-bottom: 30px;
}

.logo {
  width: 60px;
  height: 60px;
  margin: 0 auto 20px;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-header h1 {
  font-size: 24px;
  font-weight: bold;
  color: #1e293b;
  margin: 0 0 8px 0;
}

.card-header p {
  font-size: 14px;
  color: #64748b;
  margin: 0;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  font-size: 14px;
  font-weight: 600;
  color: #374151;
  margin-bottom: 8px;
}

.form-input {
  width: 100%;
  height: 48px;
  padding: 0 16px;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 15px;
  outline: none;
  transition: border-color 0.3s;
}

.form-input:focus {
  border-color: #6366f1;
}

.role-buttons {
  display: flex;
  gap: 12px;
}

.role-btn {
  flex: 1;
  padding: 14px;
  border-radius: 12px;
  border: 2px solid #e5e7eb;
  background: white;
  color: #4b5563;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.role-btn:hover {
  border-color: #6366f1;
  color: #6366f1;
}

.role-btn.active {
  border-color: #6366f1;
  background: linear-gradient(135deg, rgba(99,102,241,0.1), rgba(139,92,246,0.08));
  color: #6366f1;
}

.register-btn {
  width: 100%;
  height: 52px;
  background: linear-gradient(135deg, #3b82f6, #6366f1, #8b5cf6);
  border: none;
  border-radius: 12px;
  color: white;
  font-size: 16px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s;
}

.register-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(99,102,241,0.4);
}

.message {
  text-align: center;
  padding: 12px;
  border-radius: 10px;
  margin-top: 16px;
  font-size: 14px;
}

.message.error {
  background: rgba(239, 68, 68, 0.08);
  color: #ef4444;
}

.message.success {
  background: rgba(16, 185, 129, 0.08);
  color: #10b981;
}

.login-link {
  text-align: center;
  margin-top: 20px;
}

.login-link span {
  color: #6b7280;
  font-size: 14px;
}

.login-link button {
  background: none;
  border: none;
  color: #6366f1;
  font-weight: 600;
  cursor: pointer;
  margin-left: 4px;
}

.login-link button:hover {
  color: #4f46e5;
}
</style>