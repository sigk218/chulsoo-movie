<template>
<div class="mt-10">
  <v-container>
    <v-row>
    <MovieListItem :movie="movie" v-for="movie in movies" @selectedMovie="movieSelected" :key="movie.id"/>
    </v-row>
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
    },
    user: {
      type: Object,
    }
  },
  methods: {
    movieSelected(data) {
      this.$emit('selectedMovie', data)
    }
  }
}
</script>

<style>

</style>