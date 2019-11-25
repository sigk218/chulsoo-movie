<template>
<div>
  <h1>무비리스트입니다</h1>
  {{ movies }}
</div>
</template>

<script>
export default {
  name: 'MovieList',
  components:{

  },
  props:{
    movies:{
      type: Array,
      required: true,
    }
  }
}
</script>

<style>

</style>