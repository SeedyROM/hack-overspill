import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from './pages/Home'
import Question from './pages/Question'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: Home,
  },
  {
    path: '/question/:pk',
    component: Question,
  }
]

export default new VueRouter({
  mode: 'history',
  routes,
})