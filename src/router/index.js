import Vue from 'vue'
import Router from 'vue-router'
import LogIn from '@/components/LogIn'
import Home from '@/components/Home'
import ErrorPage from '@/components/ErrorPage'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
	    path: '',
        name: 'LogIn',
        component: LogIn
    },
    {
    	path: '/home',
    	name: 'Home',
    	component: Home,
    },
    {
      path: '*',
      name: '404',
      component: ErrorPage,
    }
  ]
})
