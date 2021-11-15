<template>
  <div>
    <div v-if="isShow">
      <iframe :src="videoUrl" frameborder="0"></iframe>
      <p>{{ selectItem.snippet.title | unescapeTitle}}</p>
      <p>{{ selectItem.snippet.description | unescapeTitle}}</p>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: "VideoDetail",

  data: function() {
    return{
    }
  },
  props: {
    selectItem: Object,
  },
  filters: {
      unescapeTitle: function (title) {
      return _.unescape(title)
    }
  },

  // 유튜브 스트링을 만들어서 보내주기 
  // 오브젝트는 length가 발생하지 않아서 로데쉬를 통해서 사용한다
  computed: {
    videoUrl: function(){
      if (_.isEmpty(this.selectItem)){
        return ''
      } else {
        return `https://www.youtube.com/embed/${this.selectItem.id.videoId}`
      }
    },
    // 전달된 데이터가 없으면 디테일 페이지는 보여줄 필요 없음.
    isShow: function() {
      return !_.isEmpty(this.selectItem)
    }
  }

}
</script>

<style>

</style>