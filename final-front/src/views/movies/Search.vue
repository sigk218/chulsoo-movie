<template>
  <div class="search mt-5">
    <MovieList v-if="display == 'list' " :movies="movies" :user="user" />
  </div>
</template>

<script>
import MovieList from '@/components/movies/MovieList'
import router from '@/router'
import VueJwtDecode from 'vue-jwt-decode'
import axios from 'axios'

const MOVIE_URL = 'http://127.0.0.1:8000/api/v1/movies/'

export default {
  name: 'home',
  components: {
    MovieList,

  },
  data() {
    return {
      movies: '',
      genres: '',
      show: false,
      display: 'list',
      options: '',
      token: '',
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
  mounted() {
    console.log(this.$route.params.word)
    this.token = this.$session.get('jwt')
    this.options = {
        headers: {
        Authorization: 'JWT ' + this.token
    },
    params: {
      title: this.$route.params.word
    }
  }    
  console.log(VueJwtDecode.decode(this.token))
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