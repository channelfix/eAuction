<template>
	<form>
		<input type="file" id="fileSelector" v-on:change="updateImageDisplay">
		
		<div id="profile" v-if="" />
			<img :src="profilePic" />
		</div>

		<p class='usernameProperty'>
			<label>Username:</label>
			<input type="text" id="usernameField" v-model="username">
		</p>

		<p class="passwordProperty">
			<label>Password:</label>
			<input type="text" id="passwordField">
		</p>


		<p class='lastNameProperty'>
			<label>Last Name:</label>
			<input type="text" id="lastNameField" v-model="lastName">
		</p>

		<p class='firstNameProperty'>
			<label>First Name:</label>
			<input type="text" id="firstNameField" v-model="firstName">
		</p>


		<p class="emailProperty">
			<label>Email:</label>
			<input type="text" id="emailField" v-model="email">
		</p>


		<p class="biograpyProperty">
			<label>Biography:</label><br>
			<textarea
				id = "biographyField"
				rows="3"
				cols="80"
				placeholder="Description here."
				v-model="biography"
			>.				
			</textarea>
		</p>

		<input type="button" id="changeButton" value="Change" v-on:click="changeProfile">
		<input type="button" id="cancelButton" value="Cancel">

	</form>
</template>

<script type="text/javascript">
	import Request from '../assets/js/Request.js';

	export default{	
		name: 'EditProfile',
		props: {
			username: String,
		},
		data() {
			return {
				userProfile: '',
				profilePic: '',
				lastName: '',
				firstName: '',
				email: '',
				biography: '',
				userName: '',
			}
		},
		computed: {
			hasProfilePic() {
				return profilePic.length > 0
			}
		},
		methods: {
			updateImageDisplay: function(e) {
				var imageFile = e.target.files;
				if(imageFile.length == 1){
					if(this.isValidImageFormat(imageFile[0]))
						this.profilePic = window.URL.createObjectURL(imageFile[0])
					else
						alert('Cannot import this file. Use only this following format (jpg, jpeg, and png).')
				}
				else
					alert('No image selected');
			},
			isValidImageFormat: function(imageFile) {
				if(imageFile.type === 'image/jpg' || imageFile.type === 'image/png' || imageFile.type === 'image/jpeg')
					return true;
			},
			changeProfile: function() {
				let request = new Request();
				let formdata = new FormData();

				alert(this.username)
			}
		},
		mounted: function() {
			let request = new Request();
			let formdata = new FormData();

			formdata.set('username', this.username);

			request.post('http://localhost:8000/', 'profile/request_profile_details/', formdata,
				(response) => {
					this.userProfile = response.data;

					this.profilePic = this.userProfile.avatar;
					this.userName = this.userProfile.username;
					this.lastName = this.userProfile.last_name;
					this.firstName = this.userProfile.first_name;
					this.email = this.userProfile.email;
					this.biography = this.userProfile.biography;
				}
			);	
		}
	}

</script>

<style>
	
</style>