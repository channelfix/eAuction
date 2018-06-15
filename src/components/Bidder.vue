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
						  :disabled="!bid.open"
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
				open: false,
				rules: [
					v=> {
						if(this.status == "open bidding"){
							let ret;
							let credits = this.$store.getters.getCredits;

							if(v >= this.minimumBid && v <= credits){
								this.bidButton.open = true;
								ret = true;
							}else {
								this.bidButton.open = false;

								if(v > this.$store.getters.getCredits){
									ret =  "Insufficient credits";
								}else{
									ret = "Must be higher than minimum bid";
								}
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

			let formdata = new FormData();
			this.$parent.$parent.displaySnackBar("Bid successfully subtracted "+this.bid.value+ " from credits");
			// formdata.set('amount', this.$store.getters.getCredits)
			formdata.set('amount', -this.bid.value);
			request.post("/profile/update_credits/", formdata,
			 (response)=>{
				this.$store.commit('addCredits', response.data.total_credit.credit_amount__sum)
			});

			this.$parent.sendLog(log);
		}
	},
	watch:{
		status(){
			this.bidButton.open = (this.status == "open bidding");
			this.bid.open = (this.status == "open bidding");
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
