<template>
	<v-form class="login">
		<v-text-field
		  name="fname"
		  label="Firstname"
		  id="fn"
		></v-text-field>
		<v-text-field
		  name="lname"
		  label="Last Name"
		  id="ln"
		></v-text-field>
		<v-text-field
		  name="user"
		  label="Username"
		  id="un"
		></v-text-field>
		<v-text-field
		  name="email"
		  label="Email"
		  id="em"
		></v-text-field>
		<v-text-field
		  name="pass"
		  label="Password"
		  id="ps"
		></v-text-field>
		<v-btn>Submit</v-btn>
	</v-form>
</template>

<script>
	export default {
		name: 'registerForm',
	}
</script>

<style scoped>
	.login {
		padding: 2em;
	}
</style>