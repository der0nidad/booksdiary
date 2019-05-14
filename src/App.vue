<template>
  <v-app>
    <v-flex >
      <VueScrollProgress></VueScrollProgress>
    </v-flex>

    <NavigationToolbar/>



    <v-content>
      <BooksList/>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import BooksList from "./components/BooksList";
import NavigationToolbar from "./components/NavigationToolbar";

export default {
  name: 'App',
  components: {
    NavigationToolbar,
    BooksList,
    HelloWorld
  },
  data () {
    return {


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
