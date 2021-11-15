<template>
  <div id="app">
    <h1 id="header">App</h1>
    <!-- DOM EVENT는 콜백함수 첫번째 인자로 event 정보를 넘겨줌  -->
    <input type="text" @keyup.enter="saveData">
    <p>appData: {{ inputData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData}}</p>

    <!-- 자식 컴포넌트에 데이터 형태로 보내주면 props가 된다 -->
    <!-- 자식 컴포넌트(사용된 형태) -->
    <!-- parent에게 데이터 받는 부분 -->
    <Parent 
    v-bind:appData="inputData" 
    @parent-data="getParentData"
    @child-data="getChildData"/>
  </div>
</template>

<script>
// 자식 컴포넌트 불러오기
import Parent from '@/components/Parent.vue'

export default {
  name: 'App',
  // 데이터를 저장할 필요가 있다
  data: function () {
    return {
      inputData: '',
      parentData: '',
      childData: '',
      
    }
  },
  components: {
    //key, value 같으면 생략 가능
    //Parent : Parent,
    Parent,
  },
  methods: {
    saveData: function (event) {
      this.inputData = event.target.value
    },

    getParentData: function (data){
      this.parentData = data
    },

    getChildData: function(data){
      this.childData = data
    },
  },
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
  /* 테두리 설정 */
  border: 1px solid black;
}
</style>
