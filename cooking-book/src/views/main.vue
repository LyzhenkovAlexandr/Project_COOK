<template>
  <div>
    <TopBlock />
    <BottomBlock />
    <!-- <div v-for="i in dish" v-bind:key="i.img">
      <img :src="itemImage(categories1.jpg)" />
      <span class="text">{{ i.title }}</span>
    </div> -->
  </div>
</template>

<script>
import axios from "axios";
import TopBlock from "@/components/Main-Header";
import BottomBlock from "@/components/Main-Content";

export default {
  data() {
    return {
      dish: [],
    };
  },
  components: {
    TopBlock,
    BottomBlock
  },
  methods: {
    // getMessage() {
    //   const path = "http://127.0.0.1:5000/";
    //   axios
    //     .get(path)
    //     .then((res) => {
    //       this.dish = res.data.dishes;
    //       console.log(this.dish);
    //     })
    //     .catch((error) => {
    //       // eslint-выключение следующей строки
    //       console.error(error);
    //     });
    // },
    // itemImage(img) {
    //   return require("@/assets/" + img);
    // },
  },
  
  // created() {
  //   this.getMessage();
  // },
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