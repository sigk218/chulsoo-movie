<template>
  <div class="home">
    <MovieList v-if="showlist" :movies="movies" :user="user" @selectedMovie="movieSelected" />
    <MovieDetail v-else :movie="movie" :user="user" />
  </div>

</template>

<script>
const axios = require('axios')
// @ is an alias to /src
import MovieList from '@/components/movies/MovieList'
import MovieDetail from '@/components/movies/MovieDetail'
import router from '@/router'
import VueJwtDecode from 'vue-jwt-decode'

const MOVIE_URL = 'http://127.0.0.1:8000/api/v1/movies/'
export default {
  name: 'home',
  components: {
    MovieList,
    MovieDetail,
  },
  data(){
    return {
      movies: [],
      genres: [],
      show: false,
      showlist: true,
      movie: '',
      searchmode: false,
      searchWord:'',
      token: '',
      options: '',
    }
  },
  methods:{
    logout() {
      this.$session.destroy()
      router.push({name: 'login'})
    },
    movieSelected(data) {
      this.showlist = false
      this.movie = data
    },
    submit(){
      this.options.params.title = this.searchWord
      axios.get(MOVIE_URL, this.options)
      .then(res=>{
        this.movies = res.data
      })
      this.searchmode = false
      this.searchWord= ''
    },
  },
  computed: {
    user() {
      return VueJwtDecode.decode(this.$session.get('jwt'))
    }
  },
  mounted(){
    // const user_id = jwtDecode(token).user_id
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
      // console.log(res.data)
    })
  }
}
</script>

<style scoped>

</style>