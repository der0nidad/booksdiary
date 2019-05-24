<template>
    <v-container>
        <v-container fluid fill-height>
            <v-layout align-center justify-center>
                <v-flex xs12 sm8 md6>
                    <v-card class="elevation-12">
                        <v-toolbar class="elevation-1">
                            <v-toolbar-title
                                    class="text--secondary toolbar_properties"
                            >Edit book {{this.$attrs}}
                            </v-toolbar-title>

                        </v-toolbar>
                        <v-card-text>
                            <v-form
                                    ref="form"
                                    v-model="valid"
                                    lazy-validation>
                                <v-text-field
                                        prepend-icon="title"
                                        name="name"
                                        label="Name"
                                        type="text"
                                        :rules="[v => !!v || 'Name is required']"
                                        v-model="name"
                                >

                                </v-text-field>
                                <v-text-field
                                        prepend-icon="face"
                                        name="author"
                                        label="Author"
                                        type="text"
                                        :rules="[v => !!v || 'Author is required']"
                                        v-model="author"
                                >

                                </v-text-field>
                                <v-text-field
                                        prepend-icon="description"
                                        name="description"
                                        label="Add description"
                                        type="textarea"
                                        v-model="description"
                                >

                                </v-text-field>
                            </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn
                                    color="primary"
                                    @click="onSubmit"
                                    :disabled="!valid"
                            >Edit Book
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </v-container>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "NewBook",
        data() {
            return {
                name: '',
                author: '',
                description: '',
                valid: false,
                endpoint: 'http://127.0.0.1:5000/books',

            }
        },
        props: ['book'],
        methods: {
            onSubmit() {
                if (this.$refs.form.validate()) {
                    const newBook = {
                        name: this.name,
                        author: this.author,
                        description: this.description
                    }
                    console.log(newBook)
                    axios.put(this.endpoint + '/' + this.$attrs.id, newBook)
                        .then(function (response) {
                            console.log(response);
                        })
                        .catch(function (error) {
                            console.log(error);
                        });
                    this.$router.push('/books')

                }
            }
        }
    }
</script>

<style scoped>
    .toolbar_properties {
        color: indigo;
    }
</style>
