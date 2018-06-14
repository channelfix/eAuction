<template>
	<v-flex 
  		md4
  	>
  		<v-layout 
  			fill-height
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
				<v-text-field
				  label="Input bid"
				  v-model="bid"
				  :disabled="!bidButton.open"
				></v-text-field>
				<button
					:class="bidButton.style"
					:disabled="!bidButton.open"
					@click="placeBid"
				>
					Bid
				</button>	
			</v-layout>
  			</v-flex>
  		</v-layout> 
  	</v-flex>
</template>

<script>
import Request from '../assets/js/Request.js'

let request = new Request();

export default {
	name: "Bidder",
	props: {
		currentProductName: String,
		status: String,
	},
	data(){
		return {
			bid: 0,
			bidButton: {
				style: 'grey',
				open: false,
			}
		}
	},
	mounted() {
		this.$parent.startLiveStream();
	},
	methods: {
		placeBid(){
			let currentUser = this.$store.getters.getUsername;
			let log = currentUser+" bid "+this.bid+" for "+this.currentProductName;

			this.$parent.sendLog(log);
		}
	},
	watch:{
		status(){
			this.bidButton.open = (this.status == "open bidding");

			this.bidButton.style = (this.bidButton.open)?"green":"grey";
		}
	}
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
</style>
