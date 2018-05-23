<template>
	<v-container
		fluid
		fill-height
	>
	  	<v-layout
			row
	  	>
	  		<v-flex md7> <!-- left -->
	  		  	<v-layout column>
		  		  	<div class="livestream">
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
									<button class="red btn">Decline</button>	
								</v-layout>
		  		  			</v-flex>
		  		  			<v-flex 
								md6
	  		  				>
								<v-layout
									align-center
									pa-3
								>
									<button class="green btn">Accept</button>	
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
							<button class="white" style="color: black;">CLEAR</button>						
						</v-layout>
	  				</v-flex>
  		  		</v-layout>
	  		</v-flex>
	  	</v-layout>
	</v-container>

</template>

<script>
function formatDecimal(num) {
	return parseFloat(Math.round(num * 100) / 100).toFixed(2)
}

export default {
	name: "Auction",
	data(){
		return{
			currentBid: 0,
			products: [
				{
					name: "Pencil",
					price: 0,
				},
			],
			activity: [],
		}
	},
	computed: {
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
	.livestream {
		height: 700px;
		background-color: black;
	}

	

	button {
		height: 5em;
		width: 100%;
	}
</style>
