<template>
	<div class="md-layout md-gutter">
		<div class=" md-layout-item md-layout md-alignment-center-center">
			<span class=" title">eAuction</span>

		</div>
		<div class="md-layout-item md-layout md-alignment-center-center md-gutter">
				<div class="loginbox md-elevation-2 loginbox md-layout-item">
					<div v-show="isRegister" class="md-layout">
						<span>Register</span>
						<md-field>
							<label>Email</label>
							<md-input v-model="password" @keyup.enter="login"></md-input>
						</md-field>
						<md-field>
						<label>Username</label>
						<md-input v-model="username" @keyup.enter="login"></md-input>
						</md-field>
						<md-field>
							<label>Password</label>
							<md-input v-model="password" @keyup.enter="login"></md-input>
						</md-field>
						<md-field>
							<label>Confirm Password</label>
							<md-input v-model="password" @keyup.enter="login"></md-input>
						</md-field>
					</div>
					<div v-show="!isRegister" class="md-layout">
						<span>Log In</span>
						<md-field>
						<label>Username</label>
						<md-input v-model="username" @keyup.enter="login"></md-input>
						</md-field>
						<md-field>
							<label>Password</label>
							<md-input v-model="password" @keyup.enter="login"></md-input>
						</md-field>
					</div>

					<md-button @click="login" class="md-raised">Log In</md-button>
					<md-button @click="login" class="md-raised">Register</md-button>
				</div>
		</div>
	</div>
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
			login:function(){
				let username = "bojoluis";
				let password = "1234";

				let oReq = new XMLHttpRequest();
				let isValid = {};

				oReq.onreadystatechange = function() {
			        if (this.readyState == 4 && this.status == 200) {
			            isValid = JSON.parse(this.responseText);
			    
			            if(isValid.isValid){
							alert("Valid");
						}else{
							alert("Wrong");
						}
			       }
			    };

				oReq.open("GET", "http://localhost:8000/login/test/?name=bojoluis&password=1234");
				oReq.send();
				console.log(oReq);

				
			}
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
