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
		let div = document.getElementById('livestream')
		let opentokClient = document.createElement('script')
		opentokClient.setAttribute('src','https://static.opentok.com/v2/js/opentok.min.js')
		div.appendChild(opentokClient)

		if(this.isAuctioneer){
			this.axios.get('http://localhost:8000/livestream/auctioneer/')
			.then((response) => {
				this.opentokCloud = response.data

				this.apiKey = this.opentokCloud.api_key
				this.sessionId = this.opentokCloud.session_id
				this.token = this.opentokCloud.token

				console.log('ApiKey: ' + this.apiKey)
				console.log('Session ID: ' + this.sessionId);
				console.log('Token: ' + this.token);

				let session, publisher;
				let hasPublish = false;
				let xhttp;

				if(OT.checkSystemRequirements() == 1){ // Check if this browser supports WebRTC.
					console.log('This browser supports WebRTC.');
					session = OT.initSession(this.apiKey, this.sessionId);

					session.connect(this.token, function(error) { // Check if the client has successfully connected to the session.
						if(error)
							console.log('Cannot connect to the session.');
						else{
							console.log('Connected to the session.');

							// Create a publisher for exposing the video to other client who is also connected to the same session.
							publisher = OT.initPublisher('publisher', {insertMode: "append"}); 
						}
					});
				}
				else
					console.log('This browser does not support WebRTC.');
			})
		}else{
			this.axios.get('http://localhost:8000/livestream/bidder/')
			.then((response) => {
				this.opentokCloud = response.data

				this.apiKey = this.opentokCloud.api_key
				this.sessionId = this.opentokCloud.session_id
				this.token = this.opentokCloud.token

				console.log('ApiKey: ' + this.apiKey)
				console.log('Session ID: ' + this.sessionId);
				console.log('Token: ' + this.token);


				let session;

				if(OT.checkSystemRequirements() == 1){ // Check if this browser supports WebRTC.
					console.log('This browser supports WebRTC.');
					session = OT.initSession(this.apiKey, this.sessionId);

					session.connect(this.token, function(error) { // Check if this client is connected to the session.
						if(error)
							console.log('Cannot connect to the session.'); // Display Message: client has successfully connected to the session.
						else
							console.log('Connected to the session'); // Display Message: client has failed connect to the session.		
					});

					session.on("streamCreated", function(event) { // Check if the stream has created in a certain session.

						// Accept the exposed video who is connected to the same session.
						session.subscribe(event.stream, 'subscriber', {inserMode:'append', width:'50%', height:'50%'}); 
						console.log('Successfully subscribe');
					});


					session.on("streamDestroyed", function(event) {	
						console.log('Failed to subscribe');
					});
				}
				else // Failed to launch the livestream.
					console.log('This browser does not support WebRTC.');
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
			console.log(this.status);
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
			console.log(msg);
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
