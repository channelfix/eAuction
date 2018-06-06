<template>
	<v-container
		fluid
	>
	  	<v-layout
			row
	  	>
	  		<v-flex md7> <!-- left -->
	  		  	<v-layout column>
		  		  	<div class="box livestream" id="livestream">		  		 
					    <div id="publisher"></div>
					    <div id="subscriber"></div>
		  		  	</div>
		  		  	<Auctioneer v-if="$store.getters.getUsername == $route.params.auctioneer"></Auctioneer>
		  		  	<Bidder v-else></Bidder>
	  		  	</v-layout>
	  		</v-flex>
	  		<v-flex md5>  <!-- right -->
  		  		<v-layout
					column	
	  			>
	  				<v-flex 
	  					md3
  					>
  						<v-layout
							row
							class="amber darken-2"

						>
							<v-flex 
								md6 
							>
								
							</v-flex>
							<v-flex 
								md6
							>
								<v-layout
									pa-3
									column
									justify-center
								>
									<p class="headline">{{currentProduct.name}}</p>
								</v-layout>
							</v-flex>
  						</v-layout>
	  				</v-flex>
	  				<v-flex 
	  					md2
  					>
  						<v-layout
							align-center
							justify-center
							class="amber darken-1"
							pa-2
						>
							<span class="headline">Current Bid: &#8369 {{formattedBid}}</span>
  						</v-layout>
	  				</v-flex>
	  				<v-flex 
	  					md7
						class="grey darken-4"
	  					pa-4
	  				>
	  					<p>Log</p>
						<div class="logbox">
							<v-layout
								column
								wrap
							>
								<v-list two-line>
									<template v-for="act of activity">
										<v-list-tile dark>
											<v-list-tile-content>{{act.name}} {{act.action}} {{act.bid}} {{act.product}}</v-list-tile-content>
										</v-list-tile>
										<v-divider></v-divider>
									</template>
								</v-list>
							</v-layout>
						</div>
	  				</v-flex>
  		  		</v-layout>
	  		</v-flex>
	  	</v-layout>
	</v-container>
</template>

<script>
import Request from '../assets/js/Request.js'
import Auctioneer from 'Auctioneer.vue'
import Bidder from 'Bidder.vue'

function formatDecimal(num) {
	return parseFloat(Math.round(num * 100) / 100).toFixed(2)
}

let logThread;
let request = new Request();

export default {
	name: "Auction",

	data(){
		return{
			opentokCloud: '',
			apiKey: '',
			sessionId: '',
			token: '',
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
		}
	},
	mounted: function(){
		if(this.$route.params.auctioneer == this.$store.getters.getUsername){ // checks if current user is owner of auction
			this.axios.get('/livestream/auctioneer/')
			.then((response) => {
				this.opentokCloud = response.data

				this.apiKey = this.opentokCloud.api_key
				this.sessionId = this.opentokCloud.session_id
				this.token = this.opentokCloud.token

				let session, publisher;
				let hasPublish = false;
				let xhttp;

				if(OT.checkSystemRequirements() == 1){ // Check if this browser supports WebRTC.
					session = OT.initSession(this.apiKey, this.sessionId);

					session.connect(this.token, function(error) { // Check if the client has successfully connected to the session.
						if(error){

						}
						else{				
							// Create a publisher for exposing the video to other client who is also connected to the same session.
							publisher = OT.initPublisher('publisher', {insertMode: 'append', width: "40%", height: "100%"}); 
						    session.publish(publisher);
						}
					});
				}
			})
		}else{
			this.axios.get('/livestream/bidder/')
			.then((response) => {
				this.opentokCloud = response.data

				this.apiKey = this.opentokCloud.api_key
				this.sessionId = this.opentokCloud.session_id
				this.token = this.opentokCloud.token

				let session;

				if(OT.checkSystemRequirements() == 1){ // Check if this browser supports WebRTC.
					session = OT.initSession(this.apiKey, this.sessionId);

					session.connect(this.token, function(error) { // Check if this client is connected to the 
					});

					session.on("streamCreated", function(event) { // Check if the stream has created in a certain session.
						
						// Accept the exposed video who is connected to the same session.
						session.subscribe(event.stream, 'subscriber', {insertMode:'append', width:'100%', height:'100%'}); 						
					});


					session.on("streamDestroyed", function(event) {							
					});
				}
			})
		}

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
