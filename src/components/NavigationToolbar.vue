<template>
    <div>
        <v-toolbar app flat color="indigo">
            <v-spacer></v-spacer>

            <!--      <v-toolbar-title>Title</v-toolbar-title>-->
            <v-menu :nudge-width="100">
                <template v-slot:activator="{ on }">
                    <v-toolbar-title v-on="on">
                        <span class="bd_title pointer"> Books Diary</span>
                        <v-icon dark>arrow_drop_down</v-icon>
                    </v-toolbar-title>
                </template>
                <v-list>
                    <v-list-tile
                            v-for="(item, index) in items"
                            :key="index"
                            :to="item.url"
                    >
                        <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                    </v-list-tile>
                </v-list>
            </v-menu>
            <v-spacer></v-spacer>

        </v-toolbar>
        <v-content>
            <router-view></router-view>
        </v-content>
    </div>
</template>

<script>
    export default {
        name: "NavigationToolbar",
        data() {
            return {
                items: [
                    {
                        title: 'Books Diary',
                        url: 'books'
                    },
                    {
                        title: 'Add new book',
                        url: 'new'

                    }
                ]
            }
        }
    }
</script>

<style scoped>


    .bd_title {
        text-decoration: none;
        color: #FFFFFF;
    }

    .pointer {
        cursor: pointer;
    }

</style>
