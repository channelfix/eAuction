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
				    <v-spacer></v-spacer>
		 			<v-toolbar-items class="hidden-sm-and-down">
	 				  <p> 
	 				  	Credits: {{credits}} 
	 				  </p>
				      <v-dialog v-model="dialog" persistent max-width="500px">
				        <v-btn slot="activator" flat>Add more credits?</v-btn>
				        <v-form class="form">
				        	<v-card>
					          	<v-card-title>
					            	<span class="headline">Purchase Credits</span>
					          	</v-card-title>				          
					          	<v-card-text>				          	
					            	<v-container grid-list-md>
					              	<v-layout wrap>
					                	<v-flex xs12 sm12 md12>
						                  	<v-text-field 
						                  		label="Input amount here"
						                  		type="number"
						                  		v-model="add_credits"
						                  		id="creditID"
						                  	></v-text-field>
					                	</v-flex>
					              	</v-layout>
					            </v-container>
					          	</v-card-text>
					          	<v-card-actions>
						            <v-spacer></v-spacer>
						            <v-btn color="blue darken-1" flat @click.native="dialog = false">Close</v-btn>
						            <v-btn color="blue darken-1" flat @click="addCredits">Save</v-btn>
					          	</v-card-actions>
					        </v-card>
			          	</v-form>				        
				      </v-dialog>
				      <v-btn 
				      	flat
						v-if="$store.getters.isAuctioneer"
						@click="createLive"
			      	  >Create Livestream
			          </v-btn>
				    </v-toolbar-items>
			 	</v-toolbar>
		 	</v-container>
		 	<!-- <v-dialog v-model="warningModal" persistent max-width="290">
		      <v-card>
		        <v-card-title class="headline">Auction Seesion Warning</v-card-title>
		        <v-card-text>You are leaving your auction session. All your progress will be lost.</v-card-text>
		        <v-card-actions>
		          <v-spacer></v-spacer>
		          <v-btn color="primary" flat @click.native="warningModal = false">Leave</v-btn>
		          <v-btn color="primary" flat @click.native="warningModal = false">Return</v-btn>
		        </v-card-actions>
		      </v-card>
		    </v-dialog> -->
		 	<router-view>
		 	</router-view>		
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

	    		<v-list-tile
	    			@click="browse()"
	    		>
	    			<v-list-tile-action>
	    				<v-icon>
	    					search
	    				</v-icon>
	    			</v-list-tile-action >
	    			<v-list-tile-content>
	    			  <v-list-tile-title>
	    			  	<p class="subheading">Browse</p>
	    			  </v-list-tile-title>
	    			</v-list-tile-content>
	    		</v-list-tile>

	    		<v-list-tile
	    			@click="signOut"
	    		>
	    			<v-list-tile-action>
	    				<v-icon>
	    					exit_to_app
	    				</v-icon>
	    			</v-list-tile-action >
	    			<v-list-tile-content>
	    			  <v-list-tile-title>
	    			  	<p class="subheading">Sign Out</p>
	    			  </v-list-tile-title>
	    			</v-list-tile-content>
	    		</v-list-tile>
	    	</v-list>
	  	</v-navigation-drawer>
	  	<v-snackbar
          :timeout="alertbar.timeout"	       
          bottom
          right	          
          v-model="alertbar.snackbar"
	    >
	        {{ alertbar.text }}
        <v-btn flat color="amber darken-3" @click.native="alertbar.snackbar = false">Close</v-btn>
        </v-snackbar>
	</v-layout>
</template>

<script>
import Home from './Home'
import Request from '../assets/js/Request.js'
export default {
	name: 'PagesNavigation',
	data(){
		return {
			dialog: false,
			showNav: false,
			currentRoute: "",
			toolbarIcon: "menu",
			username: "",
			current_credits: "",
			add_credits: "",
			pages: [
				{
					title: "Home",
					icon: "home",
					path: {
						name: 'Home'
					},
				},
				{
					title: "Profile",
					icon: "account_box",
					path: {
						name: 'Profile',
					},
				},
			],
			alertbar: {
				snackbar: false,
				y:'top',
				x: null,
				text: '',
				timeout: 4000,
			},
			warningModal: false,
		}
	},

	computed: { 
		credits() {
			return this.$store.getters.getCredits
		} 
	},
	methods: {
		browse() {
			this.$router.push({
	          name: 'Explore'
	        })
		},
		route(path) {
			let currentRoute = this.$route.name

			if (path.name == "Profile") {
				path.params = {
					username: this.username,
				}
			}
			
			if (path.name == currentRoute) {
				this.showNav = false;
			} else {
				this.$router.push(path);
			}
		},
		navigate() {
			if (this.toolbarIcon == "arrow_back"){
				this.$router.go(-1);
			} else {
				this.showNav = true;
			}
		},
		signOut() {
			let request = new Request();
			request.post("/login/logout/", {}, 
			(response)=>{
				this.$router.go(0);	
			});			
		},
		createLive() {
			this.$router.push({
				name: 'Create-Live'
			})
		},
		addCredits() {
			// this.$store.commit("addCredits", 500)
			let request = new Request();
			let formdata = new FormData();
			this.dialog = !this.dialog;
			this.alertbar.text = "Successfully added " + this.add_credits + " credits!";
			this.alertbar.snackbar = true;
			// formdata.set('amount', this.$store.getters.getCredits)
			formdata.set('amount', this.add_credits)
			request.post("/profile/update_credits/", formdata,
			 (response)=>{
				this.$store.commit('addCredits', response.data.total_credit.credit_amount__sum)
			});
		},
	},
	watch: {
		'$route' (to,from) {
			/*if(from.name == "Auction")
				this.warningModal = true;
			*/
			this.currentRoute = this.$route.name;
			if(this.currentRoute == "Auction"
			){
				this.toolbarIcon = "arrow_back";
			}else{
				this.toolbarIcon = "menu";
			}
		}
	},
	mounted() {
		this.currentRoute = this.$route.name;
		this.username = this.$store.getters.getUsername;
	}
}
</script>

<style scoped>
</style> 