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
			<label>Description</label>
			<input type="text" 
				   id="productDescField"
				   v-model="product.description"
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
					description: '',
				},
				tagList: [],
				selectedTag: '',
			}
		},
		methods: {
			createProduct() {
				alert('Product created')
			}
		},
		mounted() {
			let request = new Request();

			request.get('/profile/tag_list/', 
			(response) => {
				console.log(response)
				this.tagList = response.data.tags
			})
		}
	}
</script>

<style type="text/css">
	
</style>

