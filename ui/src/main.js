import Vue from 'vue'
import App from './App.vue'
import VModal from 'vue-js-modal'
import InfiniteScroll from 'vue-infinite-scroll'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false
Vue.use(VModal)
Vue.use(InfiniteScroll)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

new Vue({
  render: h => h(App),
}).$mount('#app')
