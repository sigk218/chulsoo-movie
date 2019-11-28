<template>
<div>
    <v-card-text>
    <v-form>
      <h3>Required</h3>
      <v-text-field
        v-model="name"
        :error-messages="nameErrors"
        :counter="30"
        label="username(required)"
        required
        @input="$v.name.$touch()"
        @blur="$v.name.$touch()"
      ></v-text-field>
      <v-text-field
        v-model="email"
        :error-messages="emailErrors"
        label="E-mail(required)"
        required
        @input="$v.email.$touch()"
        @blur="$v.email.$touch()"
      ></v-text-field>
      <v-text-field
            v-model="password"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show1 ? 'text' : 'password'"
            name="input-10-1"
            label="Password(required)"
            hint="At least 8 characters"
            counter
            @click:append="show1 = !show1"
          ></v-text-field>

        <h3>Options</h3>
        <v-text-field
        v-model="firstname"
        :counter="20"
        label="First Name"
        @input="$v.names.$touch()"
        @blur="$v.names.$touch()"
      ></v-text-field>
      
      <v-text-field
        v-model="lastname"
        :counter="20"
        label="Last Name"
        @input="$v.names.$touch()"
        @blur="$v.names.$touch()"
      ></v-text-field>
    </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="primary" @click="SignUp">SignUp</v-btn>
      <v-btn @click="clear">clear</v-btn>

    </v-card-actions>
</div>
</template>

<script>
  import { validationMixin } from 'vuelidate'
  import { required, maxLength, email } from 'vuelidate/lib/validators'
  import router from '@/router'
  import axios from 'axios'

  export default {
    name: 'LoginForm',
    mixins: [validationMixin],

    validations: {
      name: { required, maxLength: maxLength(30) },
      email: { required, email },
      select: { required },
      names: {maxLength: maxLength(20)},
      checkbox: {
        checked (val) {
          return val
        },
      },
    },
    data: () => ({
      name: '',
      email: '',
      firstname: '',
      lastname: '',
      select: null,
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
      SignUp() {

      axios.defaults.xsrfCookieName = 'csrftoken'
      axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
      if (!this.firstname) {
        this.firstname = 'none'
      }
      if (!this.lastname) {
        this.lastname = 'none'
      }

      axios.post('http://127.0.0.1:8000/rest-auth/registration/', 
      {username: this.name,
      email: this.email,
      password1: this.password,
      password2: this.password,
      first_name: this.firstname,
      last_name: this.lastname,})
      .then(res => {
        console.log('회원가입성공')
        console.log(res)
        const token = res.data.token
        this.$session.start()
        this.$session.set('jwt', token)
        router.push('/')
        alert(`환영합니다! ${this.name}님`)
      }).catch(err => {
        console.log('회원가입실패')
        console.log(err)
        })
      }
    }
  
  }
</script>

<style>
</style>