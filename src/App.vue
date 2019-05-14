<template>
  <v-app>


    <NavigationToolbar/>




  </v-app>
</template>

<script>
import BooksList from "@/components/BooksList";
import NavigationToolbar from "@/components/NavigationToolbar";
import NewBook from "@/components/NewBook";

export default {
  name: 'App',
  components: {
    NavigationToolbar,
    BooksList,
    NewBook,
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
