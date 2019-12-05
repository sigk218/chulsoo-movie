<template>
  <div class="home mt-5">
    <MovieList v-if="display == 'list' " :movies="movies" :user="user" />
  </div>

</template>

<script>
import MovieList from '@/components/movies/MovieList'
import router from '@/router'
import VueJwtDecode from 'vue-jwt-decode'
import axios from 'axios'
const BASE_URL =  process.env.VUE_APP_BASE_URL
const MOVIE_URL = BASE_URL +'api/v1/movies/'

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
    }
  },
  methods:{
    logout() {
      this.$session.destroy()
      router.push({name: 'login'})
    },
    
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
    },
    params: {
      title: ''
    }
  }    
  // console.log(VueJwtDecode.decode(this.token))
  // console.log(this.token)
  axios.get(MOVIE_URL, this.options)
    .then(res=>{
      this.movies = res.data
      console.log(res.data)
    })
  }
}
</script>

<style scoped>

</style>