<template>
 	<v-container
		fluid
		pa-5
		>
		<v-layout
			justify-center
			row
			wrap
			v-if="livestreams.length == 0"
		> <!-- if no content -->
			<v-icon
				large
	 	   >
	    		subscriptions
			</v-icon>
	  		<span class="headline">No subscriptions</span>
		</v-layout>
 		<v-layout 
 			v-if="livestreams.length != 0"
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
				>
					<v-card-media 
						:src="livestream.thumbnail" 
						height="300px"
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
			            <div>{{livestream.description}}</div>
			          </div>
			        </v-card-title>
				</v-card>
			</v-flex>
 		</v-layout>
 	</v-container>
</template>

<script>
export default {
	name: 'Home',
	data(){
		return {
			showNav: false,
			livestreams: [
				{
					title: "eAuction",
					description: "eAuction",
					thumbnail: "http://lheventures.com/wp-content/uploads/sites/7/2017/10/Cooke-Auction-Property-pic.png",
				}
			],
		}
	}
}
</script>

<style scoped>
</style> 