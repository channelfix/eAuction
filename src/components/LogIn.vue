<template>
	<v-container fluid>
		<v-layout row wrap>
		  	<v-flex lg7>
		  		<v-layout justify-space-around row class="box intro">
					<span class="title">eAuction</span>
		  		</v-layout>
		  	</v-flex>
		  	<v-flex lg5>
		  	 	
		  	</v-flex>
		</v-layout>
	</v-container>
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
	.intro {
		padding: 10em;
	}
	.title {
		font-size: 20em;
	}
</style>
