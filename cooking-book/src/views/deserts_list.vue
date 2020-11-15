<template>
  <div>
    <TopBlock @click="isOpen = !isOpen"/>
    <Deserts />
    <Footer />
  </div>
</template>

<script>
import axios from "axios";
import TopBlock from "@/components/Main-Header";
import Deserts from "@/components/deserts";
import Footer from "@/components/Footer";

export default {
  data: () => ({
    isOpen: true,
  }),
  components: {
    TopBlock,
    Deserts,
    Footer
  },
};
</script>

<style>
body {
  background: #009DC1!important;
}
html {
  overflow-x:hidden!important;
}
.text {
  color: #fff;
}
</style>