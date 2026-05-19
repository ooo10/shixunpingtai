<template>
  <div class="login-container">
    <div class="login-card">
      <div class="card-header">
        <div class="logo">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
            <path d="M12 2L2 7l10 5 10-5-10-5z"/>
            <path d="M2 17l10 5 10-5"/>
            <path d="M2 12l10 5 10-5"/>
          </svg>
        </div>
        <h1>AIGC实训平台</h1>
      </div>

      <div class="form-group">
        <label>用户名</label>
        <input v-model="loginForm.username" type="text" placeholder="请输入用户名" />
      </div>

      <div class="form-group">
        <label>密码</label>
        <input v-model="loginForm.password" type="password" placeholder="请输入密码" />
      </div>

      <div class="form-group">
        <label>角色</label>
        <div class="role-buttons">
          <button 
            :class="['role-btn', { active: loginForm.role === 'student' }]"
            @click="loginForm.role = 'student'"
          >
            学生
          </button>
          <button 
            :class="['role-btn', { active: loginForm.role === 'teacher' }]"
            @click="loginForm.role = 'teacher'"
          >
            教师
          </button>
        </div>
      </div>

      <button class="login-btn" @click="handleLogin" :disabled="isLoading">
        {{ isLoading ? '登录中...' : '登 录' }}
      </button>

      <div class="register-link">
        <span>还没有账号?</span>
        <button @click="handleRegister">立即注册</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const loginForm = reactive({
  username: '',
  password: '',
  role: 'student'
})
const isLoading = ref(false)

const handleLogin = () => {
  if (!loginForm.username.trim() || !loginForm.password) {
    alert('请输入用户名和密码')
    return
  }
  
  isLoading.value = true
  
  setTimeout(() => {
    const users = JSON.parse(localStorage.getItem('users') || '[]')
    const user = users.find(u => u.username === loginForm.username && u.password === loginForm.password)
    
    if (user && user.role === loginForm.role) {
      localStorage.setItem('currentRole', user.role)
      localStorage.setItem('currentUsername', user.username)
      if (user.role === 'student') {
        router.push('/student-workspace')
      } else {
        router.push('/teacher-dashboard')
      }
    } else {
      alert('用户名或密码错误，或角色不匹配')
    }
    
    isLoading.value = false
  }, 1000)
}

const handleRegister = () => {
  router.push('/register')
}
</script>

<style scoped>
.login-container {
  min-height: 100vh;
  background: #f8fafc;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.login-card {
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

.form-group input {
  width: 100%;
  height: 48px;
  padding: 0 16px;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 15px;
  outline: none;
  transition: border-color 0.3s;
}

.form-group input:focus {
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

.login-btn {
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

.login-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(99,102,241,0.4);
}

.login-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.register-link {
  text-align: center;
  margin-top: 20px;
}

.register-link span {
  color: #6b7280;
  font-size: 14px;
}

.register-link button {
  background: none;
  border: none;
  color: #6366f1;
  font-weight: 600;
  cursor: pointer;
  margin-left: 4px;
}

.register-link button:hover {
  color: #4f46e5;
}
</style>