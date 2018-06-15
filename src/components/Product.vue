<template>
	<div>
		<label>Create Product</label>

		<p>
			<label>Name</label>
			<input 
				type="text" 
				id="productNameField" 
				v-model="product.name"
			>
		</p>
		
		<p>
			<label>Tags: </label>
			<select v-model="selectedTag">				
				<option v-for="tag in tagList">
					{{tag.name}}
				</option>				
			</select>
		</p>

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
				tagList: [],
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
					formdata.set('tag', this.selectedTag)
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

			// used to retrieve the tags in combo box
			request.get('/profile/tag_list/', 
			(response) => {				
				this.tagList = response.data.tags
			})

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

