<template>	
	<v-form class="form">
		<v-alert v-model="alert" type="error" transition="slide-y-transition" dismissible>
	    	Incorrect username or password!
	    </v-alert>
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
				alert: false,
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
				request.post('/login/', formData, 
					(response) => {
						if(response instanceof Error){
							this.alert = true
						}else {
							this.$store.commit('authenticated', true)	
							this.$store.commit('setUsername', this.user.name)
							this.$store.commit('asAuctioneer', response.data.isAuctioneer)				
							this.$store.commit('addCredits', response.data.credits)
							this.$router.push({
								name: 'Home',
								params: {
									username: this.user.name,
								}
							});
						}
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