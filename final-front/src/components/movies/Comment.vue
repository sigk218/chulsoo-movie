<template>
  <div>
    <v-textarea
    append-outer-icon="comment"
    class="mx-2"
    label="댓글을 입력하세요"
    rows="1"
    v-model="comment"
    @keyup.enter="submit"></v-textarea>
    <p v-for="comment in this.movie.rating_set" :key="comment.id">{{ comment.content }} | {{ comment.user.username }}</p>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from 'vue-jwt-decode'
const Rating_URL = 'http://127.0.0.1:8000/api/v1/Rating/'
const MOVIE_URL = 'http://127.0.0.1:8000/api/v1/movies/'

export default {
  name: 'MovieDetail',
  props:{
      movie:{
          type: Object,
      },
  },
  data(){
    return{
      comment:'',
      headers: {
        headers:{
            Authorization: 'JWT ' + this.$session.get('jwt')
        }
      }
    }
  },
  methods:{
    submit(){
    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
    
    let form = new FormData()
    form.append('content', this.comment)
    form.append('score', 10)
    form.append('user', this.user.user_id)
    form.append('movie', this.movie.id)
    
    axios.post(`${Rating_URL}`,form, this.headers)
    .then(res=>{
      this.comment = ''
      console.log(res)
    })
    axios.get(`${MOVIE_URL}${this.movie.id}/`,this.headers)
    .then(res=>{
      this.movie = res.data
    })
    }
  },
  mounted() {
  },
  computed: {
      user(){
      return VueJwtDecode.decode(this.$session.get('jwt'))
      },
  },
}

</script>

<style>

</style>