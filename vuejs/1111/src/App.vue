<template>
  <div id="app">
    <h1>Taehun Youtube Project</h1>
    <the-search-bar></the-search-bar>
    <video-detail></video-detail>
    <video-list></video-list>
  </div>
</template>

<script>
import TheSearchBar from "@/components/TheSearchBar"
import VideoDetail from "@/components/VideoDetail"
import VideoList from "@/components/VideoList"
export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoDetail,
    VideoList,
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
