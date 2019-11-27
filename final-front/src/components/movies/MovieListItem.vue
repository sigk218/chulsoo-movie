<template>
<div class="ma-3">
  <a @click="movieSelected">
   <v-hover v-slot:default="{ hover }">
            <v-card
              :elevation="hover ? 12 : 2"
              :class="{ 'on-hover': hover }"
            >
              <v-img
                :src="movie.image"
                width="200px"
                class="d-flex align-center"
              >
                <v-card-title class="d-flex justify-center">
                        <v-icon
                          :class="{ 'show-btns': hover }"
                          x-large
                        >
                          mdi-play
                        </v-icon>
                </v-card-title>
              </v-img>
              
            </v-card>
          </v-hover>
          </a>
</div>
</template>

<script>
// import MovieDetail from './MovieDetail'

export default {
     data: () => ({
      show: false,
      transparent: 'rgba(255, 255, 255, 0)',
    }),
    name: 'MoveListItem',
    components: {
        // MovieDetail
    },
    props: {
        movie:{
            type: Object,
            required: true,
        }    
    },
    methods:{
      movieSelected() {
        this.$emit('selectedMovie', this.movie)
      },
    }
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