import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/student-workspace',
    name: 'StudentWorkspace',
    component: () => import('../views/StudentWorkspace.vue'),
    meta: { requiredRole: 'student' }
  },
  {
    path: '/teacher-dashboard',
    name: 'TeacherDashboard',
    component: () => import('../views/TeacherDashboard.vue'),
    meta: { requiredRole: 'teacher' }
  }
]

const router = createRouter({
  history: createWebHistory('/stuu/'),
  routes
})

router.beforeEach((to, from, next) => {
  const currentRole = localStorage.getItem('currentRole')
  
  if (to.path === '/' || to.path === '/register') {
    next()
    return
  }
  
  if (!currentRole) {
    next('/')
    return
  }
  
  if (to.meta.requiredRole && to.meta.requiredRole !== currentRole) {
    if (currentRole === 'student') {
      next('/student-workspace')
    } else {
      next('/teacher-dashboard')
    }
    return
  }
  
  next()
})

export default router