<template>
<v-container>
  <LoginForm />
</v-container>
</template>

<script>
  import LoginForm from '@/components/accounts/LoginForm.vue'

  export default {
    name: 'Login',
    components: {
      LoginForm
    }
  }
</script>

<style>
</style>