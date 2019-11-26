<template>
<div>
  <p>어쩌구 님이 좋아한 영화</p>
  <v-container row>
    <MovieListItem :movie="movie" v-for="movie in movies" :key="movie.id"/>
  </v-container>
</div>
</template>

<script>
import MovieListItem from './MovieListItem.vue'
export default {
  name: 'MovieList',
  components:{
    MovieListItem,
  },
  props:{
    movies:{
      type: Array,
      required: true,
    }
  }
}
</script>

<style>

</style>