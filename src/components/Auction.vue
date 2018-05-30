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
		  		  	<v-flex md4>
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
									Decline
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
										Accept
									</button>	
								</v-layout>
		  		  			</v-flex>
		  		  		</v-layout> 
		  		  	</v-flex>
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
						<v-layout
							column
							wrap
						>
							<v-text-field
							  name="log"
							  id="log"
							  flat
							  :value="logMessage"
							  disabled
							  textarea
							  multi-line
							  rows="25"
							  style="color: white;"
							>
							</v-text-field>					
						</v-layout>
	  				</v-flex>
  		  		</v-layout>
	  		</v-flex>
	  	</v-layout>
	</v-container>
</template>

<script>
import Request from '../assets/js/Request.js'

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
			isAuctioneer: this.$store.getters.isAuctioneer,
			currentBid: 0,
			products: [
				{
					name: "Pencil",
					price: 0,
				},
			],
			status: "open", //status: open, closed, nodecline, noaccept
			activity: [],
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
		if(this.isAuctioneer){
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

	button {
		height: 5em;
		width: 100%;
	}
</style>
