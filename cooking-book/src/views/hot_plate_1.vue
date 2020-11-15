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
import BottomBlock from "@/components/hot_plate1";
import Footer from "@/components/Footer";

export default {
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