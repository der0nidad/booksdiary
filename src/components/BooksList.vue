<template>
    <div>
        <v-container>
            <v-layout justify-center mb-4>
                <v-flex xs6 lg2 md4 sm3 mr-8>
                    <v-text-field
                            label="Search name"
                    ></v-text-field>

                </v-flex>
                <!--                <v-spacer></v-spacer>-->
                <v-flex xs3 lg1 ml-5>
                    <v-btn fab
                           class="elevation-1"
                           @click="table_view = true"
                    >
                        <v-icon x-large>view_list</v-icon>
                    </v-btn>
                </v-flex>
                <v-flex xs3 lg1>
                    <v-btn fab
                           class="elevation-1"
                           @click="table_view = false"
                    >
                        <v-icon x-large>view_module</v-icon>
                    </v-btn>
                </v-flex>
            </v-layout>
        </v-container>
        <v-container grid-list-lg>
            <v-layout row wrap>
                <v-flex xs12
                        v-if="table_view"
                >
                    <v-data-table
                            :headers="headers"
                            :items="books"
                            class="elevation-1"
                    >
                        <template v-slot:items="props">
                            <td>{{ props.item.id }}</td>
                            <td>{{ props.item.name }}</td>
                            <td>{{ props.item.author }}</td>
                            <td>{{ props.item.description }}</td>
                        </template>
                    </v-data-table>
                </v-flex>
                <v-flex v-else>
                    <v-card
                            v-for="(item, i) in books"
                            :key="i"
                            xs12 sm6 md4
                    >


                        <v-card-title primary-title>
                            <div>
                                <h3 class="headline mb-0"></h3>
                                <p> {{ item.name }} </p>
                                <p> {{ item.author }}</p>
                                <p> {{ item.description }}</p>
                            </div>
                        </v-card-title>
                        <v-card-actions>
                            <v-btn
                                    flat
                                    color="primary"
                                    :to="'/edit/'+item.id"
                                    :book="item"
                            >Edit
                            </v-btn>
                            <v-btn
                                    flat
                                    color="primary"
                                    @click="deleteBook(item, $event)"
                            >Delete
                            </v-btn>
                        </v-card-actions>

                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "BooksList",
        data() {
            return {
                table_view: false,
                loading: false,
                endpoint: 'http://127.0.0.1:5000/books',
                headers: [
                    {
                        test: 'id',
                        value: 'id'
                    },
                    {
                        text: 'Name',
                        align: 'left',
                        sortable: false,
                        value: 'name'
                    },
                    {
                        text: 'Author',
                        value: 'author'
                    },
                    {
                        text: 'Description',
                        value: 'description'
                    }
                ],
                books: [
                    {
                        id: 1,
                        name: 'Приключения капитана Блада',
                        author: 'Рафаэль Сабатини',
                        description: 'Книга про пиратов'

                    },
                    {
                        id: 2,
                        name: 'Приключения Тома Сойера',
                        author: 'Марк Твен',
                        description: 'Интересные приключения'

                    }]
            }
        },
        created() {
            axios.get(this.endpoint)
                .then(response => {
                    this.books = response.data
                    console.log(this.books)
                })
                .catch(error => console.log(error))
        },
        methods: {
            deleteBook(item, event) {
                console.log(this.endpoint + '/' + item.id)
                axios.delete(this.endpoint + '/' + item.id)
                    .then(response => {
                        console.log('success')
                    })
                    .catch(error => console.log(error))
            },
            editBook(item, event) {
                console.log(item)
                item.name = 'Updated Name'
                axios.put(this.endpoint + '/' + item.id, item)
                    .then(response => {
                        console.log('success')
                    })
                    .catch(error => console.log(error))
            }
        }


    }
</script>

<style scoped>

</style>
