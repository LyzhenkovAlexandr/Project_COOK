<template>
  <div>
    <div v-for="i in dish" v-bind:key="i.img">
     <img :src="`../assets/${i.img}`"/>
      <p>{{ i.title }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      dish: [],
    };
  },
  methods: {
    getMessage() {
      const path = "http://127.0.0.1:5000/Main";
      axios
        .get(path)
        .then((res) => {
          this.dish = res.data.dishes;
          console.log(this.dish);
        })
        .catch((error) => {
          // eslint-выключение следующей строки
          console.error(error);
        });
    },
    itemImage(img) {
      return require("../assets/" + img);
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

<style scoped>
</style>