<template>
<div class="content-padding">
  <loading :active.sync="isLoading" 
        :can-cancel="true" 
        :is-full-page="fullPage"></loading>

  <section class="hero">
    <div class="hero-body">
      <h1 class="title is-3 has-text-centered"><strong><span class="blue-text">Online</span> <span class="orange-text">Stores</span></strong></h1>
    </div>
</section>
<div class="is-mobile columns">
  <div class="box column is-10 is-offset-1 is-lastprice">
      <div class="card">
        <div class="card-content">
          <div class="content">
             <p class="title is-5">Compare prices from <span class="jumia-text">Jumia</span>, <span class="jiji-text">Jiji</span>, <span class="konga-text">  Konga</span>, <span class="kara-text">Kara</span> and <span class="slot-text">Slot</span>.</p>
            <div class="field has-addons">
              <div class="control has-icons-left is-expanded">
              <input class="input" type="search"  v-on:keyup.enter="getResults" v-model="term" placeholder="Search from kara, konga, jiji, jumia, slot"/>
              <span class="icon is-medium is-left">
                <i class="fa fa-search"></i>
              </span>
              </div>
              <div class="control">
                <a v-on:click="getResults" class="button is-lastprice">GO</a>
              </div>
            </div>
          </div>
        </div>
        <footer class="card-footer" v-if="showfilter">
            <div class="column is-half-mobile is-half">
                <priceslide v-model="height.value" :ini-value="initialValue">
                      <div></div>
                </priceslide>
            </div>
            <div class="column is-half-mobile is-half">
              <p-check color="default" class="p-switch p-fill" value="jumia" v-model="checkedStores">Jumia</p-check>
              <p-check color="primary" class="p-switch p-fill" value="konga" v-model="checkedStores">Konga</p-check>
              <p-check color="success" class="p-switch p-fill" value="jiji" v-model="checkedStores">Jiji</p-check>
              <p-check color="info" class="p-switch p-fill" value="kara" v-model="checkedStores">Kara</p-check>
              <p-check color="warning" class="p-switch p-fill" value="slot" v-model="checkedStores">Slot</p-check>
            </div>
        </footer>
      </div>
</div>
</div>

<section class="column is-10 is-offset-1">
    <div class="row columns is-multiline">
      <template  v-for="(result,location) in searchResults">
        <searchresult @clicked="setUrl" @deleted="deleteElement(location)" :url="result.url" :image="result.image" :store="result.source" :title="result.title" :price="result.price"></searchresult>
      </template>
    </div>
</section>

</div>
  
</template>

<script>
  import Vue from 'vue';
  import Searchresult from '../components/Searchresult.vue';
  import Priceslide from '../components/Priceslide.vue';
  import Toasted from 'vue-toasted';
    import Loading from 'vue-loading-overlay';
    import 'vue-loading-overlay/dist/vue-loading.css';
    import PrettyCheck from 'pretty-checkbox-vue/check';
    Vue.use(Toasted);
    Vue.component('p-check', PrettyCheck);

export default {
  components : { Searchresult, Priceslide, Loading, PrettyCheck },
  data () {
    return {
      term : "",
      height: { value: [0,700000], min: 0, max: 700000 },
      showfilter: false,
      results: [],
      checkedStores: ['kara','jumia','jiji','konga','slot'],
      filterbyname: "",
      isLoading:false,
      fullPage:true,
    }
  },
  computed: {
    initialValue() {
      return [parseFloat(this.results[0].price), parseFloat(this.results[this.results.length -1 ].price)] ;
    },
    searchResults() {
          if (this.checkedStores.length == 0 ){
             var products = this.results;
          } else {
           var products = this.results.filter((product) => {
              return this.checkedStores.includes(product.source.toLowerCase());
            });
          }
          var priceranges = products.filter((product) => { return parseFloat(product.price) >= this.height.value[0] && parseFloat(product.price) <= this.height.value[1];});
          return priceranges.filter((pricerange) => {
            if (isNaN(this.filterbyname) || this.filterbyname == "" || this.filterbyname == null){
              return pricerange.title.toLowerCase().includes(this.filterbyname.toLowerCase());
            }
          });
        },
  },

  methods: {

    getResults() {
      this.loading = true;
          this.showfilter = false;
          this.results = [];
          this.isLoading = true;
          axios.get(window.location.href + 'search/' + this.term).then(response => {this.isLoading=false; this.loading = false; this.results = response.data.sort((a,b)=>parseFloat(a.price) - parseFloat(b.price)); this.showfilter=true; this.height.value[0] = parseFloat(this.results[0].price); this.height.value[1] = parseFloat(this.results[this.results.length -1 ].price); return this.results;}).catch(error => { this.isLoading=false; this.loading = false; return console.log(error);});
    },
    deleteElement(index) {
        Vue.toasted.show(this.results[index].title + " Deleted!",{position: 'bottom-right', theme: 'bubble', duration: 1000, singleton: true});
        this.results.splice(index, 1);
    },
    setUrl(args) {
                var urltovisit = window.location.href + 'visitstore/?url=' + args.url + '&store=' + args.store;
                this.isLoading=true;
                axios.get(urltovisit).then(response => {  this.isLoading=false; return window.location.href = response.data; }).catch(error => { this.isLoading=false; return console.log(error);});
    },
  }
}
</script>

<style>



    .button.is-lastprice:active, .button.is-lastprice.is-active {
    background-color: #212e57;
    border-color: transparent;
    color: #fff;
}
.button.is-lastprice:hover, .button.is-lastprice.is-hovered {
    background-color: #212e57;
    border-color: transparent;
    color: #fff;
}

.button.is-lastprice {
    background-color: #212e57;
    border-color: transparent;
    color: #fff;
}

</style>
