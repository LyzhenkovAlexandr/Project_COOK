<template>
  <div>
    <TopBlock />
    <SnackPlate1 />
    <Footer />
  </div>
</template>

<script>
import axios from "axios";
import TopBlock from "@/components/Main-Header";
import SnackPlate1 from "@/components/snack_plate1";
import Footer from "@/components/Footer";

export default {
  components: {
    TopBlock,
    SnackPlate1,
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