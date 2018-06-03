<template>
	<v-container
		fluid
	>
		<v-text-field
		  label="Title"
		  v-model="title"
		></v-text-field>
		<v-text-field
		  label="Description"
		  v-model="description"
		></v-text-field>
		<p>Products</p>
		<div>
			<div>
				<v-text-field
				  label="Name"
				  solo
				  v-model="product.name"
				></v-text-field>
				<v-text-field
				  label="Price"
				  solo
				  v-model="product.minimumPrice"
				></v-text-field>
			</div>
			<button @click="createLivestream">Create</button>
		</div>
	</v-container>
</template>

<script type="text/javascript">
import Request from '../assets/js/Request.js'

export default {
	name: 'CreateLiveStream',
	data() {
		return {
			username: this.$store.getters.getUsername,

			title: '',
			description: '',
			product: {
				name: '',
				minimumPrice: ''
			},
		}
	},
	methods: {
		createLivestream() {
			let request = new Request();
			let formdata = new FormData();

			formdata.set('title', this.title);
			formdata.set('description', this.description);
			formdata.set('product_name', this.product.name);
			formdata.set('product_price', this.product.minimumPrice);

			request.post('/livestream/create_livestream/', formdata,
			(response) => {
				alert(response.data)
				this.$router.push({					
					name: 'Home'
				});
			})
		}
	}
}

</script>