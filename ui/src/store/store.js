import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const store =  new Vuex.Store({
    state: {
      page: 0,
      pageSize: 64,
      items: [],
      volume: localStorage.getItem('volume') ? localStorage.getItem('volume') : 0.5,
      nsfw: true,
    },
    mutations: {
      incrementPage (state) {
        state.page++
      },
      addItems(state, payload)
      {
          payload.items.forEach(i => state.items.push(i))
      },
      changeVolume(state, payload)
      {
          state.volume = payload.value;
          localStorage.setItem('volume', payload.value)
      },
      toggleNSFW(state)
      {
          state.nsfw = !state.nsfw
      }
    },
    actions: {
        loadItems(context) {
            console.log("Loading More | Page: " + store.state.page + " | Size: " + store.state.pageSize)
            context.commit('incrementPage')
            var URL = process.env.VUE_APP_API_URL +'/files?size=';
            fetch(URL + store.state.pageSize  + "&page=" + store.state.page)
                    .then(response => response.json())
                    .then(items => context.commit('addItems', {items : items}));
        },
        changeVolume(context, payload)
        {
            context.commit('changeVolume', payload)
        },
        toggleNSFW(context)
        {
            context.commit('toggleNSFW')
        }
      }
  })
