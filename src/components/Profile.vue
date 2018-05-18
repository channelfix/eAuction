<template>
	<div id="profile_id">
		<div id='profile' v-if="hasProfilePic"> 
			<img :src="profilePic" width="500" height="500"/>
		</div>

		<input type="file" id="fileElem" v-on:change="updateImageDisplay"><br>

		<!-- [Current User] -->

		<!-- Full Name -->
		<b>Name:</b>
		<p v-text="name"></p>

		<!-- Any Email -->
		<b>Email:</b>
		<p v-text="email"></p>

		<!-- Biography -->
		<b>Biography:</b>
		<p v-text="biography"></p>

		<!-- Tags -->
		<b>Tags:</b>
		<ul>
			<!-- Display all tags for current User. -->
			<li v-for="tag in tags">
				{{tag.name}}
			</li>
		</ul>
 	</div>
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
				input: ''
			}
		},

		methods: {
			// This function will check the image format then updates the profile picture.
			updateImageDisplay: function() {
				var imageFile = this.input.files

				// Check if any file is selected from File Selector.
				if(imageFile.length == 1){
					// Check if the file format is JPEG or PNG file.			
					if(this.isValidImageFormat(imageFile[0].type))
						this.profilePic = window.URL.createObjectURL(imageFile[0]);
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
				request.post("http://localhost:8000/profile/", "request_profile/", formdata, 
					(response) => {

						this.userProfile = response.data

						//[Current User]

						// Profile Picture					
						this.profilePic = '../../../' + this.userProfile.avatar

						// Full name
						this.name = this.userProfile.last_name + ", " + this.userProfile.first_name;

						// Email
						this.email = this.userProfile.email;

						// Biography
						this.biography = this.userProfile.biography;

						// Tags
						this.tags = this.userProfile.tags;

						// Get a reference to File Selector
						this.input = document.getElementById('fileElem');
				})
		}
	}

</script>

<style scoped>
</style>