<template>
 <div class="about my-12">
   <v-container>
   <h1>내정보</h1>
   <!-- <h1>아이디 : {{ userDetail.id }}</h1> -->
   <h1>아이디 : {{ userDetail.username }}</h1>
   <h1>가입날짜 : {{ userDetail.date_joined }}</h1>
   <h1>이메일 : {{ userDetail.email }}</h1>
   <h1>이름 : {{ userDetail.first_name }}</h1>
   <h1>성 : {{ userDetail.last_name }}</h1>
   <!-- <h1>{{ userDetail.followers }}</h1>
   <h1>{{ userDetail.followings }}</h1> -->
   
   <h1>활성여부 : {{ userDetail.is_active }}</h1>
   <h1>관리자 : {{ userDetail.is_staff }}</h1>
   <!-- <h1>{{ userDetail.like_movie }}</h1>
   <h1>{{ userDetail.rating_set }}</h1> -->
   <h1 class="display-3 mt-10">당신이 좋아할만한 영화</h1>
   <v-carousel
    cycle
    height="400"
    hide-delimiter-background
    show-arrows-on-hover
    mt-5
  >
    <v-carousel-item
      v-for="movie in this.recMovies"
      :key="movie.id"
    >
      <v-sheet
        height="100%"
        color="transparent"
      >
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <img :src="movie.image" width="300px" @click="overlay1 = !overlay1">
          <v-overlay class="overflow-y-auto" :absolute="absolute" :opacity="opacity" :value="overlay1" :z-index="zIndex">
          <MovieDetail @close-Window="overlay1=false" :movie="movie" :overlay1="overlay1"></MovieDetail>
          </v-overlay>
        </v-row>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
   <h1 class="display-3 mt-10">당신이 싫어할만한 영화</h1>
   <v-carousel
    cycle
    height="400"
    hide-delimiter-background
    show-arrows-on-hover
  >
    <v-carousel-item
      v-for="movie in this.derMovies"
      :key="movie.id"
    >
      <v-sheet
        height="100%"
        color="transparent"
      >
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <img :src="movie.image" width="300px" @click="overlay2 = !overlay2">
          <v-overlay class="overflow-y-auto" :absolute="absolute" :opacity="opacity" :value="overlay2" :z-index="zIndex">
          <MovieDetail @close-Window="overlay2=false" :movie="movie" :overlay2="overlay2"></MovieDetail>
          </v-overlay>
        </v-row>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
</v-container>
 </div>
</template>

<script>
import router from '@/router'
import MovieDetail from '@/components/movies/MovieDetail.vue'
import VueJwtDecode from 'vue-jwt-decode'
import axios from 'axios'


const BASE_URL =  process.env.VUE_APP_BASE_URL
const MOVIE_URL = BASE_URL + 'api/v1/accounts/'
export default {
    name: 'About',
    components: {
      MovieDetail
    },
    data(){
      return {
            show: false,
            userDetail: '',
            token: '',
            options: '',
            model: null,
            movies: '',
            myMovies: new Array,
            recMovies: new Array,
            derMovies: new Array,
            transparent: 'rgba(255, 255, 255, 0)',
            absolute: false,
            opacity: 0.46,
            overlay2: false,
            overlay1: false,
            zIndex: 5,
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
    }
    // console.log(this.user)
    axios.get(MOVIE_URL+`${this.user.user_id}/`, this.options)
    .then(res => {
      this.userDetail = res.data
      this.movies = res.data.like_movie
      for (let i = 0; i < this.movies.length; i++) {
          // console.log(this.movies[i])
        axios.get(MOVIE_URL+`${this.movies[i]}/`, this.options)
        .then(res => {
          this.myMovies.push(res.data)
        }).catch(err=>{
          console.log(err)
        })
      }
    }).catch(err => {
      console.log(err)
    })

    axios.get(MOVIE_URL+`recommendation/${this.user.user_id}/`, this.options)
    .then(res => {
      // console.log(res.data)
      for (let i=0; i < 10; i++) {
        axios.get(`${res.data[i]}/`, this.options)
        .then(res => {
          // console.log(res.data)
          this.recMovies.push(res.data)
        })
      }
      
      for (let j=res.data.length - 1; j > res.data.length - 10; j--) {
        axios.get(MOVIE_URL+`${res.data[j]}/`, this.options)
        .then(res => {
          // console.log(res.data)
          this.derMovies.push(res.data)
        })
      }
    })
  }
  }
</script>
<style>

</style>