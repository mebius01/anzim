import Vue from 'vue'
import App from './App.vue'
import Articles from './components/Articles.vue'

Vue.component('Articles', Articles)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
