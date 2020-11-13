<template>
  <div>
    <h1 v-for="t in dish" v-bind:key="t.title">{{ t.title }}</h1>
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
        })
        .catch((error) => {
          // eslint-выключение следующей строки
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

<style scoped>
</style>