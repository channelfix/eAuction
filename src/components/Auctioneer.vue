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
				<button 
					:class="decline.style"
					:disabled="!decline.open"
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
					:class="accept.style"
					:disabled="!accept.open"
					@click="accepted"
				>
					Start Auction
				</button>	
			</v-layout>
  			</v-flex>
  		</v-layout> 
  	</v-flex>
</template>

<script>
import Request from '../assets/js/Request.js'

function formatDecimal(num) {
	return parseFloat(Math.round(num * 100) / 100).toFixed(2)
}

let logThread;
let request = new Request();

export default {
	name: 'Auctioneer',
	data(){
		return{
			opentokCloud: '',
			apiKey: '',
			sessionId: '',
			token: '',
			isAuctioneer: this.$store.getters.isAuctioneer,
			currentBid: 0,
			products: [
				{
					name: "Pencil",
					price: 0,
				},
			],
			status: "open", //status: open, closed, nodecline, noaccept
			activity: [{
				name: 'bojoluis',
				action: 'Declined',
				product: 'pencil',
				bid: 0,
			},{
				name: 'bojoluis',
				action: 'Accepted',
				product: 'pencil',
				bid: 0,
			},{
				name: 'bojoluis',
				action: 'Destroy',
				product: 'pencil',
				bid: 0,
			},{
				name: 'bojoluis',
				action: 'Increased',
				product: 'pencil',
				bid: 0,
			},{
				name: 'bojoluis',
				action: 'Won',
				product: 'pencil',
				bid: 0,
			},
			],
			accept: {
				style: {
					green: true,
					grey: false,
				},
				open: true,
			},
			decline: {
				style: {
					red: true,
					grey: false,
				},
				open: true,
			}
		}
	},
	mounted: function(){
		let request = new Request();
		let formdata = new FormData();

		formdata.set('auction_id', this.$route.params.id)
		formdata.set('is_auctioneer', this.isAuctioneer)

		request.post('/livestream/initiate_auction/', formdata,
		(response) => {

			this.opentokCloud = response.data

			this.apiKey = this.opentokCloud.api_key
			this.sessionId = this.opentokCloud.session_id
			this.token = this.opentokCloud.token

			let session, publisher;
			let hasPublish = false;
			let xhttp;

			if(OT.checkSystemRequirements() == 1){ // Check if this browser supports WebRTC.
				console.log('This browser supports WebRTC')
				session = OT.initSession(this.apiKey, this.sessionId);

				session.connect(this.token, function(error) { // Check if the client has successfully connected to the session.
					if(error){
						console.log('failed to connect to the session')
					}
					else{				
						console.log('successfully connected to the session')
						// Create a publisher for exposing the video to other client who is also connected to the same session.
						publisher = OT.initPublisher('publisher', {insertMode: 'append', width: "40%", height: "100%"}); 
					    session.publish(publisher);
					}
				});
			}
		})

		//// get activity log thread
		logThread = setInterval(
			() => {
				// constantly ask from the server for new log 
			},
			500
		)
	},
	methods: {
		accepted() {
			this.status = "closed"

			let formdata = new FormData();

			let data = {
				username: this.$store.getters.getUsername,
				currentBid: this.currentBid,
				product: this.currentProduct,
			}

			for(let key in data){
				formdata.set(key, data[key]);
			}

			// send data
		}
	},
	watch: {
		status() {
			if(this.status == "open"){
				this.accept.open = true;
				this.decline.open = true;
			}else if(this.status == "closed"){
				this.accept.open = false;
				this.decline.open = false;
			}else if(this.status == "noaccept"){
				this.accept.open = false;
				this.decline.open = true;
			}else if(this.status == "nodecline"){
				this.accept.open = true;
				this.decline.open = false;
			}

			this.accept.style.green = this.accept.open;
			this.accept.style.grey = !this.accept.open;
			this.decline.style.red = this.decline.open;
			this.decline.style.grey = !this.decline.open;
		},
	},
	computed:{
		formattedBid() { 
			return formatDecimal(this.currentBid);
		},
		logMessage(){
			let msg = "";
			this.activity.forEach(
				(current) => {
					msg += current+"\n";
				}
			);
			return msg;
		},
		currentProduct() {
			let current = this.products[this.products.length-1];
			current.price = formatDecimal(current.price); 
			return current;
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

	.livestream{
		height: 700px;
		background-color: black;
	}

	.publisher {
	    position: absolute;
	    width: 360px;
	    height: 240px;
	    bottom: 10px;
	    left: 10px;
	    z-index: 100;
	    border: 3px solid white;
	    border-radius: 3px;
	}

	.subscriber {
	    position: absolute;
	    width: 360px;
	    height: 240px;
	    bottom: 10px;
	    left: 10px;
	    z-index: 100;
	    border: 3px solid white;
	    border-radius: 3px;
	}

	.logbox {
		overflow: scroll;
		height: 800px;
	}
</style>
