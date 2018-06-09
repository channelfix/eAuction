<template>
	<v-flex 
  		md4
  	>
  		<v-layout 
  			fill-height
			row
			wrap
		>
  			<v-layout 
  				row 
  				wrap
			>
  				<v-flex 
					md6
				>
					<v-layout 
						align-center
						pa-3
					>
						<button 
							class="red"
							@click="closeAuction"
						>
							End Auction
						</button>	
					</v-layout>
  				</v-flex>
	  			<v-flex 
				md6
					>
					<v-layout
						align-center
						pa-3
					>
						<button
							class="green"
							@click="startAuction"
						>
							Start Auction
						</button>	
					</v-layout>
	  			</v-flex>
	  			<v-flex 
					md4
				>
					<v-layout 
						align-center
						pa-3
					>
						<button 
							class="red"
							@click="closeCurrentItem"
						>
							Close auction for current item
						</button>	
					</v-layout>
  				</v-flex>
  				<v-flex 
					md5
				>
					<v-layout 
						align-center
						justify-center
						pa-3
					>
						<v-text-field
							label="Bid Increase"
							v-model="bidMinimum"
						>
							
						</v-text-field>
						<button 
							class="halfsize green"
							@click="setMinimumBid"
						>
							Set minimum bid
						</button>
					</v-layout>
  				</v-flex>
  				<v-flex 
					md3
				>
					<v-layout 
						align-center
						justify-center
						pa-3
					>
						<button class="green">Move to next item</button>
					</v-layout>
  				</v-flex>
  				<v-flex 
					md3
				>
					<v-layout 
						align-center
						justify-center
						pa-3
					>
						<button class="green">Open auction current item</button>
					</v-layout>
  				</v-flex>
	  		</v-layout>
  		</v-layout>
  	</v-flex>
</template>

<script>
import Request from '../assets/js/Request.js'

let request = new Request();

export default {
	name: 'Auctioneer',
	props: {
		currentProductName: String,
	},
	data(){
		return {
			bidMinimum: 0,
		}
	},
	methods: {
		startAuction() {
			this.$parent.startLiveStream();
		},
		closeAuction(){
			this.$parent.endAuction();
		},
		closeCurrentItem(){
			let log = this.currentProductName+" is closed for auction";
			this.$parent.sendLog(log);
		},
		setMinimumBid(){
			let log = "Minimum bid set to "+this.bidMinimum;
			this.$parent.sendLog(log);
		}
	},
}
</script>

<style scoped>
	html{
		overflow-y: hidden;
	}

	button {
		height: 5em;
		width: 100%;
	}

	.halfsize {
		width: 50%;
	}
</style>
