<template>
  <div>
    <h1>The Lotto</h1>
    <button @click="getNumber">Get Lucky Number</button>
    <ol v-if="luckyNumbers.length">
      <li v-for="(lucky, idx) in luckyNumbers" :key="idx">
        {{ lucky }}
      </li>
    </ol>
    <h2 v-else>버튼을 눌러주세요.</h2>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data: function () {
    return {
      luckyNumbers: [],
    }
  },
  methods: {
    getNumber: function () {
      this.luckyNumbers = []
      const numbers = _.range(1, 46)
      // Variable Routing 으로 전달되는 파라미터 받기
      const num = this.$route.params.num

      for (let i = 0; i < num ; i++) {
        this.luckyNumbers.push(_.sampleSize(numbers, 6))
      }
    }
  }
}
</script>

<style>

</style>