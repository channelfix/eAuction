import Vue from 'vue'
import Router from 'vue-router'
import LogIn from '@/components/LogIn'
import Home from '@/components/Home'
import ErrorPage from '@/components/ErrorPage'
import PagesNavigation from '@/components/PagesNavigation'
import Profile from '@/components/Profile'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
	    path: '',
        name: 'LogIn',
        component: LogIn
    },{
    	path: '/menu',
    	component: PagesNavigation,
      props: true,
      children: [
        {
          path: 'home',
          name: 'Home',
          props: true,
          component: Home,
        },{
          path: 'profile',
          name: 'Profile',
          props: true,
          component: Profile
        }
      ],
    },{
      path: '*',
      name: '404',
      component: ErrorPage,
    }
  ]
})
