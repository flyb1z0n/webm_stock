import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import InfiniteScroll from 'vue-infinite-scroll'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false
Vue.use(InfiniteScroll)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(Vuex)

//TODO play with a state
const store = new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment (state) {
      state.count++
    }
  }
})


new Vue({
  render: h => h(App),
  el: '#app',
  store: store
})
