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
		 			<v-toolbar-items>
	 				  <v-layout
	 				  	align-center
	 				  	justify-center
	 				  >
	 				  	  <v-flex md4>
	 				  	  	<span> 
		 				  		Credits: {{credits}} 
		 				  	</span>
		 				  </v-flex>
		 				  <v-flex md8 fill-height>
		 				  	<v-btn block slot="activator" flat @click="()=>dialog=true">Add more credits?</v-btn>
		 			  	  	<v-dialog v-model="dialog" max-width="500px">				        
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
								                  		autofocus
								                  	></v-text-field>
								                  	<p class="headline">
								                  		Total Cost: {{ totalCost }}
								                  	</p>
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
		 			  	  </v-flex>
		 			  </v-layout>
				      <v-btn 
				      	flat
						v-if="$store.getters.isAuctioneer"
						@click="createLive"
			      	  >Create Livestream
			          </v-btn>
				    </v-toolbar-items>
			 	</v-toolbar>
		 	</v-container>
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
				},{
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
		},
		totalCost(){
			return this.add_credits * 2
		}
	},
	methods: {
		route(path){
			let currentRoute = this.$route.name

			if(path.name == "Profile"){
				path.params = {
					username: this.username,
				}
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
		},
		signOut(){
			let request = new Request();
			request.post("/login/logout/", {}, 
			(response)=>{
				this.$router.go(0);	
			});			
		},
		createLive(){
			this.$router.push({
				name: 'Create-Live'
			})
		},
		displaySnackBar(text){
			this.alertbar.text = text;
			this.alertbar.snackbar = true;
		},
		addCredits(){
			let request = new Request();
			let formdata = new FormData();
			
			this.dialog = !this.dialog;
			this.displaySnackBar("Successfully added " + this.add_credits + " credits!");
			formdata.set('amount', this.add_credits)
			request.post("/profile/update_credits/", formdata,
			 (response)=>{
				this.$store.commit('addCredits', response.data.total_credit.credit_amount__sum)
			});
		},
	},
	mounted() {
		this.currentRoute = this.$route.name;
		this.username = this.$store.getters.getUsername;
	}
}
</script>

<style scoped>
</style> 