<template>
	<v-form class="form">
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
				let formData = new FormData();

				formData.set('username', this.user.name);
				formData.set('password', this.user.password);
				
				request.post('http://localhost:8000/login/','accounts/', formData, 
					function(response) {
						// process response from server
					}
				);	
			}
		}
	}
</script>

<style scoped>
	.form {
		padding: 2em;
	}
</style>