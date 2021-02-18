<template>
  <div>
    <TopBlock />
    <BottomBlock />
    <Footer />
  </div>
</template>

<script>
import axios from "axios";
import TopBlock from "@/components/Main-Header";
import BottomBlock from "@/components/Main-Content";
import Footer from "@/components/Footer";

export default {
  data() {
    return {
      dish: [],
    };
  },
  components: {
    TopBlock,
    BottomBlock,
    Footer
  }
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
    color:#fff;
  }
</style>