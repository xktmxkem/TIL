<template>
  <div id="lunch">
    <h2>점심메뉴</h2>
    <button @click="recommendLunch" >추천받기</button>
    <p v-if="pickmenu.length">{{pickmenu}}</p>
    <p></p>
    <h3>로또를 뽑아보자</h3>
    <button @click="goLotto">Pick Lotto</button>
  </div>
  
</template>

<script>
import _ from 'lodash'
export default {
  name : "lunch",
  data : function() {
    return {
      lunchmenu : ["국밥", "치킨", "샐러드", "닭가슴살", "카레", "삼겹살"],
      pickmenu : []
    }
  },
  methods : {
    recommendLunch : function(){
      this.pickmenu = _.sample(this.lunchmenu)
    },

    goLotto: function() {
      this.$router.push({name : 'Lotto'})
    }
  }
}
</script>

<style>

</style>