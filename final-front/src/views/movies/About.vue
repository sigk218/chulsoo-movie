<template>
 <div class="about">
 </div>
</template>

<script>
import router from '@/router'
import VueJwtDecode from 'vue-jwt-decode'
// import axios from 'axios'

  export default {
    name: 'About',
    data(){
      return {
            show: false,
        }
    },
    methods:{
    logout() {
      this.$session.destroy()
      router.push({name: 'login'})
    },
    movieSelected(data) {
      this.showlist = false
      this.movie = data
    },
  },
  computed: {
    user() {
      return VueJwtDecode.decode(this.$session.get('jwt'))
    }
  },
  mounted(){
    // const user_id = jwtDecode(token).user_id
    this.token = this.$session.get('jwt')
    this.options = {
      headers: {
      Authorization: 'JWT ' + this.token
    },
    params: {
      title: ''
    }
  }    
  }
  }
</script>
<style>

</style>