<template>
  <div>
    <TopBlock />
    <BottomBlock />
  </div>
</template>

<script>
import axios from "axios";
import TopBlock from "@/components/Main-Header";
import BottomBlock from "@/components/hot-plates";

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
</style>

<style scoped>
.text {
  color: #fff;
}
</style>