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
					    <div class="screen" id="screenView"></div>
		  		  	</div>
		  		  	<Auctioneer 
		  		  		v-if="$store.getters.getUsername == $route.params.auctioneer"
						:currentProductName="products[currentProductIdx].name"
						:status="status"
	  		  			:minimumBid="minimumBid"
	  		  		>
		  		  	</Auctioneer>
		  		  	<Bidder 
		  		  		v-else
	  		  			:minimumBid="minimumBid"
	  		  			:currentProductName="products[
	  		  			currentProductIdx].name"
	  		  			:status="status"
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
									<span class="headline">{{ products[currentProductIdx].name }}</span>
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
									<span class="headline">Standing Bid: &#8369 {{standingBid}}</span>
		  						</v-layout>
		  						<v-layout
									align-center
									justify-center
									class="amber darken-1"
									pa-3
								>
									<span class="headline">Minimum Bid: &#8369 {{minimumBid}}</span>
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
										<v-list-tile dark :style="log.style">
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

let logThread = null;
let request = new Request();
let session = null;

export default {
	name: "Auction",
	components: {Auctioneer, Bidder},
	data(){
		return{
			standingBid: 0,
			minimumBid: 0,
			highestBidder: '',
			products: [{
				name: '',
				minimum_price: '',
			}],
			currentProductIdx: 0,
			status: "not live", // not live, item hold, open bidding, hold bidding, no bid, item closed
			logs: [],
		}
	},
	mounted: function(){
		let formdata = new FormData();
		formdata.set('auction_id', this.$route.params.id);

		request.post('/livestream/product_list/', formdata, 
			(response)=>{
				this.products = response.data.product_list;	
				this.standingBid = this.products[0].minimum_price;
				this.minimumBid = this.products[0].minimum_price;
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
							console.log(response.data.logs);
							this.handleLogs(response.data.logs);
						}
					);
				}
			},
			1000);
	},
	methods: {
		startLiveStream(){
			let role = "bidder";
			if(this.$store.getters.getUsername == this.$route.params.auctioneer){
				role = "auctioneer";
			}

			if(role == "auctioneer"){
				this.status = "item hold";
			}

			let formdata = new FormData();

			formdata.set('auction_id', this.$route.params.id);
			formdata.set('is_auctioneer', (role == "auctioneer")?true:false);

			request.post('/livestream/initiate_auction/', formdata, 
				(response) => {
					console.log(response);
					let opentokCloud = response.data

					let apiKey = opentokCloud.api_key
					let sessionId = opentokCloud.session_id
					let token = opentokCloud.token

					let publisher;

					if(OT.checkSystemRequirements() == 1){ // Check if this browser supports WebRTC.
						session = OT.initSession(apiKey, sessionId);

						session.connect(token, function(error){
							if(role == "auctioneer"){
								publisher = OT.initPublisher('screenView', 
									{
										insertMode: 'append', 
										width: "100%", 
										height: "100%"
									});

							    session.publish(publisher);
								this.sendLog("Auction session has started");
							}
						});

						session.on("streamCreated", (event) => { // Check if the stream has created in a certain session.
							// Accept the exposed video who is connected to the same session.

							if(role == "bidder"){
								session.subscribe(event.stream, 'screenView', 
									{
										insertMode:'append', 
										width:'100%', 
										height:'100%'
									}); 				
							}		
						});

						if(role == "bidder"){
							session.on("streamDestroyed", ()=>{
								clearInterval(logThread);
							})
						}
				}
			})
		},
		endAuction(){
			// put end livestream here
			clearInterval(logThread);
			if(session != null){
				session.disconnect();
			}
			
			let formdata = new FormData();
			formdata.set('auction_id', this.$route.params.id);

			request.post('/livestream/end_auction/', formdata, 
			(response)=>{
				this.sendLog("Auction session has ended");
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
		handleLogs(latestLogs){
			for(let i = 0; i < latestLogs.length; i++){
				let style = {
					backgroundColor: "black",
				};
				
				let msg = latestLogs[i].message;

				if(msg.match("^(.*)\\sis\\sclosed\\sfor\\sauction$")){
					this.status = "item closed";
					style.backgroundColor = "red";
				}else if(msg.match("^Minimum\\sbid\\sset\\sto\\s(.*)$")){
					this.minimumBid = parseInt(msg.substring(msg.indexOf("to")+3, msg.length));
					this.status = "open bidding";
					style.backgroundColor = "orange";
				}else if(msg.match("Moved\\sto\\snext\\sitem")){
					this.currentProductIdx++;
					this.minimumBid = this.products[this.currentProductIdx].minimum_price;
					this.standingBid = this.minimumBid;
					this.status = "item hold";
					style.backgroundColor = "brown";
				}else if(msg.match("Auction\\sfor\\s(.*)\\sis\\sopen")){
					this.status = "open bidding"
					style.backgroundColor = "green";
				}else if(msg.match("Auction\\ssession\\shas\\sstarted")){
					this.status = "item hold"
					style.backgroundColor = "orange";
				}else if(msg.match("^(.*)\\sbid\\s(.*)\\sfor\\s(.*)$")){
					this.highestBidder = msg.substring(0, msg.indexOf("bid")-1);
					this.standingBid = parseInt(msg.substring(msg.indexOf(" bid ")+5, msg.indexOf(" for ")));
					this.minimumBid = this.standingBid;
					this.status = "hold bidding"
					style.backgroundColor = "green";
				}else if(msg.match("Auction\\ssession\\shas\\sended")){
					clearInterval(logThread);
				}

				this.logs.splice(0, 0, Object.assign(latestLogs[i], {style})); //insert before
			}
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

	.screen{
		height: 100%;
	}

	.logbox {
		overflow: scroll;
		height: 800px;
	}
</style>
