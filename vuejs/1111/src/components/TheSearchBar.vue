<template>
  <div id="TheSearchBar">
    <input id="searchBar" v-model.trim="searchKeyword"  @keyup.enter="getSearch" type="text">
    <button  @click="getSearch">검색</button>
  </div>
</template>

<script>
export default {
  name : "TheSearchBar",
  data : function() {
    return {
      searchKeyword : ''
    }
  },
  methods: {
    getSearch: function() {
      if (this.searchKeyword.length){
        this.$store.dispatch('getSearch', this.searchKeyword)
        this.searchKeyword = ''
      } else {
      alert("검색어를 입력해주세요")
      }
    }
  },
}
</script>

<style scoped>
#searchBar {
  margin: 3px;
  margin: 3px;
  margin: 3px;
  margin: 0px;

}
</style>