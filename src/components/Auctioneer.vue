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
							:class="endAuction.style"
							:disabled="!endAuction.open"
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
							:class="startAuction.style"
							:disabled="!startAuction.open"
							@click="startLive"
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
							:class="closeItem.style"
							:disabled="!closeItem.open"
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
							:disabled="!minimumBidSetter.open"
							label="Bid Increase"
							v-model="bidMinimum"
						>
							
						</v-text-field>
						<button 
							:disabled="!minimumBidSetter.open"
							class="halfsize"
							:class="minimumBidSetter.style"
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
						<button 
							:class="moveNext.style"
							:disabled="!moveNext.open"
							@click="moveToNextItem"
						>
							Move to next item
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
						<button 
							:class="openItem.style"
							:disabled="!openItem.open"
							@click="openAuction"
						>
							Open auction current item
						</button>
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
		status: String,
	},
	data(){
		return {
			bidMinimum: 0,
			endAuction: {
				style: 'red',
				open: true,
			},
			startAuction: {
				style: 'green',
				open: true,
			},
			closeItem: {
				style: 'grey',
				open: false,
			},
			minimumBidSetter: {
				style: 'grey',
				open: false,
			},
			moveNext: {
				style: 'grey',
				open: false,
			},
			openItem: {
				style: 'grey',
				open: false,
			},
		}
	},
	methods: {
		startLive() {
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
		},
		moveToNextItem(){
			let log = "Moved to next item";
			this.$parent.sendLog(log);
		},
		openAuction(){
			let log = "Auction for "+this.currentProductName+" is open";
			this.$parent.sendLog(log);
		}
	},
	watch: {
		status() {
			this.startAuction.open = (this.status == "not live");

			this.closeItem.open = (this.status == "no bid");

			this.minimumBidSetter.open = (this.status == "hold bidding");

			this.moveNext.open = (this.status == "item closed");

			this.openItem.open = (this.status == "item hold");

			this.endAuction.style = (this.endAuction.open)?"red":"grey";

			this.startAuction.style = (this.startAuction.open)?"green":"grey";

			this.closeItem.style = (this.closeItem.open)?"red":"grey";

			this.minimumBidSetter.style = (this.minimumBidSetter.open)?"green":"grey";

			this.moveNext.style = (this.moveNext.open)?"yellow":"grey";

			this.openItem.style = (this.openItem.open)?"green":"grey";
		},
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

	.halfsize {
		width: 50%;
	}
</style>
