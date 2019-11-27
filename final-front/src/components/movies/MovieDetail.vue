<template>
<v-container class="mt-10">
  <h1>
    {{ movie.title }}
  </h1>
</v-container>
</template>

<script>
import axios from 'axios'

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
//     // const user_id = jwtDecode(token).user_id
//     const token = this.$session.get('jwt')
//     const options = {
//       headers: {
//       Authorization: 'JWT ' + token
//     }
//   }    
//   CORS error 남.. 
  axios.get(this.movie.link)
    .then(res=>{
      console.log(res.data)
    }).catch(err => {
        console.log(err)
    })
    console.log(this.movie)
  }
}
</script>

<style>

</style>