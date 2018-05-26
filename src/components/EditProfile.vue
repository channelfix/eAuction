<template>
	<form>
		<input type="file" id="fileSelector" v-on:change="updateImageDisplay" />
		
		<div id="profile"/>
			<img :src="profilePic" width="200" height="200" />
		</div>

		<p>
			<label>Old Password:</label>
			<input type="password" id="oldPasswordField" v-model="oldPassword">
		</p>

		<p>
			<label>New Password:</label>
			<input type="password" id="newPasswordField" v-model="newPassword">
		</p>

		<p>
			<label>Confirm Password:</label>
			<input type="password" id="confirmedPasswordField" v-model="confirmPassword">
			<label v-if="hasMatchPassword">matched password</label>
			<label v-else="hasMatchPassword">password does not match.</label>
		</p>
		<v-btn
			@click="changePassword"
		>Change Password</v-btn>

		<p class='lastNameProperty'>
			<label>Last Name:</label>
			<input type="text" id="lastNameField" v-model="lastName">

			<label v-if="lastName != ''">filled</label>
			<label v-else>this field is empty</label>
		</p>

		<p class='firstNameProperty'>
			<label>First Name:</label>
			<input type="text" id="firstNameField" v-model="firstName">

			<label v-if="firstName != ''">filled</label>
			<label v-else>this field is empty</label>
		</p>


		<p class="emailProperty">
			<label>Email:</label>
			<input type="text" id="emailField" v-model="email">

			<label v-if="email != ''">filled</label>
			<label v-else>this field is empty</label>
		</p>

		<div v-if="isAuctioneer">
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
		</div> 


		<div v-if="isAuctioneer">
			<p class="tagsProperty">
				<label>Tags:</label>
				<input type="text" v-model="tag" placeholder="Tags here" size="10" v-on:keyup.enter="addTag">	
				<button @click.prevent="addTag">+</button>
				<button @click.prevent="removeTag">-</button>
			</p>
		</div>

		<input type="button" id="changeButton" value="Change" v-on:click="changeProfile">

	</form>
</template>

<style>
	html{
		overflow: auto;
	}
</style>

<script type="text/javascript">
	import Request from '../assets/js/Request.js';

	export default{	
		name: 'EditProfile',
		data() {
			return {
				username: this.$store.getters.getUsername,
				userProfile: '',
				profilePic: '',
				lastName: '',
				firstName: '',
				email: '',
				biography: '',
				tags: [],
				tag: '',
				oldPassword: '',
				newPassword: '',				
				confirmPassword: '',
				imageFile: '',
				hasChangePic: false,
				matchedPassword: false,
				isAuctioneer: false
			}
		},
		computed: {
			hasMatchPassword() {
				if(this.newPassword === this.confirmPassword){
					this.matchedPassword = true
					return true;
				}
			},
		},
		methods: {
			hasNotFilled(field) {
				if(field != '')
					return true;
			},
			isValidImageFormat: function(selectedFile) {
				if(selectedFile.type === 'image/jpg' || selectedFile.type === 'image/png' || selectedFile.type === 'image/jpeg')
					return true;
			},
			updateImageDisplay: function(e) {
				let file = e.target.files;

				// Check if the selected file exist.
				if(file.length == 1){
					if(this.isValidImageFormat(file[0])){
						// Update Image
						this.imageFile = file[0];
						this.hasChangePic = true;						
						this.profilePic = window.URL.createObjectURL(this.imageFile);
					}
					else
						alert('Cannot import this file. Use only this following format (.jpg, .jpeg, or .png).');
				}
			},
			changeProfile: function() {
				let request = new Request();
				let formdata = new FormData();

				if((this.lastName && this.firstName && this.email) != ''){
					formdata.set('username', this.username);
					formdata.set('last_name', this.lastName);
					formdata.set('first_name', this.firstName);
					formdata.set('email', this.email);
					formdata.set('tags', this.tags);
					formdata.set('biography', this.biography);			
					
					if(this.hasChangePic)
						formdata.append('imageFile', this.imageFile, this.imageFile.name)

					request.post('http://localhost:8000/', 'profile/edit_profile_details/', formdata,
					(response) => {
						alert(response.data)
					})
				}
			},
			changePassword: function(){
				let request = new Request();
				let formdata = new FormData();
				formdata.set('username', this.username);
				formdata.set('old_password', this.oldPassword);
				formdata.set('new_password', this.newPassword);
				
				if(this.matchedPassword){
					request.post('http://localhost:8000/', 'profile/edit_password/', formdata,
						(response)=>{
							alert(response.data)
							if(response.data == 'Changed Password: You will be redirect to the login page.')
								this.$router.go(0)
						}
					)
				}
			},
			addTag: function() {	
				if (this.tag != ''){
					let newTags = this.tags.map(item=>item)
					newTags.push(this.tag);
					this.tags = newTags
					alert(this.tag+' added')
					this.tag = ''	
				}			
				else
					alert('Please insert a text.')	
			},
			removeTag: function(){
				let request = new Request();
				let formdata = new FormData();

				formdata.set('username', this.username);
				formdata.set('tag', this.tag);

				request.post('http://localhost:8000/', 'profile/remove_tag/', formdata,
				(response) => { 
					alert(response.data);
					this.tag = ''; 							
				});
			}	
		},
		mounted: function() {
			let request = new Request();
			let formdata = new FormData();

			formdata.set('username', this.username);

			request.post('http://localhost:8000/', 'profile/request_profile_details/', formdata,
				(response) => {
					this.userProfile = response.data;

					this.profilePic = '/'+this.userProfile.avatar;
					this.lastName = this.userProfile.last_name;
					this.firstName = this.userProfile.first_name;
					this.email = this.userProfile.email;
					this.biography = this.userProfile.biography;
					this.isAuctioneer = this.userProfile.isAuctioneer;
					this.tags = this.userProfile.tags;
				}
			);	
		}
	}

</script>

<style>

</style>