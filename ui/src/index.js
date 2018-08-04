import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Beufy from 'buefy'

import App from './components/App'

Vue.use(Beufy)
Vue.use(VueAxios, axios)

new Vue({
    el: '#app',
    render: h => h(App),
})