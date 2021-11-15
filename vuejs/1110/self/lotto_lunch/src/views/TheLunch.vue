<template>
  <div>
    <h1>점심 메뉴</h1>
    <button @click="getOne">Pick One</button>
    <p>{{ lunch }}</p>
    <button>Emit 이벤트 발생</button>

    <hr>

    <h2>로또 뽑으러 가기</h2>
    <button @click="goLotto">Go Lotto!!</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data: function () {
    return {
      menus: ['국밥', '치킨', '피자', '삼겹살', '떡볶이', '라면'],
      lunch: ''
    }
  },
  methods: {
    getOne: function () {
      this.lunch = _.sample(this.menus)
    },

    goLotto: function () {
      // 다른 컴포넌트 페이지로 이동 시키는 부분
      this.$router.push({ name: 'Lotto', params: { num: 3 }})
    }
  }
}
</script>

<style>

</style>