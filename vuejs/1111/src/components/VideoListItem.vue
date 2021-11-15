<template>
  <div id="VideoListItem">
     <li>
    <img 
      :src="vedio.snippet.thumbnails.default.url" 
      alt="youtube thumbnail"
      @click="getDetail"
    >
    <p>{{ vedio.snippet.title}}</p>
    <hr>
  </li>
  </div>
</template>

<script>
export default {
  name : "VideoListItem",
  props:{
    vedio: Object
  },
  methods: {
    getDetail: function(){
      this.$store.dispatch('getDetail', this.vedio)
    }
  }
}
</script>

<style>

</style>