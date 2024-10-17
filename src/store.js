import { createStore } from 'vuex';

export default createStore({
    state: {
        user: null,
    },
    mutations: {
        setUser(state, user) {
            state.user = user;
        },
    },
    actions: {
        login({ commit }, user) {
            commit('setUser', user);
        },
    },
    getters: {
        isLoggedIn: (state) => !!state.user,
        userRole: (state) => state.user?.role,
    },
});
