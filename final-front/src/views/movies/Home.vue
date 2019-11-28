<template>
  <div class="home">
    <Navbar :user="user" @submitted="submit" :options="options" />
    <MovieList v-if="display=='list'" :movies="movies" :user="user" />
  </div>

</template>

<script>
import Navbar from '@/components/movies/Navbar'
import MovieList from '@/components/movies/MovieList'
import router from '@/router'
import VueJwtDecode from 'vue-jwt-decode'
import axios from 'axios'

const MOVIE_URL = 'http://127.0.0.1:8000/api/v1/movies/'
export default {
  name: 'home',
  components: {
    MovieList,
    Navbar,
  },
  data() {
    return {
      movies: '',
      genres: '',
      show: false,
      display: 'list',
      token: '',
      options: '',
    }
  },
  methods:{
    logout() {
      this.$session.destroy()
      router.push({name: 'login'})
    },
    submit(data){
        this.movies = data
        this.display = 'list'
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
  console.log(VueJwtDecode.decode(this.token))
  axios.get(MOVIE_URL, this.options)
    .then(res=>{
      this.movies = res.data 
    })
  }
}
</script>

<style scoped>

</style>