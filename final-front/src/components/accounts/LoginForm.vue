<template>
<div>
   <v-card-text>
    <v-form @>
      
      <v-text-field
        v-model="name"
        :error-messages="nameErrors"
        :counter="30"
        label="Name"
        required
        @input="$v.name.$touch()"
        @blur="$v.name.$touch()"
      ></v-text-field>

      <v-text-field
            v-model="password"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show1 ? 'text' : 'password'"
            name="input-10-1"
            label="Password"
            hint="At least 8 characters"
            counter
            @click:append="show1 = !show1"
          ></v-text-field>
  <h3 class="red--text font-weight-thin" v-if="errors == 'on'">아이디 또는 비밀번호가 잘못되었습니다.</h3>
    </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="primary" @click="login">Login</v-btn>
      <v-btn @click="clear">clear</v-btn>

    </v-card-actions>
</div>
</template>

<script>
  import { validationMixin } from 'vuelidate'
  import { required, maxLength, email } from 'vuelidate/lib/validators'
  import router from '@/router'
  import axios from 'axios'
  const BASE_URL =  process.env.VUE_APP_BASE_URL
  const LOGIN_URL = BASE_URL + 'api-token-auth/'

  export default {
    name: 'LoginForm',
    mixins: [validationMixin],

    validations: {
      name: { required, maxLength: maxLength(30) },
      email: { required, email },
      select: { required },
      checkbox: {
        checked (val) {
          return val
        },
      },
    },
    data: () => ({
      name: '',
      email: '',
      select: null,
      errors: 'off',
      items: [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4',
      ],
      show1: false,
        show2: true,
        show3: false,
        show4: false,
        password: '',
        rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',
          emailMatch: () => ('The email and password you entered don\'t match'),
      
    },
    }),

    computed: {
      nameErrors () {
        const errors = []
        if (!this.$v.name.$dirty) return errors
        !this.$v.name.maxLength && errors.push('Name must be at most 10 characters long')
        !this.$v.name.required && errors.push('Name is required.')
        return errors
      },
      emailErrors () {
        const errors = []
        if (!this.$v.email.$dirty) return errors
        !this.$v.email.email && errors.push('Must be valid e-mail')
        !this.$v.email.required && errors.push('E-mail is required')
        return errors
      },
    },

    methods: {
      submit () {
        this.$v.$touch()
      },
      clear () {
        this.$v.$reset()
        this.name = ''
        this.email = ''
        this.password = ''
      },
      login() {
      axios.post(LOGIN_URL, {username: this.name, password: this.password})
      .then(res => {
        console.log(res)
        // start는 session id를 초기화 한다는 메소드임
        this.$session.start()
        this.$session.set('jwt', res.data.token)
        // this.$router == router
        router.push('/')
        console.log(this.$session)
      }).catch(err => {
        console.log(err)
        this.errors = 'on'
      }
      )
    }
    }}
</script>

<style>
</style>