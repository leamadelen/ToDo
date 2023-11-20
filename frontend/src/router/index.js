import Register from '../views/RegisterView.vue';
import Login from '../views/LoginView.vue';
import Dashboard from '../views/DashboardView.vue';
import Profile from '../views/ProfileView.vue';
import { getToken } from '../utils/auth';
import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  { path: '/', redirect: '/dashboard' },
  { path: '/register', component: Register },
  { path: '/login', component: Login },
  { path: '/dashboard', component: Dashboard, meta: { requiresAuth: true } },
  { path: '/profile', component: Profile, meta: { requiresAuth: true } }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
      const token = getToken();
      if (!token) {
          next('/login');
      } else {
          next();
      }
  } else {
      next();
  }
});

export default router;