<template>
	<v-flex 
  		md4
  	>
  		<v-layout 
  			fill-height
			row
			wrap
			class="box"
		>
  			<v-layout 
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
	  			<v-flex 
					md4
				>
					<v-layout 
						align-center
						pa-3
					>
						<button 
							class="red"
						>
							Close auction for current item
						</button>	
					</v-layout>
  				</v-flex>
  				<v-flex 
					md5
				>
					<v-layout 
						align-center
						justify-center
						pa-3
					>
						<v-text-field
							label="Bid Increase"
						>
							
						</v-text-field>
						<button class="halfsize green">Increase</button>
					</v-layout>
  				</v-flex>
  				<v-flex 
					md3
				>
					<v-layout 
						align-center
						justify-center
						pa-3
					>
						<button class="green">Move to next item</button>
					</v-layout>
  				</v-flex>
  				<v-flex 
					md3
				>
					<v-layout 
						align-center
						justify-center
						pa-3
					>
						<button class="green">Open auction current item</button>
					</v-layout>
  				</v-flex>
	  		</v-layout>
  		</v-layout>
  	</v-flex>
</template>

<script>
import Request from '../assets/js/Request.js'

let request = new Request();

export default {
	name: 'Auctioneer',
	methods: {
		startAuction() {
			this.$parent.startLiveStream();
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

	.halfsize {
		width: 50%;
	}
</style>
