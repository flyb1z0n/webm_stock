import Vue from 'vue'
import App from './App.vue'
import VModal from 'vue-js-modal'
import infiniteScroll from 'vue-infinite-scroll'


Vue.config.productionTip = false
Vue.use(VModal)
Vue.use(infiniteScroll)

new Vue({
  render: h => h(App),
}).$mount('#app')
