<template>
  <div class="home">
      <v-app-bar absolute> 
      <!-- <v-icon>mdi-magnify</v-icon>   -->
      <v-toolbar-title>ChulSoo MOVIE</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        
        <v-btn text @click="searchmode = !searchmode">
        <v-icon>mdi-magnify</v-icon>
        </v-btn>
        <v-text-field 
        style="margin-top: 4.5px" 
        v-show="searchmode" 
        label="search" 
        single-line outlined
        v-model="searchWord"
        @keyup.enter="submit"
        ></v-text-field>
        <v-btn text>
        <v-icon color="primary">mdi-heart</v-icon>보고싶어요
        </v-btn>
      </v-toolbar-items>
      <!-- <template v-if="$vuetify.breakpoint.smAndUp"> -->
        <v-menu offset-y>
      <template v-slot:activator="{ on }">
        <v-btn
          color="primary"
          dark
          v-on="on"
        >
          {{ user.username }}
          <v-icon @click="show = !show">{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
        </v-btn>
      </template>
      <v-list>
        <v-list-item>
          <v-list-item-title><v-btn text>My page</v-btn></v-list-item-title>
        </v-list-item>
        <v-list-item>
          <v-list-item-title><v-btn text @click="logout">Logout</v-btn></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  
      <!-- </template> -->
    </v-app-bar>
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
        console.log(res)
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