<template>
  <div>
    <TopBlock @click="isOpen = !isOpen"/>
    <BottomBlock />
  </div>
</template>

<script>
import axios from "axios";
import TopBlock from "@/components/Main-Header";
import BottomBlock from "@/components/hot-plates";

export default {
  data: () => ({
    isOpen: true,
  }),
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
</style>

<style scoped>
.text {
  color: #fff;
}
</style>