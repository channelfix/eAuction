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
				<v-text-field
				  label="Input bid"
				></v-text-field>
				<button
					:class="bidButton.style"
					:disabled="!bidButton.open"
				>
					Bid
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
	name: "Bidder",
	data(){
		return {
			bidButton: {
				style: {
					green: true,
					grey: false,
				},
				open: true,
			}
		}
	},
	mounted() {
		this.$parent.startLiveStream();
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
