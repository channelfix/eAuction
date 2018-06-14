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
			md12
				>
				<v-layout
					align-center
					pa-3
				>
					<v-flex
						md8
					>
						<v-text-field
						  label="Input bid"
						  v-model="bid.value"
						  type="number"
						  :rules="bid.rules"
						></v-text-field>
					</v-flex>
					<v-flex
						md4
					>
						<button
							block
							:class="bidButton.style"
							:disabled="!bidButton.open"
							@click="placeBid"
						>
							Bid
						</button>
					</v-flex>	
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
		minimumBid: Number,
	},
	data(){
		return {
			bid: {
				value: 0,
				rules: [
					v=> {
						if(this.status == "open bidding"){
							let ret;
							if(v >= this.minimumBid){
								this.bidButton.open = true;
								ret = true;
							}else {
								this.bidButton.open = false;
								ret =  "Must be higher than minimum bid";
							}

							this.bidButton.style = (this.bidButton.open)?'green':'grey'

							return ret;
						}else{
							return "Can not bid yet";
						}
					}
				],
			},
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
			let log = currentUser+" bid "+this.bid.value+" for "+this.currentProductName;

			this.$parent.sendLog(log);
		}
	},
	watch:{
		status(){
			console.log(this.status);
			this.bidButton.open = (this.status == "open bidding");
			this.bid.value = (this.status == "open bidding")?this.minimumBid:0;
			this.bidButton.style = (this.bidButton.open)?"green":"grey";
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
</style>
