<template>
  <div id="VideoList">
    <ul v-if="videoList.length">

      <video-list-item 
        v-for="(video, index) in videoList" 
        :key="index"
        :video-item="video"
        @selected="selectVideo"
        >
        </video-list-item>

    </ul>

  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {

  name:"VideoList",

  data: function(){
    return{
    }
  },
  
  components:{
    VideoListItem
    
  },

  props: {
    videoList: Array,
  },

  methods: {
    selectVideo: function(data) {
      this.$emit('selected', data)
    }
  }
}
</script>

<style>
#VideoList {
  border: 1px solid yellow
}
</style>