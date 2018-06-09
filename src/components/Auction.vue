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
					    <div class="screen" id="publisher"></div>
					    <div class="screen" id="subscriber"></div>
		  		  	</div>
		  		  	<Auctioneer 
		  		  		v-if="$store.getters.getUsername == $route.params.auctioneer"
						:currentProductName="products[0].name"
	  		  		>
		  		  	</Auctioneer>
		  		  	<Bidder 
		  		  		v-else
	  		  			:currentProductName="products[0].name"
	  		  		>
	  		  		</Bidder>
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
							align-center
						>
							<v-flex 
								md6
							>
								<v-layout
									pa-3
									align-center
									justify-center
								>
									<span class="headline">{{ products[0].name }}</span>
								</v-layout>
							</v-flex>
							<v-flex 
			  					md6
		  					>
		  						<v-layout
									align-center
									justify-center
									class="amber darken-1"
									pa-3
								>
									<span class="headline">Current Bid: &#8369 {{currentBid}}</span>
		  						</v-layout>
		  						<v-layout
									align-center
									justify-center
									class="amber darken-1"
									pa-3
								>
									<span class="headline">Minimum Bid: &#8369 {{products[0].minimum_price}}</span>
		  						</v-layout>
			  				</v-flex>
  						</v-layout>
	  				</v-flex>
	  				<v-flex
						md2
						class="green darken-3"
						v-if="highestBidder != ''"
	  				>
	  					<v-layout
							align-center
							justify-center
							pa-1
	  					>
							<span class="headline">Highest Bidder: {{highestBidder}}</span>
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
									<template v-for="log of logs">
										<v-list-tile dark>
											<v-list-tile-content>{{log.message}}</v-list-tile-content>
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
import Auctioneer from './Auctioneer'
import Bidder from './Bidder'

let logThread;
let request = new Request();
let session = null;

export default {
	name: "Auction",
	components: {Auctioneer, Bidder},
	data(){
		return{
			currentBid: 0,
			highestBidder: '',
			products: [{
				name: '',
				minimum_price: '',
			}],
			status: "open", //status: open, closed, nodecline, noaccept
			logs: [],
		}
	},
	mounted: function(){
		let formdata = new FormData();
		formdata.set('auction_id', this.$route.params.id);

		request.post('/livestream/product_list/', formdata, 
			(response)=>{
				this.products = response.data.product_list;	
				this.currentBid = this.products[0].minimum_price;
			}
		)

		logThread = setInterval(
			() => {
				if(session != null){
					// constantly ask from the server for new log 
					let latestId = -1;
					let auction_id = this.$route.params.id;

					if(this.logs.length > 0){
						latestId = this.logs[0].id;
					}

					let formdata = new FormData();

					formdata.set('auction_id', auction_id);
					formdata.set('log_id', latestId);


					request.post('/livestream/show_logs/', formdata, 
						(response)=>{
							let latestLogs = response.data.logs;

							for(let i = 0; i < latestLogs.length; i++){
								this.logs.splice(0, 0, latestLogs[i]); //insert before
							}
						}
					);
				}
			},
			1000
		)
	},
	methods: {
		startLiveStream(){
			let role = "bidder";
			if(this.$store.getters.getUsername == this.$route.params.auctioneer){
				role = "auctioneer";
			}

			let formdata = new FormData();

			formdata.set('auction_id', this.$route.params.id);
			formdata.set('is_auctioneer', (role == "auctioneer")?true:false);

			request.post('/livestream/initiate_auction/', formdata, 
				(response) => {
					let opentokCloud = response.data

					let apiKey = opentokCloud.api_key
					let sessionId = opentokCloud.session_id
					let token = opentokCloud.token

					let publisher;

					if(OT.checkSystemRequirements() == 1){ // Check if this browser supports WebRTC.
						session = OT.initSession(apiKey, sessionId);

						session.connect(token, function(error){
							if(role == "auctioneer"){
								publisher = OT.initPublisher('publisher', 
									{
										insertMode: 'append', 
										width: "100%", 
										height: "100%"
									});

							    session.publish(publisher);
							}
						});

						session.on("streamCreated", function(event) { // Check if the stream has created in a certain session.
							// Accept the exposed video who is connected to the same session.
							if(role == "bidder"){
								session.subscribe(event.stream, 'subscriber', 
									{
										insertMode:'append', 
										width:'100%', 
										height:'100%'
									}); 				
							}		
						});


						session.on("sessionDisconnected", (event)=>{
							clearInterval(logThread)
						})
				}
			})
		},
		endAuction(){
			// put end livestream here
			if(session != null){
				session.disconnect();
			}
		
			let formdata = new FormData();
			formdata.set('auction_id', this.$route.params.id);

			request.post('/livestream/end_auction/', formdata, 
			(response)=>{
				this.$router.push({
					name: 'Home',
				})
			});
		},
		sendLog(log){
			let today = new Date();
			let time = today.getHours()+":"+today.getMinutes()+" "+today.getMonth()+"/"+today.getDay()+"/"+today.getFullYear();

			// time format hr:min month/day/year

			let formdata = new FormData();

			formdata.set('auction_id', this.$route.params.id);
			formdata.set('logs', log);
			formdata.set('time', time);

			request.post('/livestream/store_logs/', formdata, ()=>{});
		},
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

	.screen{
		height: 100%;
	}

	.logbox {
		overflow: scroll;
		height: 800px;
	}
</style>
