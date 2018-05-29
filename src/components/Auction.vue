<script type="text/javascript"> 

export default {
	name: "Auction",
	data(){
		return{
			// messages: [
			// 	{
			// 		name: 'Person',
			// 		accepted: false,
			// 	}
			// ],
			opentokCloud: '',
			apiKey: '',
			sessionId: '',
			token: '',
			isAuctioneer: this.$store.getters.isAuctioneer
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
				console.log(this.opentokCloud)

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
		}
	}
}
</script>



<template>
	<v-container
		fluid
		fill-height
	>
	  	<v-layout
			row
			wrap
	  	>
	  		<v-flex md7> <!-- left -->
	  		  	<v-layout column>
		  		  	<div class="box livestream" id="livestream">			  		  			  
					    <div id="publisher"></div>
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
									<v-btn
									block
									large
									color="error"
									>
										Decline
									</v-btn>
								</v-layout>
		  		  			</v-flex>
		  		  			<v-flex 
								md6
	  		  				>
								<v-layout
									align-center
									pa-3
								>
									<v-btn
										block
										large
										color="success"
									>
										Accept
									</v-btn>
								</v-layout>
		  		  			</v-flex>
		  		  		</v-layout> 
		  		  	</v-flex>
	  		  	</v-layout>
	  		</v-flex>
	  		<v-flex>  <!-- right -->
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
									<p class="headline">product name</p>
									<p class="headline">product name</p>
									<p class="headline">product name</p>
									<p class="headline">product name</p>
								</v-layout>
							</v-flex>
  						</v-layout>
	  				</v-flex>
	  				<v-flex 
	  					md1
  					>
  						<v-layout
							align-center
							justify-center
							class="amber darken-3"
						>
							<span class="headline">Current Bid: &#8369 0.00</span>
  						</v-layout>
	  				</v-flex>
	  				<v-flex md8
						class="grey darken-3"
	  				>
	  				</v-flex>
  		  		</v-layout>
	  		</v-flex>
	  	</v-layout>
	</v-container>
</template>




<style scoped>
	html{
		overflow-y: hidden;
	}

	.livestream{
		height: 700px;
		width: ;
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

	button {
		height: 5em;
	}
</style>
