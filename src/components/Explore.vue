<template>
  <div class="div-container">
      <div align-center row wrap>
        <div>
          <v-text-field         
            label="Looking for someone?"
            v-model="browseQuery"
            id="queryID"
            @keyup = "browse"
            dont-fill-mask-blanks
          ></v-text-field>
        </div> 
        <v-btn 
          v-for="tag of tags" 
          :disabled="(active == tag)?true:false" 
          dark 
          depressed 
          @click="query_tag(tag)"
        > 
          {{ tag }} 
        </v-btn>
        <v-btn dark depressed @click="clearAll()"> Clear </v-btn>
      <v-layout
        v-if="results.length != 0"
        row
        wrap
        style="width: inherit;"
      >
        <v-flex
          v-for="result in results"
          xs12
          @click="goprofile(result.username)"
        >
            <v-card 
              :hover="true"              
              color="transparent"
              style="width: 100%;"              
            >
              <v-layout 
                row 
                wrap
                justify-end
              ></v-layout>
              <v-card-title primary-title>
                <div>
                  <p style="margin: 0px;" class="headline">{{result.username}}</p>
                  <div>{{result.first_name}} {{result.last_name}}</div>
                  <v-chip
                    medium
                    label
                    outline color="secondary" 
                    v-for="tag in result.tags"
                    disabled
                    style="margin-left: 0px;"
                  >
                  <v-icon left>label</v-icon>
                  {{tag}}
                  </v-chip>
                </div>
              </v-card-title>
            </v-card>      
        </v-flex>
      </v-layout>
    </div>
  </div>
</template>

<script>
  import Request from '../assets/js/Request.js'

  export default{
    name: 'Explore',
    data(){
      return {
        browseQuery: "",
        browseFilter: "",
        results: [],
        tags: ["Collectibles", "Antiques", "Novel", "Vehicles", "Jewelry"],
        keyTimeout: null,
        active: '',
      }
    },
    methods: {
      goprofile(username) {
        this.$router.push({
          name: 'Profile',
          params: {
            username: username
          }
        })
      },
      clearAll() {
        this.browseQuery = "";
        this.browseFilter = "";
        this.active = ""
        this.results = [];
      },
      query_tag(tag) {
        this.browseFilter = tag;
        this.active = tag;
        this.search();  
      },
      browse() {
        clearInterval(this.keyTimeout)
        this.keyTimeout = setTimeout(()=> {
          this.search();
        }, 500);
      },
      search() {
        this.results = [];
        let queries = this.browseQuery.trim();
        let filter = this.browseFilter.trim();

        if (!queries && !filter) {
          return;
        }

        let request = new Request();
        let formdata = new FormData();
        formdata.set('browseQuery', queries);
        formdata.set('browseFilter', filter);
        request.post('/browse/', formdata,
          (response)=>{            
            for(var index in response.data){
              this.results.push(response.data[index]);
            }
          });    
      },
    },
  }

</script>

<style scoped>
  .div-container{
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    flex-direction: column;
  }

  #queryID{
    width: 400px;
  }
</style>

