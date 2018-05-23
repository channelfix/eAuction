import Vue from 'vue'
import Vuex from 'vuex'
import Request from '../assets/js/Request.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isAuthenticated: false,
    username: '',
    biography: '',
    email: '',
    lastname: '',
    firstname: '',
    avatar: '',
    tags: '',
    isAuctioneer: true
  },

  mutations: {
  	authenticated: (state, auth) => state.isAuthenticated = auth,
    setUsername: (state, username) => state.username = username,
    setBiography: (state, biography) => state.biography = biography,
    setEmail: (state, email) => state.email = email,
    setLastName: (state, lastname) => state.lastname = lastname,
    setFirstName: (state, firstname) => state.firstname = firstname,
    setProfilePic: (state, image) => state.avatar = image,
    setTags: (state, tags) => state.tags = tags,
    asAuctioneer: (state, asAuct) => state.isAuctioneer = asAuct
  },

  actions: {
   setProfile(context, username) {

      let request = new Request();
      let formdata = new FormData();
      

      formdata.set('username', username);

      request.post('http://localhost:8000/','profile/request_profile_details/', formdata,
      (response) => {
        
        let userDetails = response.data

        context.commit('setUsername', userDetails.username)
        context.commit('setBiography', userDetails.biography)
        context.commit('setEmail', userDetails.email)
        context.commit('setLastName', userDetails.last_name)
        context.commit('setFirstName', userDetails.first_name)
        context.commit('setProfilePic', userDetails.avatar)
        context.commit('setTags', userDetails.tags)
        context.commit('asAuctioneer', userDetails.isAuctioneer)
      },);
    },
    setUsername: (context, username) => {
      context.commit('setUsername', username)
    }
  },

  getters: {
    getUsername: (state) => { return state.username },
    getBiography: (state) => { return state.biography },
    getEmail: (state) => { return state.email },
    getLastName: (state) => { return state.lastname },
    getFirstName: (state) => { return state.firstname },
    getProfilePic: (state) => { return state.avatar },
    getTags: (state) => { return state.tags },
    getAuctioneer: (state) => { return state.isAuctioneer }
  }

})

