<template>
	<v-container
		fluid
	>
		<v-text-field
		  label="Title"
		></v-text-field>
		<v-text-field
		  label="Description"
		></v-text-field>
		<p>Products</p>
		<div>
			<div>
				<v-text-field
				  label="Name"
				  solo
				></v-text-field>
				<v-text-field
				  label="Price"
				  solo
				></v-text-field>
			</div>
			<button>Add</button>
		</div>
	</v-container>
</template>

<script>
export default {
	name: 'CreateLiveStream',
}

</script>