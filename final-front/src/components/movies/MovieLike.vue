<template>
  <div>
    <v-btn icon @click="AddLike">
        <v-icon>{{ like ? 'mdi-thumb-up' : 'mdi-thumb-up-outline' }}</v-icon>
    </v-btn>

  </div>
</template>

<script>
import VueJwtDecode from 'vue-jwt-decode'
import axios from 'axios'
const BASE_URL =  process.env.VUE_APP_BASE_URL
const MOVIE_URL = BASE_URL+'api/v1/movies/'

export default {
    name: "MovieLike",
    data(){
    return {
        like: false,
        headers: {
            headers:{
                Authorization: 'JWT ' + this.$session.get('jwt')
            }
        }
        }
    },
    props:{
        movie:{
        type: Object,
        },
    },
    methods:{
        AddLike(){
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
            axios.post(`${MOVIE_URL}${this.movie.id}/user/${this.user.user_id}/`,{}, this.headers)
            .then(res=>{
                if (res.status === 200){
                    this.like = !this.like
                }
            })
        }
    },
    mounted(){
        axios.get(`${MOVIE_URL}${this.movie.id}/`,this.headers)
        .then(res=>{
            console.log(res.data.like_user)
            for(let v of res.data.like_user){
            if( this.user.user_id === v.id ){
                this.like = true
                }
            }
        }
        )
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


