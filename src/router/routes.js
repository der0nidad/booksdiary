import Vue from 'vue'
import Router from 'vue-router'
import BooksList from '@/components/BooksList'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '',
            name: 'home',
            component: BooksList
        },
        {
            path: '/books',
            name: 'books',
            component: BooksList
        },
        // {
        //     path: '/new',
        //     name: 'new',
        //     component: 'NewBook'
        // },
        // {
        //     path: '',
        //     name: '',
        //     component: ''
        // },
    ],
    mode: 'history'
})
