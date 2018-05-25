<template>
	<v-form class="form">
		<v-layout row wrap justify-space-between>
			<v-flex lg5>
				<v-text-field
				  name="fname"
				  label="Firstname"
				  id="fn"
				  v-model="user.fname"
				></v-text-field>
			</v-flex>
			<v-flex lg5>
				<v-text-field
				  name="lname"
				  label="Last Name"
				  id="ln"
				  v-model="user.lname"
				></v-text-field>
			</v-flex>
		</v-layout>

		<v-text-field
		  name="user"
		  label="Username"
		  id="un"
		  v-model="user.name"
		></v-text-field>
		<v-text-field
		  name="email"
		  label="Email"
		  id="em"
		  v-model="user.email"
		></v-text-field>
		<v-text-field
		  name="pass"
		  label="Password"
		  id="ps"
		  v-model="user.password"
		></v-text-field>
		<v-text-field
		  name="confirmpass"
		  label="Confirm Password"
		  id="cps"
		></v-text-field>
		<v-btn @click="register">Submit</v-btn>
	</v-form>
</template>

<script>
	import Request from '../assets/js/Request'

	export default {
		name: 'registerForm',
		data() {
			return {
				user: {
					name: "",
					password:"",
					fname:"",
					lname:"",
					email:"",
				},
				visible: false,
			}
		},
		methods: {
			register: function(){
				let request = new Request();
				let formData = new FormData();


				formData.set('username', this.user.name);
				formData.set('password', this.user.password);
				formData.set('email', this.user.email);
				formData.set('firstname', this.user.fname);
				formData.set('lastname', this.user.lname);

				request.post('http://localhost:8000/','register/', formData, 
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