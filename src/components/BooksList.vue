<template>
    <div>
        <v-container >
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
                       @click="table_view = !table_view"
                    >
                    <v-icon x-large>view_list</v-icon>
                    </v-btn>
                </v-flex>
                <v-flex xs3 lg1>
                    <v-btn fab
                        class="elevation-1"
                       @click="table_view = !table_view"
                    >
                    <v-icon x-large>view_module</v-icon>
                    </v-btn>
                </v-flex>
            </v-layout>
        </v-container>
        <v-container grid-list-lg>
            <v-layout row wrap>
                <v-flex xs12 sm6 md4
                    v-if="table_view"
                >
                    <v-data-table
                            :headers="headers"
                            :items="books"
                            class="elevation-1"
                    >
                        <template v-slot:items="props">
                            <td>{{ props.item.id }}</td>
                            <td class="text-xs-right">{{ props.item.name }}</td>
                            <td class="text-xs-right">{{ props.item.author }}</td>
                            <td class="text-xs-right">{{ props.item.description }}</td>
                        </template>
                    </v-data-table>
                </v-flex>
                <v-flex v-else>
                    <v-card
                        v-for="(item, i) in books"
                        :key="i"
                    >


                        <v-card-title primary-title>
                            <div>
                                <h3 class="headline mb-0"></h3>
                                <p> {{ item.name }} </p>
                                <p> {{ item.author }}</p>
                                <p> {{ item.description }}</p>
                            </div>
                        </v-card-title>


                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
    export default {
        name: "BooksList",
        data () {
            return {
                table_view: false,
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
        }


    }
</script>

<style scoped>

</style>
