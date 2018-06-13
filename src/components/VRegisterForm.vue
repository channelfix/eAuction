<template>
	<v-form class="form" ref="form" v-model="valid" lazy-validation>
		<v-alert v-model="alert" type="error" transition="slide-y-transition" dismissible>
		    	Please fill in form promptly
		    </v-alert>
		<v-layout row wrap justify-space-between>
			<v-flex lg5>
				<v-text-field
				  label="Firstname"
				  id="fn"
				  v-model="user.fname.text"
				  required
				  :rules="user.fname.rules"
				></v-text-field>
			</v-flex>
			<v-flex lg5>
				<v-text-field
				  label="Last Name"
				  id="ln"
				  v-model="user.lname.text"
				  required
				  :rules="user.lname.rules"
				></v-text-field>
			</v-flex>
		</v-layout>

		<v-text-field
		  label="Username"
		  id="un"
		  v-model="user.name.text"
		  required
		  :rules="user.name.rules"
		></v-text-field>
		<v-text-field
		  label="Email"
		  id="em"
		  v-model="user.email.text"
		  required
		  :rules="user.email.rules"
		></v-text-field>
		<v-text-field
		  required
		  name="pass"
		  label="Password"
		  id="ps"
		  hint="At least 8 characters"
		  :rules="user.password.rules"
		  v-model="user.password.text"
		  :append-icon="iconVis ? 'visibility' : 'visibility_off'"
		  :append-icon-cb="() => (iconVis = !iconVis)"
		  :type="iconVis ? 'password': 'text'"
		  min="8"
		></v-text-field>
		<v-text-field
		  :rules="user.cpassword.rules"
		  required
		  v-model="user.cpassword.text"
		  name="confirmpass"
		  label="Confirm Password"
		  :append-icon="iconVis ? 'visibility' : 'visibility_off'"
		  :append-icon-cb="() => (iconVis = !iconVis)"
		  :type="iconVis ? 'password': 'text'"
		  min="8"
		  id="cps"
		></v-text-field>
		<v-btn :disabled="!valid" @click="register">Submit</v-btn>
		<v-btn @click="clear()">clear</v-btn>
	</v-form>
</template>

<script>
	import Request from '../assets/js/Request'

	export default {
		name: 'registerForm',
		data() {
			return {
				user: {
					name: {
						text: "",
						valid: false,
						rules: [
							v => this.user.name.valid = !!v || 'Username is required',
      						v => this.user.name.valid = /^\w+/.test(v) || "Field shouldn't start with symbols"
						]
					},
					password: {
						text: "",
						valid: false,
						rules: [
							v => this.user.password.valid = !!v || 'Password is required',
      						v => this.user.password.valid = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/.test(v) || "Minimum eight characters, at least one letter and one number"
						]
					},
					cpassword: {
						text: "",
						valid: false,
						rules: [
							v => this.user.cpassword.valid = !!v || 'Confirm Password is required',
      						v => this.user.cpassword.valid = (this.user.cpassword.text == this.user.password.text) || "Minimum eight characters, at least one letter and one number"
						]	
					},
					fname: {
						text: "",
						valid: false,
						rules: [
							v => this.user.fname.valid = !!v || 'First name is required',
      						v => this.user.fname.valid = /([A-Z][a-z]*)([\\s\\\'-][A-Z][a-z]*)*/.test(v) || "First name can only contain alphabetical characters and ,.`- Must start with capital letter"
						]
					},
					lname: {
						text: "",
						valid: false,
						rules: [
							v => this.user.lname.valid = !!v || 'Last name is required',
      						v => this.user.lname.valid = /([A-Z][a-z]*)([\\s\\\'-][A-Z][a-z]*)*/.test(v) || "Last name can only contain alphabetical characters and ,.`- Must start with capital letter"
						],
					},
					email: {
						text: "",
						valid: false,
						rules: [
							v => this.user.email.valid = !!v || 'Email is required',
      						v => this.user.email.valid = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid. e.g user@example.com'
						],	
					},
				},
				visible: false,
				iconVis: true,
				alert: false,
				checkVar: true,
			}
		},
		methods: {
			register(){
				let request = new Request();
				let formData = new FormData();

				formData.set('username', this.user.name);
				formData.set('password', this.user.password);
				formData.set('email', this.user.email);
				formData.set('firstname', this.user.fname);
				formData.set('lastname', this.user.lname);

				for(let data of formData.values()){
					if(data == ""){
						this.alert = true;
						return
					}
				}

				request.post('/register/', formData, 
					(response)=> {
						// process response from server
					}
				);	
			},
			clear() {
				this.user.name = "";
				this.user.password = "";
				this.user.cpassword = "";
				this.user.fname = "";
				this.user.lname = "";
				this.user.email = "";
				this.valid = false;
			},
		},
		computed:{
			valid(){
				if(
					this.user.name.valid == true && 
					this.user.fname.valid == true &&
					this.user.lname.valid == true &&
					this.user.email.valid == true &&
					this.user.password.valid == true &&
					this.user.cpassword.valid == true 
				){
					return true;
				} else {
					return false;
				}
			},
		}
	}
</script>

<style scoped>
	.form {
		padding: 2em;
	}
</style>