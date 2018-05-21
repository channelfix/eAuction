<template>
	<v-container fluid>
		<v-layout row justify-center align-center mt-5>
<<<<<<< HEAD
			<div>				
				<div id='profile' v-if="hasProfilePic">
					<v-avatar 					
						size = 400>
=======
			<div>
				<div id='profile' v-if="hasProfilePic">
					<v-avatar size = 400>
>>>>>>> 6ac658cd1993c692365bb6a8ce9fd5f5bd10ec96
						<img :src="profilePic"/>
					</v-avatar>
				</div>
				<input type="file" id="fileElem" v-on:change="updateImageDisplay">
				<!-- [Current User] -->

				<!-- Full Name -->
				<v-layout row justify-center>
					<div class = 'mx-auto' align='center'>
						<!-- note: remove 'name: ', 'email' -->
						<span class = 'body-2'>Name:</span>
						<p v-text="name" class="title"></p>

						<!-- Any Email -->
						<span class = 'body-2'>Email:</span>
						<p v-text="email"></p>

						<!-- Tags -->
						<span class = 'body-2'>Tags:</span>
						<ul>
							<!-- Display all tags for current User. -->
							<li v-for="tag in tags">
								{{tag.name}} &nbsp
							</li>
						</ul>
						<!-- <p v-for="tag in tags">
							{{tag.name}}
						</p> -->

						<!-- Biography -->
						<span class = 'body-2'>Biography:</span>
						<p v-text="biography"></p>
					</div>
				</v-layout>
			</div>
		</v-layout>
	</v-container>
</template>


<script type="text/javascript">
	import Request from '../assets/js/Request.js';

	export default {
	// User Details
		name: "Profile",
		props: {
			username: String,
		},
		data() {
			return {
				userProfile: '',
				name: '',
				email: '',
				biography: '',
				profilePic: '',
				tags: [],
			}
		},

		methods: {
			// This function will check the image format then updates the profile picture.
			updateImageDisplay: function(e) {
				var imageFile = e.target.files

				// Check if any file is selected from File Selector.
				if(imageFile.length == 1){
					// Check if the file format is JPEG or PNG file.			
					if(this.isValidImageFormat(imageFile[0].type)){
						this.profilePic = imageFile[0]
						/* Save an image in a media folder
						   and update the profile picture
						   of a certain User. */

						let request = new Request();
						let formdata = new FormData();

						formdata.append('imageFile', imageFile[0], imageFile[0].name)

						
						request.post('http://localhost:8000/', 'profile/save_profile_pic/', formdata,
						(response) => {
							alert(response.data);
						})

					}
					else
						alert('Cannot import this file. use only this following format (jpg, jpeg, and png).');
				}
				else
					alert('No file selected.');
			},

			// This function will return true if the file is JPEG or PNG.
			isValidImageFormat: function(selectedFileType) {

				if(selectedFileType === 'image/jpg' || selectedFileType === 'image/jpeg' || selectedFileType === 'image/png')
					return true;
			}
		},

		computed: {

			// This function will return true if there exist a picture.
			hasProfilePic() {
				return this.profilePic.length > 0
			}
		},
		mounted: function() {
				let request = new Request();
				let formdata = new FormData();
				//add username to formdata
				formdata.set('username', this.username);

				// Request for the user details from the server.
				request.post('http://localhost:8000/', 'profile/request_profile_details/', formdata, 
					(response) => {

						this.userProfile = response.data

						//[Current User]

						// Profile Picture					
						this.profilePic = '/'+this.userProfile.avatar						

						// Full name
						this.name = this.userProfile.last_name + ', ' + this.userProfile.first_name;

						// Email
						this.email = this.userProfile.email;

						// Biography
						this.biography = this.userProfile.biography;

						// Tags
						this.tags = this.userProfile.tags;
				})
		}
	}

</script>

<style>
	ul {
		list-style-type: none;
		margin: 0;
		padding: 0;
		overflow: hidden;
	}

	li {
		float: left;
	}

	html{
		overflow: hidden;
	}

	img{
		box-shadow: 0px 2px 10px #000000;
	}

</style>