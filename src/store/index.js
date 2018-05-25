import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isAuthenticated: false,
    username: ''
  },

  mutations: {
  	authenticated: (state, auth) => state.isAuthenticated = auth,
    setUsername: (state, username) => state.username = username
  },

  actions: {

  },

  getters: {
    getUsername: (state) => {
        return state.username
    }
  }

})

