<template>
	<v-form class="login">
		<v-text-field
		  name="name"
		  label="Username"
		  id="id"
		></v-text-field>
		<v-text-field
		  name="name"
		  label="Password"
		  id="id"
		></v-text-field>
		<v-btn>Submit</v-btn>
	</v-form>
</template>

<script>
	export default {
		name: 'loginForm',
	}
</script>

<style scoped>
	.login {
		padding: 2em;
	}
</style>