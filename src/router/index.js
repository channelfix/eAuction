import Vue from 'vue'
import Router from 'vue-router'
import LogIn from '@/components/LogIn'
import Home from '@/components/Home'
import ErrorPage from '@/components/ErrorPage'
import PagesNavigation from '@/components/PagesNavigation'
import Profile from '@/components/Profile'
import Auction from '@/components/Auction'
import EditProfile from '@/components/EditProfile'
import store from '../store'

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
      children: [
        {
          path: 'home',
          name: 'Home',
          component: Home,
        },{
          path: 'profile/:username',
          name: 'Profile',     
          component: Profile,
        },{
          path: 'edit-profile',
          name: 'Edit-Profile',
          component: EditProfile
        },
      ],
    },
    {
          path: '/auction/:id',
          name: 'Auction',
          component: Auction,
        },
    {
      path: '*',
      name: '404',
      component: ErrorPage,
    }
  ]
})
