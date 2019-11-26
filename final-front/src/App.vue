<template>
  <v-app>
    <v-container>
    <button v-if="loggedIn()" @click="logout">Logout</button>
    <div class="d-inline" v-else>
    </div>
    <router-view />
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
  },
  mounted() {
  this.loggedIn()
  }
}
</script>