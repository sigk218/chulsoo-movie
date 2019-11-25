<template>
  <v-app>
    <v-container>
    <router-link to="/">Home </router-link>
    <button v-if="loggedIn()" @click="logout">Logout</button>
    <div class="d-inline" v-else>
    <router-link to="/login">Login </router-link>
    <router-link to="/login">SignUp</router-link>
    </div>
    <router-view></router-view>
    </v-container>
  </v-app>
</template>

<script>
import router from '@/router'

export default {
  name: 'home',
  data() {
    return {
    }
  },
  methods: {
    logout() {
      this.$session.destroy()

      // NavigationDuplicated 를 핸들링 하기 위해 () => {} 를 추가함.
      // 위의 에러는 현재 페이지와 push하려는 페이지가 같을 때 발생하는 에러.
      this.$router.push({name: 'login'}, () => {})
    },
    loggedIn() {
      this.$session.start()
      if (!this.$session.has('jwt')) {
        router.push({name: 'login'}, () => {});
        return false
      } else {
        return true
      }
    },
  },
  mounted() {
  this.loggedIn()
  }
}
</script>