<template>
  <div>
    <TopBlock @click="isOpen = !isOpen"/>
    <BottomBlock />
    <Footer />
  </div>
</template>

<script>
import axios from "axios";
import TopBlock from "@/components/Main-Header";
import BottomBlock from "@/components/hot-plates";
import Footer from "@/components/Footer";

export default {
  data: () => ({
    isOpen: true,
  }),
  components: {
    TopBlock,
    BottomBlock,
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