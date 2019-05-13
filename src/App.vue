<template>
  <v-app>
    <v-flex >
      <VueScrollProgress></VueScrollProgress>
    </v-flex>
    <v-toolbar app>

      <v-toolbar-title class="headline text-uppercase">
        <span>Vuetify</span>
        <span class="font-weight-light">MATERIAL DESIGN</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        flat
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
        <span class="mr-2">Latest Release</span>
      </v-btn>

    </v-toolbar>



    <v-content>
      <HelloWorld/>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld'

export default {
  name: 'App',
  components: {
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
