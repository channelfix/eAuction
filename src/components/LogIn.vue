<template>
	<v-container fluid>
		<v-layout row wrap fill>
		  	<v-flex lg7 class="intro">
				<p class="text-lg-left display-4">eAuction</p>
				<p class="text-lg-left headline">eAuction eAuction eAuction eAuction eAuction</p>
				<p class="text-lg-left headline">eAuction eAuction eAuction eAuction eAuction eAuction</p>
				<p class="text-lg-left headline">eAuction eAuction eAuction eAuction eAuction eAuction eAuction</p>
				<p class="text-lg-left headline">eAuction eAuction eAuction eAuction eAuction eAuction eAuction eAuction</p>
		  	</v-flex>
		  	<v-flex lg5 class="right amber darken-3">
				<v-layout row wrap>
					<v-flex lg6 >
						<v-btn 
							depressed
							flat
							:ripple="false"
							@click="isRegister = false"
							:class="{'amber darken-3': !isRegister, 'yellow darken-3': isRegister}"
						>
							Log In
						</v-btn>
					</v-flex>
					<v-flex lg6 >
						<v-btn 
							depressed 
							flat
							:ripple="false"
							@click="isRegister = true" 
							:class="{'amber darken-3': isRegister, 'yellow darken-3': !isRegister}"
						>
							Register
						</v-btn>
					</v-flex>
				</v-layout>
				<loginForm v-show="!isRegister"></loginForm>
				<registerForm v-show="isRegister"></registerForm>
		  	</v-flex>
		</v-layout>
	</v-container>
</template>

<script>
	import loginForm from './loginForm';
	import registerForm from './registerForm';

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
		components: {
			loginForm, registerForm
		},
		watch: {
			isRegister: function(){
				console.log(this.isRegister);
			}
		},
	}
</script>

<style lang="scss" scoped>
	.intro {
		padding: 2em;
		padding-top: 15em;
	}


	button {
		width: 100%;
		height: 5em;
		margin: 0;
	}
</style>
