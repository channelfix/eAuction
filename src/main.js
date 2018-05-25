// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuex from 'vuex'
import App from './App'
import router from './router'
import store from './store'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import colors from 'vuetify/es5/util/colors'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

Vue.use(Vuetify, {
  theme: {
    primary: colors.amber.lighten5, // #E53935
    secondary: colors.amber.lighten1, // #FFCDD2
    accent: colors.amber.accent1 // #3F51B5
  }
});

Vue.config.productionTip = false

store.commit('authenticated', window.__INITIAL_STATE__.isAuthenticated)
//store username
router.beforeEach((to, from, next) => {
  let isAuth = store.state.isAuthenticated;
  if (to.name === 'LogIn' && isAuth) return next('/menu/profile/'+to.params.username) 
  if (!to.meta) return next()
  if (!to.meta.isAuthRequired) return next()
  if (to.meta.isAuthRequired && isAuth) return next()
  return next('/')
})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
