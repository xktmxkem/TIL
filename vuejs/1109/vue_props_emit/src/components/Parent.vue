<template>
  <div id="parent">
    <h1 id="header">AppParent</h1>
    <input type="text" @keyup.enter="saveData">
    <p>appData: {{ appData }} </p>
    <p>parentData: {{ inputData }}</p>
    <p>childData: {{ childData }}</p>

    <!-- 부모로 부터 받은 데이터를 나의 자식에게 다시 전달!! -->
    <child 
      :app-data="appData" 
      :parent-data="inputData"
      @child-data="getChildData"
      >
    </child>
  </div>
</template>

<script>
import Child from '@/components/Child'

export default {
  name: 'Parent',
  data: function () {
    return {
      inputData: '',
      childData: '',
    }
  },
  components: {
    Child,
  },
  // 부모가 보낸 데이터를 받는 부분 (전화 수신)
  props: {
    // DOM 의 kebab case 는 자동으로 JS에서 Camel case로 변환
    // DOM에서 app-data 전달, JS에서는 appData 로 받으면됨
    appData: String,
  },
  methods: {
    saveData: function (event) {
      this.inputData = event.target.value
      // 부모로 데이터를 전달 emit (이벤트 발생시키기)
      this.$emit('parent-data', this.inputData)
    },

    getChildData: function (data) {
      this.childData = data
      // 할당과 동시에 다시 부모인 App으로 emit
      this.$emit('child-data', this.childData)
    },
  },
}
</script>

<style scoped>
#parent {
  border: 1px solid red;
}

#header {
  color: green;
}
</style>