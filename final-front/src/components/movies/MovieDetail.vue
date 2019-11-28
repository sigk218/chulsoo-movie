<template>
<v-container>
  <v-btn icon @click="closeWindow">
    <v-icon>
      mdi-close
    </v-icon>
  </v-btn>
  <div class="d-flex flex-col">
    <img :src="movie.image" :alt="movie.title" width="300" height="400px">
    <div>
      <h1>{{ movie.title }}</h1>
      <h2>{{ movie.subtitle }}</h2>
      <p> 평점 : {{ movie.userRating }}</p>
      <p>감독 : <span v-for="director in movie.directors" :key="director.id">{{ director.peopleNm }}</span></p>
      <p> 네이버 {{ movie.naver_price }}</p>
      <p> 유투브 {{ movie.youtube_price }}</p>
    <p>출연진
      <v-sheet
      :opacity=0.46
      elevation="100"
      max-width="400"
      max-height="100"
      >
      <v-slide-group
        v-model="model"
        show-arrows
      >
        <v-slide-item
          v-for="actor in movie.actors"
          :key="actor.id"
          v-slot:default="{ active, toggle }"
        >
        <v-row
            class="fill-height"
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
  <v-row>
    <!-- <v-container >{{ movie.description }}</v-container> -->
  </v-row>
  
</v-container>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'MovieDetail',
  components: {
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