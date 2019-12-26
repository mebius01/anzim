import Vue from 'vue'
import App from './App.vue'
import Article from './components/Article.vue'

Vue.component('Article', Article)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
