import Vue from 'vue'
import Router from 'vue-router'

let routes = [

{
	path: '/',
	component: require('../views/Home.vue').default
},

{
	path: '/about',
	component: require('../views/About.vue').default
},

{
	path: '/cinemas',
	component: require('../views/Cinemas.vue').default
},

{
	path: '/travelbybus',
	component: require('../views/Bus.vue').default
},

{
	path: '*',
	component: require('../views/Notfound.vue').default
}

];
Vue.use(Router);
export default new Router({
  routes,
  mode: 'history'
})