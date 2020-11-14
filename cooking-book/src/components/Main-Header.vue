<template>
  <div class="header">
    <span>Максимастер</span>
    <button><img src="@/assets/menu_btn.png" /></button>
  </div>
</template>

<script>
import axios from "axios";

export default {};
</script>

<style scoped>
.header {
  background: #343434;
  width: 100%;
  height: 40px;
  border-bottom: 1px solid #fff;
}

.header > span {
  font-family: SF UI Text;
  font-size: 20px;
  font-style: normal;
  font-weight: 400;
  line-height: 40px;
  letter-spacing: 0em;
  text-align: left;
  color:#fff;
  margin-left: 26px;
}

.header>button{
    background: none;
    border: none;
    width: initial;
    outline: none;
    line-height: 40px;
    float: right;
    padding-right: 26px;
}
</style>