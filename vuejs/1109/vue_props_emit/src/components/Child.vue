<template>
  <div id="child">
    <h1 id="header">AppChild</h1>
    <input type="text" @keyup.enter="saveData">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ inputData }}</p>
  </div>
</template>

<script>
export default {
  name: 'Child',
  data: function () {
    return {
      inputData: '',
    }
  },
  props: {
    appData: String,
    parentData: String,
  },
  methods: {
    saveData: function (event) {
      this.inputData = event.target.value
      // parent 로 데이터 전달
      this.$emit('child-data', this.inputData)
    }
  }
}
</script>

<style>
#child {
  border: 1px solid blue;
}
</style>