<template>
  <v-app>
    <v-flex >
      <VueScrollProgress></VueScrollProgress>
    </v-flex>

    <v-toolbar app flat>
      <v-spacer></v-spacer>

<!--      <v-toolbar-title>Title</v-toolbar-title>-->
          <v-menu :nudge-width="100">
            <template v-slot:activator="{ on }">
              <v-toolbar-title v-on="on">
                <span>Books Diary</span>
                <v-icon dark>arrow_drop_down</v-icon>
              </v-toolbar-title>
            </template>
            <v-list>
              <v-list-tile
                      v-for="(item, index) in items"
                      :key="index"
                      @click=""
              >
                <v-list-tile-title>{{ item.title }}</v-list-tile-title>
              </v-list-tile>
            </v-list>
          </v-menu>
      <v-spacer></v-spacer>

    </v-toolbar>



    <v-content>
      <BooksList/>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import BooksList from "./components/BooksList";

export default {
  name: 'App',
  components: {
    BooksList,
    HelloWorld
  },
  data () {
    return {

      items: [
        {
          title: 'Books Diary'
        },
        {
          title: 'Add new book'
        }
      ]
      //
    }
  }
}
</script>
<style>
  #progress-container-el {
    /* background */
    background-color: #f5f5f5 !important;
    top: 0px !important;

  }
  #progress-el {
    /* progress bar */
    background-color: #1867c0 !important;
  }
</style>
