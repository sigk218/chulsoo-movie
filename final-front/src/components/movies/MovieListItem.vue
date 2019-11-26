<template>
<v-card>
    <v-img :src="movie.image">
    </v-img>
    <v-card-title primary-title>
      <div>
        <div class="headline">Top western road trips</div>
        <span class="grey--text">1,000 miles of wonder</span>
      </div>
    </v-card-title>
    <v-card-actions>
      <v-btn flat>Share</v-btn>
      <v-btn flat color="purple">Explore</v-btn>
      <v-spacer></v-spacer>
      <v-btn icon @click.native="show = !show">
        <v-icon>{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
      </v-btn>
    </v-card-actions>
    <v-slide-y-transition>
      <v-card-text v-show="show">
        I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
      </v-card-text>
    </v-slide-y-transition>
</v-card>
    <!-- <div>
        <img :src="movie.image" alt="moive.name">
        <v-btn icon @click.native="show = !show">
            <v-icon>{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
        </v-btn>
    </div> -->
</template>

<script>
// import MovieDetail from './MovieDetail'
export default {
     data: () => ({
      show: false
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

    }
}
</script>

<style>

</style>