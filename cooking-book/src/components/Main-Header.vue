<template>
  <div class="header">
    <span>Максимастер</span>
    <img src="@/assets/logo.png"/>
    <button><img src="@/assets/menu_btn.png" /></button>
  </div>
</template>

<script>
import axios from "axios";

export default {};
</script>

<style scoped>
.header {
  background: #001C23;
  width: 100%;
  height: 55px;
  border-bottom: 2px solid #fff;
      text-align: center;
}

.header > span {
  font-family: SF UI Text;
  font-size: 20px;
  font-style: normal;
  font-weight: 400;
  line-height: 55px;
  letter-spacing: 0em;
  text-align: left;
  color:#fff;
  margin-left: 26px;
  float: left;
}

.header>button{
    background: none;
    border: none;
    width: initial;
    outline: none;
    line-height: 50px;
    float: right;
    padding-right: 26px;
}

.header>button img{
    width: 26px;
    height: 18px;
    margin-left: 26px;
}

.header>img {
    height: 40px;
    margin-left: -56px;
    margin-top: 6.5px;
}
</style>