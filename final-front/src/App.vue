<template>
  <v-app>
    <Navbar v-if="loggedIn()" :user="user" @submitted="submit" />
    <router-view />
  </v-app>
</template>

<script>
import Navbar from '@/components/accounts/Navbar'
import VueJwtDecode from 'vue-jwt-decode'
import router from '@/router'

export default {
  name: 'home',
  components: {
    Navbar,
  },
  data() {
    return {
      movies: ''
    }
  },
  methods: {
    logout() {
      this.$session.destroy()
      // NavigationDuplicated 를 핸들링 하기 위해 () => {} 를 추가함.
      // 위의 에러는 현재 페이지와 push하려는 페이지가 같을 때 발생하는 에러.
      router.push({name: 'login'}, () => {})
    },
    loggedIn() {
      this.$session.start()
      if (!this.$session.has('jwt')) {
        router.push({name: 'login'}, () => {})
        return false
      } else {
        return true
      }
    },
    submit(data){
        this.movies = data
    },
  },
  computed: {
    user() {
      return VueJwtDecode.decode(this.$session.get('jwt'))
    }
  },
  mounted() {
  this.loggedIn()
  }
}
</script>