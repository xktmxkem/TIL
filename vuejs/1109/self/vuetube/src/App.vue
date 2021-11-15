<template>
  <div id="app">
    <the-search-bar @search-data="getSearchData"></the-search-bar>
    <hr>
    <video-detail :select-item="selectItem"></video-detail>
    <hr>
    <video-list :video-list="results" @selected="selectVideo"> </video-list>
  </div>
</template>

<script>
import TheSearchBar from './components/TheSearchBar.vue'
import VideoList from './components/VideoList.vue'
import axios from 'axios'
import VideoDetail from './components/VideoDetail.vue'

export default {
  name: 'App',
  data: function(){
    return {
      searchData: '',
      results: [],
      selectItem: {},
    }
  },
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  methods: {
    getSearchData: function(data){
      this.searchData = data
      // search 이벤트가 발생했을때 axios 를 통해 요청을 보내고 결과를 받아옴
      axios({
        method: "get",
        url: "https://www.googleapis.com/youtube/v3/search",
        params: {
          part: "snippet",
          q: this.searchData,
          type: 'video',
          // apikey가 hardcoding 되어 있어서 public 정보에 노출될 수 있다.
          // 따라서 .env.local 로 따로 const 상수를 환경설정하여 
          // API KEY를 저장하고 이를 통해 받아 오도록 한다.
          key: process.env.VUE_APP_YOUTUBE_API_KEY,
        }
      })
      .then(res => {
        // 검색 결과를 App.vue의 data에 저장
        this.results = res.data.items
        console.log(typeof(this.results))

      })
      .catch(err => {
        console.log(err)
      })
    },

    // 자식(VidioListItem)에서 선택된 데이터를 받아옴 
    selectVideo: function(data){
      this.selectItem = data
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
