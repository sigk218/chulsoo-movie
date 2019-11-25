<template>
  <div class="home">
    <MovieList :movies="movies"/>
  </div>
</template>

<script>
const axios = require('axios')
// @ is an alias to /src
import MovieList from '@/components/movies/MovieList'

const MOVIE_URL = 'http://127.0.0.1:8000/api/v1/movies/'
export default {
  name: 'home',
  components: {
    MovieList,
  },
  data(){
    return {
      movies: [],
      genres: [],
    }
  },
  mounted(){
    // const user_id = jwtDecode(token).user_id
    const token = this.$session.get('jwt')
    const options = {
      headers: {
      Authorization: 'JWT ' + token
    }
  }    
  // console.log(token)
  axios.get(MOVIE_URL, options)
    .then(res=>{
      this.movies = res.data 
      // console.log(res.data)
    })
  }
}
</script>
