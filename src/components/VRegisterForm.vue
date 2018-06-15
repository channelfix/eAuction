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
				  v-model="user.fname"
				  required
				  :rules="fnameRules"
				></v-text-field>
			</v-flex>
			<v-flex lg5>
				<v-text-field
				  label="Last Name"
				  id="ln"
				  v-model="user.lname"
				  required
				  :rules="lnameRules"
				></v-text-field>
			</v-flex>
		</v-layout>

		<v-text-field
		  label="Username"
		  id="un"
		  v-model="user.name"
		  required
		  :rules="unameRules"
		></v-text-field>
		<v-text-field
		  label="Email"
		  id="em"
		  v-model="user.email"
		  required
		  :rules="emailRules"
		></v-text-field>
		<v-text-field
		  required
		  name="pass"
		  label="Password"
		  id="ps"
		  hint="At least 8 characters"
		  v-model="user.password"
		  :append-icon="iconVis ? 'visibility' : 'visibility_off'"
		  :append-icon-cb="() => (iconVis = !iconVis)"
		  :type="iconVis ? 'password': 'text'"
		  min="8"
		></v-text-field>
		<v-text-field
		  :error="err"
		  required
		  v-model="user.cpassword"
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
					name: "",
					password:"",
					cpassword:"",
					fname:"",
					lname:"",
					email:"",
				},
				visible: false,
				valid: false,
				iconVis: true,
				alert: false,
				checkVar: true,
				fnameRules: [
					v => !!v || 'First name is required',
      				v => /^\w+/.test(v) || "Field shouldn't start with symbols"
				],
				lnameRules: [
					v => !!v || 'Last name is required',
      				v => /^\w+/.test(v) || "Field shouldn't start with symbols"
				],
				unameRules: [
					v => !!v || 'Username is required',
      				v => /^\w+/.test(v) || "Field shouldn't start with symbols"
				],
				emailRules: [
			      	v => !!v || 'E-mail is required',
			      	v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
			    ],
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
			err(){
				if(this.user.password == this.user.cpassword){
					return false;
				} else {
					this.valid = false;
					return true;
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