<template>
<v-container>
  <SignUpForm />
  <h1>나오냐</h1>
  <LoginForm/>
  </v-container>
</template>

<script>
import SignUpForm from '@/components/accounts/SignUpForm.vue'
import LoginForm from '@/components/accounts/LoginForm.vue'

export default {
  name: 'SignUp',
  components: {
    SignUpForm,
    LoginForm
  }
}
</script>

<style>

</style>