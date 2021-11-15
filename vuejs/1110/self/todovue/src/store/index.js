import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    todoList: [
      // Todo dummy Data
      // 완료 유무와 내용이 들어가야해서 object형태로
      // {
      //   content: '할 일 1',
      //   isCompleted: false,
      // },
      // {
      //   content: '할 일 2',
      //   isCompleted: true,
      // },

    ],
  },
  mutations: {
    ADD_TODO: function (state, data) {
      const todo = {
        content: data,
        isCompleted: false
      }
      state.todoList.push(todo)
    },

    UPDATE_TODO: function(state, data){
      // isCompleted를 토글
      // 고민: data가 stae.todoList 어디에 있는지 모름.
      // 해결 : 하나씩 뒤져서 같은걸 찾는다!! => 수정하고 저장한다.
      state.todoList = state.todoList.map(todo => {
        if (todo === data) {
          const temp = {
            ...todo, // Spread Syntax
            isCompleted: !todo.isCompleted
          }
          return temp
        } else {
          return todo
        }
      })
    },

    DELETE_TODO: function(state, data) {
      // state.todoList = state.todoList.map(todo => {
      //   if (todo != data){
      //     return data
      //   } else {
      //     continue
      //   }
      // })
      //filter로 해도되지만 splice로 연습
      // 인덱스 받아옴
      const idx = state.todoList.indexOf(data)
      // splice로 삭제
      state.todoList.splice(idx, 1)

    }


  },
  actions: {
    addTodo ({commit}, data) {
      // mutation을 호출하여 state에 data를 바녕ㅇ
      commit('ADD_TODO', data)
    },
    updateTodo({commit}, data){
      commit('UPDATE_TODO', data)
    },
    deleteTodo({commit}, data){
      commit('DELETE_TODO', data)
    },
  },

  // Vuex의 computed의 역할
  getters: {
    allTodos: function(state) {
      return state.todoList.length
    },
    completedTodo: state => {
      return state.todoList.filter(todo => {
        return todo.isCompleted
      }).length
    },
    uncompletedTodo: state => {
      return state.todoList.filter(todo => {
        return !todo.isCompleted
      }).length
    }


  }

})
