<template>
  <div id="parent">
    <h1 id="header">AppParent</h1>
    <input type="text" @keyup.enter="saveData">
    <p>appData: {{appData}}</p>
    <p>parentData: {{inputData}}</p>
    <p>childData: {{childData}}</p>

    <!-- 다시 받은 데이터를 자식한테 보내면됨 -->
    <!-- app에서 child에게 보내는 데이터 -->
    <!-- 내가 child에게 보내는 데이터 -->
    <Child :app-data="appData" 
    :parent-data="inputData"
    @child-data="getChildData"
    />

  </div>
</template>

<script>
import Child from '@/components/Child.vue'


export default {
  name: 'Parent',
  data: function (){
    return{
      // 영역이 서로 달라서 다르게 작동한다.
      inputData: '',
      childData: '',
    }
  },
  components: {
    Child,
  },
  // 부모가 보낸 데이터를 받는 부분
  props: {
    // 이때 DOM의 kebabcase는 자동으로 JS에서 Camel case로 변환된다.
    // DOM에서 app-data 전달 했더라도 JS 에서는 appData 로 수신
    appData: String,
  },

  methods: {
    saveData: function (event){
      this.inputData = event.target.value
      // 데이터가 저장되는 시점에 부모로 데이터를 전달 emit
      // 템플릿에서 들을 수 있도록 케밥 케이스로 전달
      // parent component가 발생시키는 이벤트 
      this.$emit('parent-data', this.inputData)
    },
    getChildData: function(data){
      this.childData = data
      // 할당과 동시에 다시 부모인 App으로 emit
      this.$emit('child-data', this.childData)
    }
  },


}
</script>
// scoped 속성을 주게 되면 지역변수로서 활용하게 된다.
<style scoped>
#parent {
  border: 1px solid red
}

#header {
  color: green;
}
</style>