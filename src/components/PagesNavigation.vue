<template>
	<v-layout 
		fill-height
	>
		<v-container 
			fluid
		>
			<v-container
				fluid
			>
			  	<v-toolbar 
		  			color="amber darken-3"
				>
				    <v-toolbar-side-icon 
				    	@click="showNav = !showNav"
			   		>
			   		</v-toolbar-side-icon>
				    <v-toolbar-title>Home</v-toolbar-title>
				    <v-spacer></v-spacer>
			 	</v-toolbar>
		 	</v-container>
		 	<router-view></router-view>
		</v-container>
		<v-navigation-drawer 
			temporary 
			absolute 
			v-model="showNav">
	    	<v-list>
	    		<v-toolbar class="transparent">
					<v-toolbar-title>Username Here</v-toolbar-title>
	    		</v-toolbar>
	    	</v-list>
	  	</v-navigation-drawer>
	</v-layout>
</template>

<script>
import Home from './Home'

export default {
	name: 'PagesNavigation',
	data(){
		return {
			showNav: false,
		}
	}
}
</script>

<style scoped>
</style> 