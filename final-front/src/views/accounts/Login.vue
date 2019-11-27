<template>
<v-content>
  <v-layout align-center justify-center>
    <h1 class="font-weight-thin display-4" style="position: absolute; margin-top: 80px">ChulSoo Movie</h1>
    </v-layout>
      <v-container
        fluid
        fill-height
      >
        <v-layout
          align-center
          justify-center
        >
          <v-flex
            xs12
            sm8
            md4
          >
            <v-card class="elevation-12">
              <v-toolbar
                color="primary"
                dark
                flat
              >
                <button @click="changeForm('login')"><v-toolbar-title>Login</v-toolbar-title></button>
                <v-toolbar-title><pre> | </pre></v-toolbar-title>
                <button @click="changeForm('signup')"><v-toolbar-title>Register</v-toolbar-title></button>
                
                <v-spacer></v-spacer>
              </v-toolbar>
  <LoginForm v-if="status == 'login'"/>
  <SignUpForm v-else/>
</v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
</template>

<script>
  import LoginForm from '@/components/accounts/LoginForm.vue'
  import SignUpForm from '@/components/accounts/SignUpForm.vue'
  import router from '@/router'

  export default {
    name: 'Login',
    components: {
      LoginForm,
      SignUpForm
    },
    data() {
      return {
        status: 'login'
      }
    },
    methods: {
      changeForm(data) {
        this.status = data
      },

      loggedIn() {
      this.$session.start()
      if (this.$session.has('jwt')) {
        router.push({name: 'Home'}, () => {})
        }
      },
    },
    watch: {
      status,
    },
    mounted() {
      this.loggedIn()
    }
    }
</script>

<style>
</style>