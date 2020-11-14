import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'Main',
    component: () =>
        import ( /* webpackChunkName: "about" */ '../views/main.vue')
}, {
    path: '/hot_list',
    name: 'hot_plates',
    component: () =>
        import ( /* webpackChunkName: "about" */ '../views/hot_list.vue')
}, {
    path: '/hot_list/hot_1',
    name: 'hot_1',
    component: () =>
        import ( /* webpackChunkName: "about" */ '../views/hot_plate_1.vue')
}, {
    path: '/test',
    name: 'test',
    component: () =>
        import ( /* webpackChunkName: "about" */ '../views/product.vue')
}]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router