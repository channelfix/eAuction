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
			}
		}

	}
</script>

<style scoped>
	.login {
		padding: 2em;
	}
</style>