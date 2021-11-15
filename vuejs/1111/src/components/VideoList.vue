<template>
  <div id="VideoList">
    <h1>videolist</h1>
    <video-list-item
    v-for="(vedio, idx) in searchResult"
    :key="idx"
    :vedio="vedio"
    >

    </video-list-item>
  </div>
</template>

<script>
import VideoListItem from "@/components/VideoListItem"
export default {
  name : "VideoList",
  data: function(){
    return {
    }
  },
  components : {
    VideoListItem
  },
  computed: {
    searchResult: function() {
      return this.$store.getters.searchResult
    }
  }
}
</script>

<style>

</style>