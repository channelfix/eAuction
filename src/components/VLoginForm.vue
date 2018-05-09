<template>
	<v-form class="login">
		<v-text-field
		  name="name"
		  label="Username"
		  v-model="user.name"
		></v-text-field>
		<v-text-field
		  name="name"
		  label="Password"
		  v-model="user.password"
		  :append-icon="visible ? 'visibility_off': 'visibility'"
          :append-icon-cb="() => (visible = !visible)"
          :type="visible ? 'text': 'password' "
		></v-text-field>
		<v-btn @click="login">Submit</v-btn>
	</v-form>
</template>

<script>
	import Request from '../assets/js/Request'

	export default {
		name: 'loginForm',
		data() {
			return {
				user: {
					name: "",
					password:"",
				},
				visible: false,
			}
		},
		methods: {
			login: function(){
				let request = new Request();

				let response = request.post('http://localhost:8000/login/','accounts/',this.user);				
			}
		}
	}
</script>

<style scoped>
	.login {
		padding: 2em;
	}
</style>