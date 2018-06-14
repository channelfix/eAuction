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
				style: {
					red: true,
					grey: false,
				},
				open: true,
			},
			startAuction: {
				style: {
					green:true,
					grey: false,
				},
				open: true,
			},
			closeItem: {
				style: {
					red: false,
					grey: true,
				},
				open: false,
			},
			minimumBidSetter: {
				style: {
					green: false,
					grey: true,
				},
				open: false,
			},
			moveNext: {
				style: {
					green: false,
					grey: true,
				},
				open: false,
			},
			openItem: {
				style: {
					green: false,
					grey: true,
				},
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
			console.log(this.status)
			if(this.status == "item hold"){
				this.endAuction.open = true;
				this.startAuction.open = false;
				this.closeItem.open = false;
				this.minimumBidSetter.open = false;
				this.moveNext.open = false;
				this.openItem.open = true;
			}else if(this.status == "open bidding"){
				this.endAuction.open = true;
				this.startAuction.open = false;
				this.closeItem.open = false;
				this.minimumBidSetter.open = false;
				this.moveNext.open = false;
				this.openItem.open = false;
			}else if(this.status == "hold bidding"){
				this.endAuction.open = true;
				this.startAuction.open = false;
				this.closeItem.open = false;
				this.minimumBidSetter.open = true;
				this.moveNext.open = false;
				this.openItem.open = false;
			}else if(this.status == "open bidding:no bid"){
				this.endAuction.open = true;
				this.startAuction.open = false;
				this.closeItem.open = true;
				this.minimumBidSetter.open = false;
				this.moveNext.open = false;
				this.openItem.open = false;
			}else if(this.status == "item closed"){
				this.endAuction.open = true;
				this.startAuction.open = false;
				this.closeItem.open = false;
				this.minimumBidSetter.open = false;
				this.moveNext.open = true;
				this.openItem.open = false;
			}

			this.endAuction.style.red = this.endAuction.open;
			this.endAuction.style.grey = !this.endAuction.open;

			this.startAuction.style.green = this.startAuction.open;
			this.startAuction.style.grey = !this.startAuction.open;

			this.closeItem.style.red = this.closeItem.open;
			this.closeItem.style.grey = !this.closeItem.open;

			this.minimumBidSetter.style.green = this.minimumBidSetter.open;
			this.minimumBidSetter.style.grey = !this.minimumBidSetter.open;

			this.moveNext.style.green = this.moveNext.open;
			this.moveNext.style.grey = !this.moveNext.open;

			this.openItem.style.green = this.openItem.open;
			this.openItem.style.grey = !this.openItem.open;
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
