<template>
  <div id="Lotto">
    <h2>로또</h2>
    <button @click="getLottoNum">Pick Lotto</button>
    <div v-if="lottoNum.length">
      {{lottoNum}}
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  data : function(){
    return{
      lottoNum : [],
      
    }
  },
  methods : {
    getLottoNum : function() {
      this.lottoNum = []
      for (let i = 0; i < 6; i ++ ){
        const randomNum = _.random(1,46)
        this.lottoNum.push(randomNum)
      }
      
    }

  }

}
</script>

<style>

</style>