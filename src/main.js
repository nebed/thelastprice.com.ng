import Vue from 'vue';
import axios from 'axios';
import App from './App.vue';
import router from './router';

window.vue = Vue;
window.axios = axios;
require('./assets/sass/main.scss');
Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
