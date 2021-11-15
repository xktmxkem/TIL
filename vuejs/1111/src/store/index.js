import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const URL = "https://www.googleapis.com/youtube/v3/search"
export default new Vuex.Store({
  state: {
    detailResult : [],
    searchResult : []
  },
  mutations: {
    GETSEARCH: function(state, data){
      for (let info of data){
        state.searchResult.push(info)
      }
    },
    GETDETAIL: function(state, data){
      state.detailResult = data
    }
  },
  actions: {
    getSearch: function(context, data){
      const params = {
        key: API_KEY,
        part: 'snippet',
        q: data,
        type: 'video'
      }

      axios({
        method: 'get',
        url: URL,
        params,
      })
        .then(res => {
          const returnData = res.data.items
          context.commit('GETSEARCH', returnData)
        
        })
        .catch(err => {
          console.log(err)
        })
    },
    getDetail: function(context, data){
      context.commit('GETDETAIL',data)
    }

  },
  getters: {
    searchResult: function(state){
      return state.searchResult
    }
  }

})
