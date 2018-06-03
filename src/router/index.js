import Vue from 'vue'
import Router from 'vue-router'
import LogIn from '@/components/LogIn'
import Home from '@/components/Home'
import ErrorPage from '@/components/ErrorPage'
import PagesNavigation from '@/components/PagesNavigation'
import Profile from '@/components/Profile'
import Auctioneer from '@/components/Auctioneer'
import Bidder from '@/components/Bidder'
import EditProfile from '@/components/EditProfile'
import CreateLiveStream from '@/components/CreateLiveStream'
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
        },{
          path: '/create-auction',
          name: 'Create-Live',
          component: CreateLiveStream,
        }
      ],
    },

    {
      path: '/auctioneer/:id',
      name: 'Auctioneer',
      component: Auctioneer
    },
    {
      path: '/bidder/:id',
      name: 'Bidder',
      component: Bidder
    },
    {
      path: '*',
      name: '404',
      component: ErrorPage,
    }
  ]
})
