import Vue from 'vue'
import VueRouter from 'vue-router'
import Lunch from '@/views/TheLunch'
import Lotto from '@/views/TheLotto'


Vue.use(VueRouter)

const routes = [
 {
   path: "/lunch",
   component: Lunch,
   name: 'Lunch',
  
  },
 {
   path: "/lotto/6",
   component: Lotto,
   name: 'Lotto',
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
