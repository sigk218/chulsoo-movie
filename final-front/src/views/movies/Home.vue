<template>
  <div class="home">
      <v-app-bar absolute > 
      <v-icon v-model="platform">mdi-magnify</v-icon>  
      <v-toolbar-title>철수 MOVIE</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <button class="ma-2">
        <v-icon v-model="platform">mdi-magnify</v-icon>검색
        </button>
        <button class="ma-2">
        <v-icon v-model="platform">mdi-heart</v-icon>보고싶어요
        </button>
      </v-toolbar-items>
      <!-- <template v-if="$vuetify.breakpoint.smAndUp"> -->
        <v-btn>
          username
          <v-icon @click.native="show = !show">{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
        </v-btn>
      <!-- </template> -->
    </v-app-bar>
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
      show: false,
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

<style scoped>

</style>