<template>
  <div class="home mt-5" >
    <MovieList v-infinite-scroll="loadMore" infinite-scroll-disabled="busy" infinite-scroll-distance="100" v-if="display == 'list' " :movies="movies" :user="user" />
  </div>
</template>

<script>
import MovieList from '@/components/movies/MovieList'
import router from '@/router'
import VueJwtDecode from 'vue-jwt-decode'
import axios from 'axios'

// https://chulsoo-back-end.herokuapp.com/

const BASE_URL =  process.env.VUE_APP_BASE_URL
const MOVIE_URL = BASE_URL +'api/v1/movies/list/'

export default {
  name: 'home',
  components: {
    MovieList,
  },
  data() {
    return {
      movies: [],
      genres: '',
      show: false,
      display: 'list',
      token: '',
      options: Object, 
      page: 1,
      busy: false,
    }
  },
  methods:{
    logout() {
      this.$session.destroy()
      router.push({name: 'login'})
    },
    loadMore() {
      this.busy = true
      console.log(this.page)
      axios.get(MOVIE_URL+`?page=${this.page}`, this.options)
      .then(res=>{
        this.movies= this.movies.concat(res.data.results)
        this.page++
        this.busy = false
        if(res.data.next === null){ 
          this.busy = true
        }     
      })
    }
    
  },
  watch: {
      movies: function() {
      }
  },
  computed: {
    user() {
      return VueJwtDecode.decode(this.$session.get('jwt'))
    },
  },
  mounted(){
    this.token = this.$session.get('jwt')
    this.options = {
      headers: {
      Authorization: 'JWT ' + this.token
      }
    }    
  }
}
</script>

<style scoped>

</style>