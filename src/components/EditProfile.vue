<template>
	<v-container fluid class = "editProfilePage">
		<v-layout row justify-center mt-5 wrap>
			
				<v-flex xs3>
					<form>
						<div id="profile"/>
							<img :src="profilePic" width="400" height="400" />
						</div>
						<input type="file" id="fileSelector" v-on:change="updateImageDisplay" />
						<div v-if="isAuctioneer">
							<p class="biograpyProperty mt-2 pt-2 ">
								<p class="title mb-0">Biography</p>
								<v-text-field
									style="width: 80% !important; margin-top: -10px !important;"
									id = "biographyField"
									rows="3"
									multi-line
									v-model="biography"
									hint="Describe yourself"
								></v-text-field>
							</p>
							<p class="tagsProperty">
								<v-select
									style="width: 80% !important;"
									:items="items"
									v-model="tag"
									label="Select Tag"
									single-line
								></v-select>	
								<v-btn @click.prevent="addTag">Add Tag</v-btn>
								<v-btn @click.prevent="removeTag">Remove Tag</v-btn>
							</p>
						</div>
					</form>
				</v-flex>
				
				<v-flex xs3>
					<form>
						<p class="mb-2 title">Login and Security</p>
						<v-divider class="mb-1"></v-divider>
						<p class='lastNameProperty my-0'>
							<v-text-field 
								type="text" 
								id="lastNameField" 
								v-model="lastName"
								label="Last name"
							></v-text-field>
						</p>

						<p class='firstNameProperty my-0'>
							<v-text-field 
								type="text" 
								id="firstNameField" 
								v-model="firstName"
								label="First name"
							></v-text-field>
						</p>

						<p class="emailProperty my-0">
							<v-text-field 
								type="text" 
								id="emailField" 
								v-model="email"
								label="Email"
							></v-text-field>
						</p>

						<p class="contactNumberProperty my-0">
							<v-text-field
								type="text" 
								id="contactNumberField" 
								v-model="contactNumber"
								label="Contact Number"
							></v-text-field>
						</p>
						<v-btn id="changeButton" v-on:click="changeProfile">Save</v-btn>
						<p class="mb-2 mt-3 title">Change Password</p>
						<v-divider class="mb-1"></v-divider>
						<p class = "my-0">
							<v-text-field 
								type="password" 
								id="oldPasswordField" 
								v-model="oldPassword"
								label="Enter Old Password"
							></v-text-field>
						</p>

						<p class = "my-0">
							<v-text-field
								type="password" 
								id="newPasswordField" 
								v-model="newPassword"
								label="Enter New Password"
							></v-text-field>
						</p>

						<p class = "my-0">
							<v-text-field 
								type="password" 
								id="confirmedPasswordField" 
								v-model="confirmPassword"
								label="Confirm Password"
							></v-text-field>
							<label v-if="hasMatchPassword">Passwords match!</label>
							<label v-else="hasMatchPassword">Passwords do not match</label>
						</p>
						<v-btn
							@click="changePassword"
							:disabled="!hasMatchPassword"
						>Change Password</v-btn>
					</form>					
				</v-flex>
				
		</v-layout>
	</v-container>
	
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
				tag: '',
				oldPassword: '',
				newPassword: '',				
				confirmPassword: '',
				imageFile: '',
				hasChangePic: false,
				matchedPassword: false,
				isAuctioneer: false,
				contactNumber: '',
				items: [
					{text: 'Collectibles'},
					{text: 'Antiques'}, 
					{text: 'Novel'},
					{text: 'Vehicles'},
					{text: 'Jewelry'},
				]
			}
		},
		computed: {
			hasMatchPassword() {
				if(this.newPassword === this.confirmPassword && (this.newPassword != "" && this.confirmPassword != "")){
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
					formdata.set('biography', this.biography);

					if(this.hasChangePic)
						formdata.append('imageFile', this.imageFile, this.imageFile.name)

					// Check for valid phone number format
					let contactNumber = this.contactNumber
					if((contactNumber.match(/[0-9]+/).length != 0) || contactNumber.length == 0)
					{
						formdata.set('contact_number', contactNumber);

						request.post('/profile/edit_profile_details/', formdata,
						(response) => {
							alert(response.data)
							this.requestProfileDetails()
							this.$router.push({
								name: "Profile",
								params: {
									username: this.username
								}
							})
						})
					}		
				}
			},
			changePassword: function(){
				let request = new Request();
				let formdata = new FormData();
				formdata.set('username', this.username);
				formdata.set('old_password', this.oldPassword);
				formdata.set('new_password', this.newPassword);
				
				if(this.matchedPassword){
					request.post('/profile/edit_password/', formdata,
						(response)=>{
							alert(response.data)
							if(response.data == 'Changed Password: You will be redirect to the login page.')
								this.$router.go(0)
						}
					)
				}
			},
			viewProductLog() {
				this.$router.push({
					name: 'Product'
				})
			},
			findTag: function(element) {
				return element.name === this.tag.text
			},
			addTag: function() {
				if (this.tag.text != ''){
					let newTags = this.tags.map(item=>item)
					if(newTags.find(this.findTag))
						alert('You already have this tag.')
					else{					
						let tag = this.tag.text	
						newTags.push(tag);
						this.subTag.push(tag);
						this.tags = newTags
						alert(this.tag.text+' added')
						this.tag.text = ''						
					}
				}			
				else
					alert('Please insert a text.')	
			},
			removeTag: function(){
				let request = new Request();
				let formdata = new FormData();

				formdata.set('username', this.username);
				formdata.set('tag', this.tag);

				request.post('/profile/remove_tag/', formdata,
				(response) => { 
					alert(response.data);
					this.tag = ''; 							
				});
			},
			requestProfileDetails() {				
				let request = new Request();
				let formdata = new FormData();

				formdata.set('username', this.username);

				request.post('/profile/request_profile_details/', formdata,
					(response) => {
						this.userProfile = response.data;
						this.profilePic = '/'+this.userProfile.avatar;
						this.lastName = this.userProfile.last_name;
						this.firstName = this.userProfile.first_name;
						this.email = this.userProfile.email;
						this.biography = this.userProfile.biography;
						this.isAuctioneer = this.userProfile.isAuctioneer;
					}
				);
			}	
		},
		mounted: function() {
			this.requestProfileDetails()
		}
	}

</script>

<style>
	.editProfilePage < .btn{
		margin-left: 0px !important;
	}

</style>