import Vue from 'vue'
import Router from 'vue-router'
import BooksList from '@/components/BooksList'
import NewBook from '@/components/NewBook'

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
        {
            path: '/new',
            name: 'new',
            component: NewBook
        },
        // {
        //     path: '',
        //     name: '',
        //     component: ''
        // },
    ],
    mode: 'history'
})
