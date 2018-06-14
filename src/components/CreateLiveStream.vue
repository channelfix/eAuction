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

		<label>Thumbnail</label>
		<form>
			<input type="file" id="fileSelector" v-on:change="updateImageDisplay" />

			<div id="auction"/>
				<img :src="auctionPic" width="200" height="200" />
			</div>
		</form>

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
			<button @click="addProduct">Add Product</button><br><br>
			<button @click="createLivestream">Create</button>
		</div>
		<ul>
			<li v-for="name in productNames">
				{{name}}<br>
			</li>
		</ul>
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
			auctionPic: '',
			hasChangePic: false,
			imageFile: '',
			products: [],
			productNames: [],
			productPrices: [],
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
			formdata.set('product_name', this.productNames);
			formdata.set('product_minimum_price', this.productPrices);

			if(this.hasChangePic)
				formdata.append('imageFile', this.imageFile, this.imageFile.name)

			request.post('/livestream/create_livestream/', formdata,
			(response) => {
				let session = response.data
				let id = session.auction_id
				let auctioneer = session.auctioneer_username

				alert(session.message)

				this.$router.push({
					name: 'Auction',
					params: {
						id,
						auctioneer,
					}
				})
			})
		},

		addProduct() {
			this.productNames.push(this.product.name);
			this.productPrices.push(this.product.minimumPrice);
			alert('successfully add '+this.product.name);
		},
		isValidImageFormat: function(selectedFile) {
				if(selectedFile.type === 'image/jpg' || selectedFile.type === 'image/png' || selectedFile.type === 'image/jpeg')
					return true;
		},
		updateImageDisplay: function(e) {
			let file = e.target.files;

			// Check if the selected file exist.
			if(file.length == 1){
				if(this.isValidImageFormat(file[0])){
					// Update Image
					this.imageFile = file[0];
					this.hasChangePic = true;						
					this.auctionPic = window.URL.createObjectURL(this.imageFile);
				}
				else
					alert('Cannot import this file. Use only this following format (.jpg, .jpeg, or .png).');
			}
		},
	}
}

</script>