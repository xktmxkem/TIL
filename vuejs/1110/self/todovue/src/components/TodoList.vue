<template>
  <div id="Todoist">
    <h1>Todo List</h1>
    <h2>All Todos: {{allTodos}}</h2>
    <h2>Completed Todo: {{completedTodo}}</h2>
    <h2>Uncompleted Todo: {{uncompletedTodo}}</h2>
    <todo-list-item
      v-for="(todo, idx) in todoList" :key="idx"
      :todo="todo"
     
    >
    </todo-list-item>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem.vue'
//import { mapGetters } from 'vuex'
import { mapState } from 'vuex'

export default {
  name: "Todoist",
  components : {
    TodoListItem
  },

  computed: {
    // todos: function() {
    //   return this.$store.state.todoList
    // },
    // 같은 역할하는 mapState 사용해보기
    ...mapState([
      'todoList',
    ]),

    // getter 역시 위와 같은 역할을 하지만 연습을 위해 하나하나
    // 따로 작성을 해주었다. 
    // ...mapGetters([
    //   'allTodos',
    //   'completedTodo',
    //   'uncompletedTodo',
    // ])
    allTodos: function() {
      return this.$store.getters.allTodos
    },
    completedTodo: function(){
      return this.$store.getters.completedTodo
    },
    uncompletedTodo: function(){
      return this.$store.getters.uncompletedTodo
    }
  },

}
</script>

<style>

</style>