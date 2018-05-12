<template>
 	<div id="profile_id"> 	
 		<button @click="requestProfile">request profile</button>
 		<p v-text="simpleText"></p>
 	</div>
</template>

<script type="text/javascript">
	import axios from 'axios';

	export default {
		data() {
			return {
				simpleText: 'Livestream'
			}
		},
		methods: {
			requestProfile: function() {
				axios.get("http://localhost:8000/profile/request_profile/")
				.then((response) => {
					// Requested Successfully
					this.simpleText = response.data;
				}, (error) => {
					alert('Failed to request')
				})
			}
		}
	}

	
</script>