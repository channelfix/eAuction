<template>
 	<div id="profile_id"> 	
 		<button @click="requestProfile">request profile</button>
 	</div>
</template>

<script type="text/javascript">
	import axios from 'axios';

	export default {
		data() {
			return {
				userProfile: null
			}
		},
		methods: {
			requestProfile: function() {
				axios.get("http://localhost:8000/profile/request_profile/")
				.then((response) => {
					
					// Get all the field value from User, Profile and Tags 					
					this.userProfile = response.data

					var div = document.getElementById("profile_id")

					var html = ""

					// [Current User]
					html += "<img src=../../../" + this.userProfile.avatar + "><br>"


					// Display the full name
					html += "<h4>Name: </h4><p>" + this.userProfile.last_name + ", " + this.userProfile.first_name + "</p>"

					// Display the email
					html += "<h4>Email: </h4><p>" + this.userProfile.email + "</p>"

					// Display the biography
					html += "<h4>Biography: </h4><p>" + this.userProfile.biography + "</p>"

					// Get all the tags value given the 'tag' key
					var tags = this.userProfile.tags
					html += "<h4>Tags: </h4>"

					for(var x in tags)
						html += "<p>" + tags[x].name + "</p>"			


					div.innerHTML = html


				}, (error) => {
					alert('Failed to request')
				})
			}
		}
	}
		
</script>