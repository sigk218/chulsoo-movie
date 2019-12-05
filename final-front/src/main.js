import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import VueSession from 'vue-session'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import infiniteScroll from 'vue-infinite-scroll'

Vue.config.productionTip = false
Vue.use(VueSession)
Vue.use(infiniteScroll)

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
