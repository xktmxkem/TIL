<template>
  <div id="VideoDetail">
    <div id="area">
      <iframe id="vedio" :src="selectVedio" frameborder="0"></iframe>

    </div>
  </div>
</template>

<script>
export default {

  name :"VideoDetail",
  computed : {
    selectVedio: function() {
      const vedioId = this.$store.state.detailResult.id.videoId
      console.log(vedioId)
      return `https://www.youtube.com/embed/${vedioId}`
    }
  }
}
</script>

<style>
#area {
  position: relative; /* absolute는 부모가 relative일 때 부모를 따라간다. */
  width: 50%;
  padding-bottom: 30%;
}
#vedio {
  position: absolute;
  width: 100%;
  height: 100%;
}
</style>