<template>
  <div id="app">
    <h1 id="header">App</h1>
    <input type="text" @keyup.enter="saveData">
    <p>appData: {{ inputData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>

    <!-- 데이터를 자식에게 보내는 부분 "속성=전달값" 형식으로 전달 (전화 송신) -->
    <parent 
      :app-data="inputData" 
      @parent-data="getParentData"
      @child-data="getChildData"
      >
    </parent>
  </div>
</template>

<script>
import Parent from '@/components/Parent'

export default {
  name: 'App',
  data: function () {
    return {
      inputData: '',
      parentData: '',
      childData: '',
    }
  },
  components: {
    Parent,
  },
  methods: {
    saveData: function (event) {
      this.inputData = event.target.value
    },

    getParentData: function (data) {
      // console.log(data)
      this.parentData = data
    },

    getChildData: function (data) {
      this.childData = data
    }
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
