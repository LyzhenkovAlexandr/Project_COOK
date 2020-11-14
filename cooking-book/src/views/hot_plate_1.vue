<template>
  <div>
    <TopBlock />
    <BottomBlock />
  </div>
</template>

<script>
import axios from "axios";
import TopBlock from "@/components/Main-Header";
import BottomBlock from "@/components/hot_plate1";

export default {
  components: {
    TopBlock,
    BottomBlock
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