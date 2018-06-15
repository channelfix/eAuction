<template>
	<v-form class="form" ref="form" lazy-validation>
		<v-alert v-model="alert" type="error" transition="slide-y-transition" dismissible>
		    	There was a problem in the server
	    </v-alert>
	    <v-alert v-model="success" type="success" transition="slide-y-transition" dismissible>
		    	Registered Successfully! Redirecting you to Sign In
	    </v-alert>
		<v-layout row wrap justify-space-between>
			<v-flex lg5>
				<v-text-field
				  @keyup.enter="register"
				  label="Firstname"
				  id="fn"
				  v-model="user.fname.text"
				  required
				  :rules="user.fname.rules"
				></v-text-field>
			</v-flex>
			<v-flex lg5>
				<v-text-field
				 @keyup.enter="register"
				  label="Last Name"
				  id="ln"
				  v-model="user.lname.text"
				  required
				  :rules="user.lname.rules"
				></v-text-field>
			</v-flex>
		</v-layout>
		<v-text-field
		  @keyup.enter="register"
		  label="Username"
		  id="un"
		  v-model="user.name.text"
		  required
		  :rules="user.name.rules"
		></v-text-field>
		<v-text-field
	      @keyup.enter="register"
		  label="Email"
		  id="em"
		  v-model="user.email.text"
		  required
		  :rules="user.email.rules"
		></v-text-field>
		<v-text-field
		  @keyup.enter="register"
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
		  @keyup.enter="register"
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
		<v-btn :disabled="valid" @click="register">Submit</v-btn>
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
							v => this.user.name.valid = (v!='') || 'Username is required',
      						v => this.user.name.valid = /^\w+/.test(v) || "Field shouldn't start with symbols"
						]
					},
					password: {
						text: "",
						valid: false,
						rules: [
							v => this.user.password.valid = (v!='') || 'Password is required',
      						v => this.user.password.valid = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/.test(v) || "Minimum eight characters, at least one letter and one number"
						]
					},
					cpassword: {
						text: "",
						valid: false,
						rules: [
							v => this.user.cpassword.valid = (v!='') || 'Confirm Password is required',
      						v => this.user.cpassword.valid = (v!='' && v == this.user.password.text) || "Password doesn't match"
						]	
					},
					fname: {
						text: "",
						valid: false,
						rules: [
							v => this.user.fname.valid = (v!='') || 'First name is required',
      						v => this.user.fname.valid = /([A-Z][a-z]*)([\\s\\\'-][A-Z][a-z]*)*/.test(v) || "First name can only contain alphabetical characters and ,.`- Must start with capital letter"
						]
					},
					lname: {
						text: "",
						valid: false,
						rules: [
							v => this.user.lname.valid = (v!='') || 'Last name is required',
      						v => this.user.lname.valid = /([A-Z][a-z]*)([\\s\\\'-][A-Z][a-z]*)*/.test(v) || "Last name can only contain alphabetical characters and ,.`- Must start with capital letter"
						],
					},
					email: {
						text: "",
						valid: false,
						rules: [
							v => this.user.email.valid = (v!='') || 'Email is required',
      						v => this.user.email.valid = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid. e.g user@example.com'
						],	
					},
				},
				visible: false,
				iconVis: true,
				alert: false,
				checkVar: true,
				submitLoading: false,
				success: false,
			}
		},
		methods: {
			register(){
				this.submitLoading = true;


				let request = new Request();
				let formData = new FormData();

				formData.set('username', this.user.name.text);
				formData.set('password', this.user.password.text);
				formData.set('email', this.user.email.text);
				formData.set('firstname', this.user.fname.text);
				formData.set('lastname', this.user.lname.text);

				request.post('/register/', formData, 
					(response)=> {
						// process response from server
						this.submitLoading = false;
						if(response instanceof Error){
							this.alert = true;
						}else{
							this.success = true;
							let thread = setTimeout(()=>{
								this.$parent.activeForm = 'VLoginForm';
							}, 2000)

						}
					}
				);	



			},
			clear() {
				this.user.name.text = "";
				this.user.password.text = "";
				this.user.cpassword.text = "";
				this.user.fname.text = "";
				this.user.lname.text = "";
				this.user.email.text = "";
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