import { createStore } from 'vuex'

export default createStore({
  state: {
    isLoggedIn: !!localStorage.getItem('token'),
    sortOrder: localStorage.getItem('sortOrder') || 'createdAt',
    profileUpdated: false,
    },
  mutations: {
    setProfileUpdated(state, value) {
      state.profileUpdated = value;
    },
    login(state) {
      state.isLoggedIn = true;
    },
    logout(state) {
      state.isLoggedIn = false;
    },
    setSortOrder(state, sortOrder) {
      state.sortOrder = sortOrder;
      localStorage.setItem('sortOrder', sortOrder);
    },
  },
  actions: {
    setProfileUpdated(context, value) {
      context.commit('setProfileUpdated', value);
    },
    login(context) {
      context.commit('login');
    },
    logout(context) {
      context.commit('logout');
    }
  }
});
