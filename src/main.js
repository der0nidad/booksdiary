import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
// YourComponent.vue or main.js for global usage
import VueScrollProgress from 'vue-scroll-progress'

Vue.use(VueScrollProgress)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
