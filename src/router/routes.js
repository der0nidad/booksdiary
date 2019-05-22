import Vue from 'vue'
import Router from 'vue-router'
import BooksList from '@/components/BooksList'
import NewBook from '@/components/NewBook'
import EditBook from '@/components/EditBook'

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
        {
            path: '/edit/:id',
            props: true,
            name: 'edit',
            component: EditBook
        },
        // {
        //     path: '',
        //     name: '',
        //     component: ''
        // },
    ],
    mode: 'history'
})
