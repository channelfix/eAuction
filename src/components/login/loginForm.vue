<template>
	<v-form class="login">
		<v-text-field
		  name="name"
		  label="Username"
		  id="id"
		  v-model="name"
		></v-text-field>
		<v-text-field
		  name="name"
		  label="Password"
		  id="id"
		  v-model="password"
		  :append-icon="visible ? 'visibility_off': 'visibility'"
          :append-icon-cb="() => (visible = !visible)"
          :type="visible ? 'text': 'password' "
		></v-text-field>
		<v-btn @click="login">Submit</v-btn>
	</v-form>
</template>

<script>
	import axios from 'axios'
	import Cookies from 'js-cookie'
	export default {
		name: 'loginForm',
		data() {
			return {
				name: "",
				password: "",
				visible: false,
			}
		},
		methods: {
			login: function(){
				
			}
		}
	}
</script>

<style scoped>
	.login {
		padding: 2em;
	}
</style>