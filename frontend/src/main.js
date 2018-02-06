/* eslint-disable no-new */
import Vue from 'vue'
import App from './App'
import router from './router'
import Upload from './App.vue' /* 2/5 */

Vue.config.productionTip = false

new Vue({                    /* 2/5 */
  el: '#upload',             /* 2/5 */
  render: h => h(Upload)     /* 2/5 ... what does this line do? */
})                           /* 2/5 */

new Vue({
  el: '#app',
  router,
  render: h => h(App)          /* what does App mean here, exactly? */
})
