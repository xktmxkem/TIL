import Vue from 'vue'
import VueRouter from 'vue-router'
import Lotto from '@/views/TheLotto'
import Lunch from '@/views/TheLunch'

Vue.use(VueRouter)

const routes = [
  {
    path: '/lunch',
    component: Lunch,
    name: 'Lunch',
  },

  {
    path: '/lotto/:num',
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
