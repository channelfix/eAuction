<template>
	<v-container fluid id="profile">
		<v-layout pa-5 row>
				<v-flex md4>
					<v-layout column>
						<v-flex id='profile' v-if="hasProfilePic">
							<img class="profPic" :src="profilePic"/>
						</v-flex>

						<v-layout row pa-2 v-if="isAuctioneer">
							<span class="title">Subscribers: </span>
							<v-spacer></v-spacer>
							<span class="title">{{subscribers}}</span>
						</v-layout>

						<v-btn
							v-if="$route.params.username == $store.getters.getUsername"
							@click="moveToEdit"
							block
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
					</v-layout>
					
				</v-flex>

				<!-- Profile content -->
				<v-flex md8 pa-3>
					<v-layout column>
						<v-layout row align-center>
							<v-flex pa-2>
							<span class = "title">Name: </span>
							<v-text-field solo light disabled v-model="name"></v-text-field>	
							</v-flex>
						</v-layout>
						<v-layout row align-center>
							<v-flex pa-2>
							<span class = "title">Email: </span>
							<v-text-field solo light disabled v-model="email"></v-text-field>	
							</v-flex>
						</v-layout>
						<v-layout row align-center>
							<v-flex pa-2>
							<span class = "title">Contact Number: </span>
							<v-text-field solo light disabled v-model="contactNumber"></v-text-field>	
							</v-flex>
						</v-layout>
						<v-layout 
							column 
							v-if="isAuctioneer == true"
							pa-2
						>
							<span class="title">
								Biography
							</span>
							<v-text-field light disabled solo v-model="biography" multi-line>
							></v-text-field>							
						</v-layout>						
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

<style scoped>
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

	.profPic{
		height: 100%;
		width: 100%;
	}

	#profile < p{
		margin-top: -5px;
	}

	#description{
		word-wrap: break-word;
	}
</style>