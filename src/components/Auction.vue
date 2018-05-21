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
		  		  	<div class="box livestream">
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

<script>
export default {
	name: "Auction",
	data(){
		return{
			messages: [
				{
					name: 'Person',
					accepted: false,
				}
			],
		}
	},
}
</script>

<style scoped>
	.livestream {
		height: 700px;
		width: ;
	}

	button {
		height: 5em;
	}
</style>
