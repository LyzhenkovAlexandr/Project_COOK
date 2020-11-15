<template>
  <div>
    <TopBlock @click="isOpen = !isOpen"/>
    <Snack />
    <Footer />
  </div>
</template>

<script>
import axios from "axios";
import TopBlock from "@/components/Main-Header";
import Snack from "@/components/snack";
import Footer from "@/components/Footer";

export default {
  data: () => ({
    isOpen: true,
  }),
  components: {
    TopBlock,
    Snack,
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