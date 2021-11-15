<template>
  <div>
    
    <input type="text" v-model.trim="searchData" @keyup.enter="getSearch">
    <button @click="getSearch">검색</button>
  </div>
</template>

<script>
export default {
  name: "search",

  data: function() {
    return {
      searchData : ''
    }
  },

  methods: {
    getSearch: function() {
      if(this.searchData.length !==0){
        this.$emit('search-data', this.searchData)
      }
    },


  }

}
</script>

<style>

</style>