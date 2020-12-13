import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const store =  new Vuex.Store({
    state: {
      page: 0,
      pageSize: 64,
      items: [],
      volume: localStorage.getItem('volume') ? localStorage.getItem('volume') : 0.5
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
      }
    },
    actions: {
        loadItems(context) {
            console.log("Loading More | Page: " + store.state.page + " | Size: " + store.state.pageSize)
            context.commit('incrementPage')
            fetch('http://webm.flyb1z0n.com/api/files?size=' + store.state.pageSize  + "&page=" + store.state.page)
                    .then(response => response.json())
                    .then(items => context.commit('addItems', {items : items}));
        },
        changeVolume(context, payload)
        {
            context.commit('changeVolume', payload)
        }
      }
  })