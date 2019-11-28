<template>
<v-container>
  <div class="d-flex flex-col">
    <img class="ma-3" :src="movie.image" :alt="movie.title" width="300" height="400px">
    <div>
      <h1>{{ movie.title }}</h1>
      <h2>{{ movie.subtitle }}</h2>
      <p> 평점 : {{ movie.userRating }}</p>
      <p>감독 : <span v-for="director in movie.directors" :key="director.id">{{ director.peopleNm }}</span></p>
      <a style="text-decoration:none" :href=" movie.naver_link "><v-btn color="success" class="mx-1">{{ movie.naver_price }}</v-btn></a>
      <a style="text-decoration:none" :href=" movie.youtube_link "><v-btn color="error" class="mx-1">{{ movie.youtube_price }}</v-btn></a>
    <p></p>
    <p>출연진
      <v-sheet
      :opacity=0.46
      elevation="100"
      max-width="400"
      max-height="100"
      color="transparent"
      >
      <v-slide-group
        show-arrows
      >
        <v-slide-item
          v-for="actor in movie.actors"
          :key="actor.id"
          v-slot:default="{ active, toggle }"
        >
        <v-row
          height="200"
          width="100"
          class="ma-4"
          align="center"
          justify="center"
          >{{ actor.peopleNm }}
          </v-row>
        </v-slide-item>
      </v-slide-group>
      </v-sheet>
    </p>
    </div>
  </div>
    <v-btn icon @click="closeWindow">
    <v-icon>
      mdi-close
    </v-icon>
  </v-btn>
  <v-row>
    <p>설명 여기 와야댐</p>
  </v-row>
  <MovieLike :movie="movie"/>
  <Comment :movie="movie"/>
</v-container>
</template>

<script>
// import axios from 'axios'
import MovieLike from './MovieLike'
import Comment from './Comment'

export default {
  name: 'MovieDetail',
  components: {
    MovieLike,
    Comment,
  },
  props:{
      movie:{
          type: Object,
      },
      overlay:{
        type: Boolean,
      }
  },
  data(){
    return {
      main: '',

    }
  },
  methods:{
    closeWindow(){
      this.$emit('close-Window')
    }
  },
  computed: {

  },
  mounted(){

  }
}
</script>

<style>

</style>