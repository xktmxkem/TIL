<template>
  <div id="app">
    <div id="nav">
      <span v-if="isLogin">
        <router-link :to="{ name: 'TodoList' }">Todo List</router-link> | 
        <router-link :to="{ name: 'CreateTodo' }">Create Todo</router-link> |
        <!-- 고유 이벤트가 없어서 .native로 발생시켜줘야한다. -->
        <!-- 라우터 링크의 경우 그렇다. -->
        <router-link to="#" @click.native="logout">로그아웃</router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> 
      </span>
    </div>
    <!-- 아래에서 로그인되어서 변경되었을 때 그 값을ㅇ 윗 돔에게 전달을 해야지 화면이 바뀜 -->
    <router-view @login="isLogin=true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      // 로그인이 되었는가
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      // 로그인 상태 해제
      this.isLogin = false,
      // 토큰삭제
      localStorage.removeItem('jwt'),
      this.$router.push({ name: 'Login' })
    }
  },
  created: function () {
    // 로그인 되었는지 토큰값 확인하기 
    const token = localStorage.getItem('jwt')

    if (token) {
      this.isLogin = true
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
