<template>
	<v-container fluid>
		<v-layout row wrap fill-height>
		  	<v-flex lg7>
				<v-layout align-center justify-center fill-height>
					<div>
						<p class="text-lg-left display-4">eAuction</p>
						<p class="text-lg-left headline">eAuction eAuction eAuction eAuction eAuction</p>
						<p class="text-lg-left headline">eAuction eAuction eAuction eAuction eAuction eAuction</p>
						<p class="text-lg-left headline">eAuction eAuction eAuction eAuction eAuction eAuction eAuction</p>
						<p class="text-lg-left headline">eAuction eAuction eAuction eAuction eAuction eAuction eAuction eAuction</p>
		  			</div>
		  		</v-layout>
		  	</v-flex>
		  	<v-flex lg5 class="right amber darken-3">
				<v-layout row wrap>
					<v-flex lg6 >
						<v-btn 
							depressed
							flat
							block
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
							block
							:ripple="false"
							@click="isRegister = true" 
							:class="{'amber darken-3': isRegister, 'yellow darken-3': !isRegister}"
						>
							Register
						</v-btn>
					</v-flex>
				</v-layout>
				<component :is="form">
				</component>
		  	</v-flex>
		</v-layout>
	</v-container>
</template>

<script>
	import loginForm from './login/loginForm';
	import registerForm from './login/registerForm';

	export default {
		data(){
			return {
				email: "",
				isRegister: false,
				confirmMatch: true,
			};
		},
		components: {
			loginForm, registerForm
		},
		computed: {
			form: function(){
				if(this.isRegister){
					return registerForm;
				}else{
					return loginForm;
				}
			}
		},
		watch: {
			isRegister: function(){
				console.log(this.isRegister);
			}
		},
	}
</script>

<style lang="scss" scoped>

	button {
		padding: 0;
		margin: 0;
		height: 5em;
	}

</style>
