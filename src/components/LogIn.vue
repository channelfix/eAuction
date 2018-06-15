<template>
	<v-container fluid>
		<v-layout 
			row wrap 
			fill-height
		>
		  	<v-flex 
		  		pa-3
		  		lg7
		  	>
				<v-layout 
					align-center 
					justify-center
					fill-height
				 >
					<v-layout
						column
					>
						<img 
							class="img"
							src="https://image.flaticon.com/icons/png/512/186/186337.png"
						/>
						<p class="text-lg-left display-4 titleText">eAuction</p>
						<p elevation-20 class="text-lg-left headline titleText"><i>A web platform that brings traditional auctioning to a modern online system, coupled with tools that’s necessary for the auctioning process</i></p>
		  			</v-layout>
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

<style scoped>
	@import url('https://fonts.googleapis.com/css?family=Raleway:300i,600');

	button {
		padding: 0;
		margin: 0;
		height: 5em;
	}

	.img {
		height: 250px;
		width: 250px;
	}

	.titleText {
		padding: 10px;
		font-family: 'Raleway', sans-serif;
	}

</style>
