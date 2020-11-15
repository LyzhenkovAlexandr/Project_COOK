<template>
  <div>
    <TopBlock @click="isOpen = !isOpen"/>
    <ColdPlates />
    <Footer />
  </div>
</template>

<script>
import axios from "axios";
import TopBlock from "@/components/Main-Header";
import ColdPlates from "@/components/cold_plates";
import Footer from "@/components/Footer";

export default {
  data: () => ({
    isOpen: true,
  }),
  components: {
    TopBlock,
    ColdPlates,
    Footer
  },
};
</script>

<style>
body {
  background: #009DC1!important;
}
html, body {
  overflow-x:hidden!important;
}
.text {
  color: #fff;
}
</style>