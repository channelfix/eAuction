<template>
	<v-form class="login">
		<v-text-field
		  name="name"
		  label="Username"
		  id="id"
		  v-model="username"
		></v-text-field>
		<v-text-field
		  name="name"
		  label="Password"
		  id="id"
		  v-model="password"
		></v-text-field>
		<v-btn @click="login">Submit</v-btn>
	</v-form>
</template>

<script>
	export default {
		name: 'loginForm',
		data() {
			return {
				username: "",
				password: "",
			}
		},
		methods: {
			login: function(){
				console.log(this.username, this.password);
				let xhr = new XMLHttpRequest();

				xhr.onreadystatechange = function(){
					  if(xhr.readyState === 4 && xhr.status === 200) {
					    console.log(xhr.responseText);
					  }
				}

				xhr.open('POST', 'https://localhost:8000/login/test/', true);
				xhr.send("name="+this.username+"&password="+this.password);
			}
		}

	}
</script>

<style scoped>
	.login {
		padding: 2em;
	}
</style>