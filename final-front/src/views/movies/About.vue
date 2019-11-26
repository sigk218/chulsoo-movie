<template>
 <v-card
    max-width="450"
    class="mx-auto"
  >
    <v-list>
    <v-list-item v-for="item in items" :key="item.title">
        <v-list-item-avatar>
        <v-icon>mdi-magnify</v-icon>
        </v-list-item-avatar>
         <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
         </v-list-item-content>
    </v-list-item>
    </v-list>
 </v-card>
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