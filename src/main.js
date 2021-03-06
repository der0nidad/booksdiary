import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
// YourComponent.vue or main.js for global usage
import Router from '@/router/routes'

Vue.use(Router)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router: Router,
}).$mount('#app')
