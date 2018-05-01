<template>
</template>

<script>
	export default {
		data(){
			return {
				username: "",
				password: "",
				email: "",
				isRegister: false,
				confirmMatch: true,
			};
		},
		methods: {
			login(){
				console.log("test");
			},
		},
		calculated: {
		}

	}
</script>

<style scoped>
	.title {
		font-size: 5em;
	}
	.loginbox {
		margin: 5%;
		margin-top: 7%;
		padding: 5%;
	}
	.desc {
		text-align: center;
	}
</style>
