<template>
  <div id="TodoListItem">
    <span @click="updateTodo(todo)" class='mx-3' :class="{completed : todo.isCompleted}">{{todo.content}}</span>
    <button @click="deleteTodo(todo)">Delete</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  
  name : "TodoListItem",
  data: function() {
    return{

    } 
  },
  props: {
    todo: Object,
  },
  methods: {
    ...mapActions([
      'deleteTodo',
      'updateTodo'
    ]),
    
    // updateTodo: function(){
    //   // 해당 item의 isCompleted를 토글해주세요! 라는 요청을 보낸다. 
    //   this.$store.dispatch('updateTodo', this.todo)
    // },
    // deleteTodo: function(){
    //   this.$store.dispatch('deleteTodo', this.todo)
    // }
  }

}
</script>

<style scoped>
  .mx-3{
    margin: 1rem;
  }
  .completed{
    text-decoration: line-through;
  }
</style>