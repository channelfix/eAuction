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
			v-model="showNav"
			width="400"
		>
	    	<v-list
				three-line
	    	>
	    		<v-toolbar class="transparent">
					<v-toolbar-title>Username Here</v-toolbar-title>
	    		</v-toolbar>
	    		<v-list-tile
					v-for="page in pages"
	    			@click="route(page.path)"
	    		>
	    			<v-list-tile-action>
	    				<v-icon>
	    					{{page.icon}}
	    				</v-icon>
	    			</v-list-tile-action >
	    			<v-list-tile-content>
	    			  <v-list-tile-title>
	    			  	<p class="subheading">{{page.title}}</p>
	    			  </v-list-tile-title>
	    			</v-list-tile-content>
	    		</v-list-tile>
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
			pages: [
				{
					title: "Home",
					icon: "home",
					path: {
						name: 'Home'
					},
				},{
					title: "Profile",
					icon: "account_box",
					path: {
						name: 'Profile',
					},
				},

			],

		}
	},
	methods: {
		route(path){
			let currentRoute = this.$router.app._route.name
			if(path.name == currentRoute)
				this.showNav = false;
			else
			this.$router.push(path);
		}
	}
}
</script>

<style scoped>
</style> 