<template>
	<div>
		<label>Create Product</label>

		<v-text-field
			label="Name"
			v-model="product.name"
		>
		</v-text-field>

		<label>Tags: </label>
		<v-flex xs6>
	        <v-select
	          :items="tagList"
	          v-model="selectedTag"
	          label="Select"
	          single-line
	        ></v-select>
     	 </v-flex>

		<button @click="createProduct">[Create Product]</button><br>

		<div>
			<label>My Records</label>
		</div>

		<div>
			<ul>
				<label>Name      Tags         Date Sold</label>
				<li v-for="product in products">
					{{product.products__name}} {{product.name}} 
					<div v-if="product.products__date_sold === null">
						unsold
					</div>
					<div v-else>
						{{product.products__date_sold}}
					</div>
				</li>
			</ul>
		</div>
			
	</div>
</template>

<script type="text/javascript">
import Request from '../assets/js/Request.js';

	export default{
		name: 'Product',
		data() {
			return {
				product: {
					name: '',					
				},
				tagList: [
					{text: "Collectibles"},
					{text: "Antiques"},
					{text: "Novel"},
					{text: "Vehicles"},
					{text: "Jewelry"}
				],
				selectedTag: '',
				products: []
			}
		},
		methods: {
			createProduct() {
				let request = new Request();
				let formdata = new FormData();

				// Check if all fields are filled.
				if((this.selectedTag && this.product.name) != "")
				{					
					formdata.set('tag', this.selectedTag.text)
					formdata.set('name', this.product.name)

					request.post('/profile/create_product/', formdata,
					(response) => {
						alert(response.data)
					})
				}					
			}
		},
		mounted() {
			let request = new Request();
			// used to retrieve the product details (name, tag name, and date sold)
			request.get('/profile/retrieve_product/',
			(response) => {				
				this.products = response.data.products
			})
		}
	}
</script>

<style>

</style>

