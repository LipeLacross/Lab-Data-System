import { createRouter, createWebHistory } from 'vue-router';
import Login from './components/Login.vue';
import AdminView from './views/AdminView.vue';
import OperatorView from './views/OperatorView.vue';

const routes = [
    { path: '/', component: Login },
    { path: '/admin', component: AdminView },
    { path: '/operator', component: OperatorView },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
