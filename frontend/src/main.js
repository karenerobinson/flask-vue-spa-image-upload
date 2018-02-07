/* eslint-disable no-new */
import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  render: h => h(App)          /* what does App mean here, exactly? */
})
