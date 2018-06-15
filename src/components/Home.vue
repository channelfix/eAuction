<template>
 	<v-container
		fluid
		pa-5	
	>
		<v-layout
			fill-height
			justify-center
			align-center
			column
			v-if="livestreams.length == 0"
		> <!-- if no content -->
			<img 
				elevation-0
				class="sadFace"
				src="https://images.vexels.com/media/users/3/134743/isolated/preview/97ae591756f3dc69db88c09fd097319a-sad-face-emoji-emoticon-by-vexels.png"/>
  			<span class="display-2">No subscriptions</span>
  			<span class="headline">
  				Looks pretty lonely here, <router-link :to="{name: 'Explore'}" style="color: yellow">make some friends</router-link> 
  			</span>
		</v-layout>
 		<v-layout 
 			v-else
	 		row
	 		wrap
			>
			<v-flex
	 			v-for="livestream in livestreams"
				md3
				pa-3
				>
				<v-card 
					color="grey darken-1"
					:hover="true"
					@click.native="route(livestream.id, livestream.auctioneer_username)"
				>
					<v-card-media 
						:src="livestream.thumbnail" 
						height="250px"
					>
						<v-layout 
							row 
							wrap
							justify-end
							pa-2
						>
						    <v-icon
								large
								color="red lighten-1"
							>
								live_tv
							</v-icon>
						</v-layout>
					</v-card-media>	
					<v-card-title primary-title>
			          <div>
			            <p class="headline mb-0">{{livestream.title}}</p>
			            <p class="title mb-0">{{livestream.auctioneer_username}}</p>
			            <div>{{livestream.description}}</div>
			          </div>
			        </v-card-title>
				</v-card>
			</v-flex>
 		</v-layout>
 	</v-container>
</template>

<script>
import Request from '../assets/js/Request.js'

export default {
	name: 'Home',
	data(){
		return {
			showNav: false,
			livestreams: [],
		}
	},
	methods: {
		route(id, auctioneer){
			this.$router.push({
				name: 'Auction',
				params: {
					id,
					auctioneer,
				}
			})
		}
	},
	mounted: function() {
		let request = new Request();
		let formdata = new FormData();

		this.axios.get('/livestream/auction_events/')
		.then((response) => {
			this.livestreams = response.data.sessions
		})
	}
}
</script>

<style scoped>
	.sadFace{
		height: 250px;
		width: 250px;
	}
</style> 