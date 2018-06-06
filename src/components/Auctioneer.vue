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
					class="red"
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
					class="green"
					@click="startAuction"
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

let request = new Request();

export default {
	name: 'Auctioneer',
	props: {
		status: String,
	},
	data(){
		return{
			opentokCloud: '',
			apiKey: '',
			sessionId: '',
			token: '',
			accept: {
				open: true,
				style: {
					green: true,
					grey: false,
				}
			}
		}
	},
	methods: {
		startAuction() {
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
			}else if(this.status == "closed"){
				this.accept.open = false;

			this.accept.style.green = this.accept.open;
			this.accept.style.grey = !this.accept.open;
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
</style>
