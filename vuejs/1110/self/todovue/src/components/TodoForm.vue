<template>
  <div id="TodoForm">
    <h2>TodoForm.vue</h2>
    <input v-model.trim="inputData" @keyup.enter="addTodo" class="my-3" type="text" >
    <button @click="addTodo">Add</button>
  </div>
</template>

<script>
export default {
  name : "TodoForm",
  data : function() {
    return{
      inputData : '',
    }
  },
  methods:{
    addTodo: function(){
      // vuex에 저장하도록 한다.
      if (this.inputData.length){
        this.$store.dispatch('addTodo', this.inputData)
        this.inputData = ''
      } else {
        alert('할 일을 입력해주세요.')
      }
      
    },
  }
}
</script>

<style scoped>
  .my-3{
    margin:1rem, 0;
  }
</style>