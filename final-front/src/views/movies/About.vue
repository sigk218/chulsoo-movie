<template>
 <div class="about">
<v-app-bar absolute> 
      <!-- <v-icon>mdi-magnify</v-icon>   -->
      <v-toolbar-title>ChulSoo MOVIE</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        
        <v-btn text @click="searchmode = !searchmode">
        <v-icon>mdi-magnify</v-icon>
        </v-btn>
        <v-text-field 
        style="margin-top: 4.5px" 
        v-show="searchmode" 
        label="search" 
        single-line outlined
        v-model="searchWord"
        @keyup.enter="submit"
        ></v-text-field>
        <v-btn text>
        <v-icon color="primary">mdi-heart</v-icon>보고싶어요
        </v-btn>
      </v-toolbar-items>
      <!-- <template v-if="$vuetify.breakpoint.smAndUp"> -->
        <v-menu offset-y>
      <template v-slot:activator="{ on }">
        <v-btn
          color="primary"
          dark
          v-on="on"
          @click="show = !show"
        >
          {{ user.username }}
          <v-icon >{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
        </v-btn>
      </template>
      <v-list>
        <v-list-item>
          <v-list-item-title><a href="/about/" style="text-decoration: none"><v-btn text>My page</v-btn></a></v-list-item-title>
        </v-list-item>
        <v-list-item>
          <v-list-item-title><v-btn text @click="logout">Logout</v-btn></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  
      <!-- </template> -->
    </v-app-bar>

 </div>
</template>

<script>
  export default {
    data() {
        return {
            items : [
                { title: '마이페이지', link: 'mypage'},
                { title: 'follower', link: 'follower'},
            ]
        }
    }
  }
</script>
<style>

</style>