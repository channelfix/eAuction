<template>
	<v-container fluid id="profile">
		<v-layout justify-center align-start mt-5 row>

				<v-flex offset-x5 xs3>
					<div id='profile' v-if="hasProfilePic">
						<v-avatar
							tile 					
							size = 400>

							<img :src="profilePic"/>
						</v-avatar>
					</div>

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

						v-text="subscriptionStatus"
					>
					</v-btn>
				</v-flex>

				<!-- Profile content -->
				<v-flex xs4>
					<v-layout row>
						<v-flex xs12>
							<span class = "">Name surname</span>
							<p 
								v-text="name" 
								class="title" 
								style="margin-top: -5px !important;"
							></p>
						</v-flex>					
					</v-layout>

					<v-layout row>
						<v-flex xs4>
							<span class = "">Email address</span>
							<p v-text="email" class="title" style="margin-top: -5px;"></p>     
						</v-flex>
						<v-flex xs3>
							<span class = "">Contact number</span>
							<p 
								v-text="contactNumber" 
								class="title" 
								style="margin-top: -5px !important;"
							></p>
						</v-flex>	
						<v-flex xs3>
							<div style="text-align: center;">
				                <span class = "body-2">Subscribers</span>
				                <div class="title">
				                    <p style="display:inline;"> {{subscribers}} </p>
				                </div>
				            </div>
						</v-flex>															
					</v-layout>

					<v-layout row v-if="isAuctioneer == true">
						<v-chip
			                large	     
			                label
			                outline color="secondary" 
			                v-for="tag in tags"
			                disabled
			            >                 
			            <v-icon left>label</v-icon>
			                {{tag.name}}
			            </v-chip>
					</v-layout>

					<v-layout 
						row 
						v-if="isAuctioneer == true"
						mt-3
					>
						<v-flex xs12>
							Biography
							<div style="
								height: 195px; 
								overflow-y: auto;">
								<p 
									class="subheading"
									v-text="biography"
								></p>
							</div>							
						</v-flex>
					</v-layout>

				</v-flex>
			

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
				lastname: '',
				firstname: '',
				email:'',
				subscribers: '',
				biography: '',
				profilePic: '',
				tags: [],
				isAuctioneer: '',//modify isAuctioneer for auctioneer identification
				subscriptionStatus: '', // Displays text either subscribe or unsubscribe
				contactNumber: ''
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
				let request = new Request();
				let formdata = new FormData();

				formdata.set('username', this.$route.params.username)

				request.post('/profile/subscribe/', formdata,
				(response) => {
					this.subscriptionStatus = response.data

					if(this.subscriptionStatus == 'Unsubscribe')
						this.subscribers++;
					else
						this.subscribers--;
				})
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


			request.post('/profile/request_profile_details/', formdata,
			(response) => {
				this.userProfile = response.data
				this.profilePic = '/'+this.userProfile.avatar
				this.name = this.userProfile.first_name + ' ' + this.userProfile.last_name
				this.lastname = this.userProfile.last_name
				this.firstname = this.userProfile.first_name
				this.email = this.userProfile.email
				this.biography = this.userProfile.biography
				this.tags = this.userProfile.tags
				this.isAuctioneer = this.userProfile.isAuctioneer
				this.subscribers = this.userProfile.subscribers
				this.contactNumber = this.userProfile.contact_number

				let hasSubscribed = this.userProfile.hasSubscribed

				if(hasSubscribed)
					this.subscriptionStatus = 'unsubscribe'
				else
					this.subscriptionStatus = 'subscribe'
			})
		},
	}

</script>

<style>
	ul {
		list-style-type: none;
		margin: 0;
		padding: 0;
		padding-bottom: 10px;
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

	#profile < p{
		margin-top: -5px;
	}

	#description{
		word-wrap: break-word;
	}
</style>