<template>
	<v-container fluid>
		<v-layout 
			row wrap 
			fill-height
		>
		  	<v-flex lg7>
				<v-layout 
					align-center 
					justify-center
					 fill-height
				 >
					<div>
						<p class="text-lg-left display-4">eAuction</p>
						<p class="text-lg-left headline">eAuction eAuction eAuction eAuction eAuction</p>
						<p class="text-lg-left headline">eAuction eAuction eAuction eAuction eAuction eAuction</p>
						<p class="text-lg-left headline">eAuction eAuction eAuction eAuction eAuction eAuction eAuction</p>
						<p class="text-lg-left headline">eAuction eAuction eAuction eAuction eAuction eAuction eAuction eAuction</p>
		  			</div>
		  		</v-layout>
		  	</v-flex>
		  	<v-flex 
		  		lg5 
		  		class="right amber darken-3"
	  		>
				<v-layout 
					row
					wrap
				>
					<v-flex lg6>
						<v-btn 
							depressed
							flat
							block
							:ripple="false"
							@click="activeForm = 'VRegisterForm'"
							:class="registerButtonStyle"
						>
							Sign Up
						</v-btn>
					</v-flex>
					<v-flex lg6 >
						<v-btn 
							depressed
							flat
							block
							:ripple="false"
							@click="activeForm = 'VLoginForm'" 
							:class="loginButtonStyle"
						>
							Sign In
						</v-btn>
					</v-flex>
				</v-layout>
				<component :is="activeForm">
				</component>
		  	</v-flex>
		</v-layout>
	</v-container>
</template>

<script>
	import VLoginForm from './VLoginForm';
	import VRegisterForm from './VRegisterForm';

	export default {
		name: "LogIn",
		data(){
			return {
				activeForm: 'VRegisterForm',
			}
		},
		components: {
			VLoginForm, VRegisterForm
		},
		computed: {
			loginButtonStyle(){
				let style = {
					'amber darken-3' : false,
					'yellow darken-3': true,
				}
				if(this.activeForm == 'VLoginForm'){
					style['amber darken-3'] = true;
					style['yellow darken-3'] = false;
				}
				return style;
			},
			registerButtonStyle(){
				let style = {
					'amber darken-3' : false,
					'yellow darken-3': true,
				}
				if(this.activeForm == 'VRegisterForm'){
					style['amber darken-3'] = true;
					style['yellow darken-3'] = false;
				}
				return style;
			}
		}
	}
</script>

<style lang="scss" scoped>

	button {
		padding: 0;
		margin: 0;
		height: 5em;
	}

</style>
