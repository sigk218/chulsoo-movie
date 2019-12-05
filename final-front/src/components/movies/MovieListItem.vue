<template>
<div class="ma-3">
   <v-hover v-slot:default="{ hover }">
     <v-card
      :elevation="hover ? 12 : 2"
      :class="{ 'on-hover': hover }"
      >
        <v-img
        :src="movie.image"
        width="200px"
        class="d-flex align-center"
        @click="overlay = !overlay"
        ></v-img>
     </v-card>
  </v-hover>
    <v-overlay class="overflow-y-auto" :absolute="absolute" :opacity="opacity" :value="overlay" :z-index="zIndex">
    <MovieDetail @close-Window="overlay=false" :movie="movie" :overlay="overlay"></MovieDetail>
  </v-overlay>
</div>
</template>

<script>
import MovieDetail from './MovieDetail'

export default {
    name: 'MoveListItem',
     data: () => ({
      show: false,
      transparent: 'rgba(255, 255, 255, 0)',
      absolute: false,
      opacity: 0.7,
      overlay: false,
      zIndex: 5,
    }),
    components: {
        MovieDetail
    },
    props: {
        movie:{
            type: Object,
            required: true,
        }    
    },
    methods:{

    },

}
</script>

<style>
.v-card {
  transition: opacity .4s ease-in-out;
}

.v-card:not(.on-hover) {
  opacity: 0.7;
 }

.show-btns {
  color: rgba(255, 255, 255, 1) !important;
}
</style>