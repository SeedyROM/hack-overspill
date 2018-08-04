import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Beufy from 'buefy'

import App from './components/App'

import router from './router'

Vue.use(Beufy)
Vue.use(VueAxios, axios.create({
  baseURL: 'http://localhost:8000/'
}))

new Vue({
    el: '#app',
    render: h => h(App),
    router,
})