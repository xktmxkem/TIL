<template>
  <div @click="selectVideo">
    <hr>
    <img :src="videoItem.snippet.thumbnails.default.url" alt="썸네일">
    <p>{{ videoItem.snippet.title | unescapeTitle }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',


  props: {
    videoItem: Object,
  },
  // TEXT 에서 깨지는 문자열을 원래대로 돌리는 filter
  filters: {
    unescapeTitle: function (title) {
      return _.unescape(title)
    }
  },

  methods: {
    selectVideo: function(){
      //비디오가 클릭되면 부모 데이터로 알려준다.
      this.$emit('selected', this.videoItem)
    }
  }
}
</script>

<style>

</style>