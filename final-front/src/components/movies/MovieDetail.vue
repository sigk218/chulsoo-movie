<template>
<v-container justify="center">
  <img :src="movie.image" :alt="movie.title" width="300px" height="400px">
  <h1>{{ movie.title }}</h1>
  <h2>{{ movie.subtitle }}</h2>
  <p>{{ movie.userRating }}</p>
  <p>{{ movie.acotors }}</p>
  <p>{{ movie.directors }}</p>
  <p>{{ movie.genres }}</p>
  <p>{{ movie.description }}</p>
  <p>{{ movie.naver_price }}</p>
  <p>{{ movie.youtube_price }}</p>
</div>
</v-container>

<script>
export default {
  name: 'MovieDetail',
  components: {
  },
  props:{
      movie:{
          type: Object,
      }
  },
  data(){
    return {
      main: '',
    }
  },
  methods:{
    
  },
  computed: {
    
  },
  mounted(){

  }
}
</script>

<style>

</style>