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
				    	@click="navigate"
			   		>
			   			<v-icon>{{toolbarIcon}}</v-icon>
			   		</v-toolbar-side-icon>
				    <v-toolbar-title>{{currentRoute}}</v-toolbar-title>
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
					<v-toolbar-title>{{username}}</v-toolbar-title>
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
	props: {
		username: String,
	},
	data(){
		return {
			showNav: false,
			currentRoute: "",
			toolbarIcon: "menu",
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
			let currentRoute = this.$route.name
			
			path.params = {
				username: this.username,
			}

			if(path.name == currentRoute)
				this.showNav = false;
			else
				this.$router.push(path);
		},
		navigate(){
			if (this.toolbarIcon == "arrow_back"){
				this.$router.go(-1);
			}else {
				this.showNav = true;
			}
		}
	},
	watch: {
		'$route' (to,from) {
			this.currentRoute = this.$route.name;
			if(this.currentRoute == "Auction" || 
			   this.currentRoute == "Edit Profile"
			){
				this.toolbarIcon = "arrow_back";
			}else{
				this.toolbarIcon = "menu";
			}
		}
	},
	mounted() {
		this.currentRoute = this.$route.name;

		if(this.username == undefined){
			this.$router.push({
				name: 'LogIn'
			})
		} 
	}
}
</script>

<style scoped>
</style> 