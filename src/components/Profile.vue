<template>
	<v-container fluid>
		<v-layout row justify-center align-center mt-5>
			<div>				
				<div id='profile' v-if="hasProfilePic">
					<v-avatar 					
						size = 400>

						<img :src="profilePic"/>
					</v-avatar>
				</div>
				<v-layout row justify-center>
					<div class = 'mx-auto' align='center'>
						<v-btn
							v-if="$route.params.username == $store.getters.getUsername"
							@click="moveToEdit"
						>
							Edit Profile
						</v-btn>
						<v-btn
							v-if="
								$route.params.username != $store.getters.getUsername && isAuctioneer
							"
							@click="subscribe"
						>
							Subscribe
						</v-btn>
						<span class = 'body-2'>Name:</span>
						<p v-text="name" class="title"></p>
						
						<div v-if="isAuctioneer">
							<span class = 'body-2'>Subscribers:</span>
							<p class="title">{{subscribers}}</p>
						</div>
						
						<span class = 'body-2'>Email:</span>
						<p v-text="email"></p>

						<div v-if="isAuctioneer == true">
							<!-- Tags -->
							<span class = 'body-2'>Tags:</span>
							<ul>
								<!-- Display all tags for current User. -->
								<li v-for="tag in tags">
									{{tag.name}} &nbsp
								</li>
							</ul>
							<!-- Biography -->
							<span class = 'body-2'>Biography:</span>
							<p v-text="biography"></p>
						</div>
					</div>
				</v-layout>
			</div>
		</v-layout>
	</v-container>
</template>


<script type="text/javascript">
	import Request from '../assets/js/Request.js';
	import store from '../store'

	export default {
	// User Details
		name: "Profile",
		data() {
			return {
				userProfile: '',
				name:'',
				email:'',
				subscribers: '',
				biography: '',
				profilePic: '',
				tags: [],
				isAuctioneer: ''//modify isAuctioneer for auctioneer identification
			}
		},

		methods: {
			// This function will return true if the file is JPEG or PNG.
			moveToEdit(){
				this.$router.push({
					name: "Edit-Profile",
				})
			},
			subscribe() {
				//add subsciber if clicked
				this.subscribers++
			}
		},

		computed: {
			// This function will return true if there exist a picture.
			hasProfilePic() {
				return this.profilePic.length > 0
			},
		},

		mounted: function() {
			let request = new Request();
			let formdata = new FormData();

			formdata.set('username', this.$route.params.username)


			request.post('http://localhost:8000/','profile/request_profile_details/', formdata,
			(response) => {
				this.userProfile = response.data
				this.profilePic = '/'+this.userProfile.avatar
				this.name = this.userProfile.last_name + ', ' + this.userProfile.first_name
				this.email = this.userProfile.email
				this.biography = this.userProfile.biography
				this.tags = this.userProfile.tags
				this.isAuctioneer = this.userProfile.isAuctioneer
				this.subscribers = this.userProfile.subscribers
			})
		},
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