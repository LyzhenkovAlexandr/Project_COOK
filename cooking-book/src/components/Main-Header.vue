<template>
  <div class="t-header">
      <div class="logo"><router-link to="/"> <img src="@/assets/logo.png" /></router-link></div>
    <div class="header">
    <span>Максимастер</span>
    



    <nav class="menu" id="main-menu" :class="{openMenu: !isClose}">
      <section class="menu-flex-1">
        <section class="menu-dropdown">
          <router-link to="/" tag="button" class="button">На главную</router-link>
          <router-link to="#" tag="button" class="button">Закуски</router-link>
          <router-link to="#" tag="button" class="button">Холодные блюда</router-link>
          <router-link to="/hot_list" tag="button" class="button">Горячие блюда</router-link>
          <router-link to="#" tag="button" class="button">Десерты</router-link>
        </section>
      </section>
    </nav>


    <button class="box-2" id="toggle-menu" @click="isClose = !isClose"><img src="@/assets/menu_btn.png" /></button>
  </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: () => {
    return {
      isClose: true,
    };
  },
};
</script>

<style>
.t-header .header {
  background: #001C23;
  width: 100%;
  height: 55px;
  border-bottom: 2px solid #fff;
  text-align: center;
}

.t-header .header > span {
  font-family: SF UI Text;
  font-size: 20px;
  font-style: normal;
  font-weight: 400;
  line-height: 55px;
  letter-spacing: 0em;
  text-align: left;
  color: #fff;
  margin-left: 26px;
  float: left;
}

.t-header .header > button {
  background: none;
  border: none;
  width: initial;
  outline: none;
  line-height: 18px;
  float: right;
  padding-right: 26px;
  padding-left: 0;
}

.t-header .header > button img {
  width: 26px;
  height: 18px;
  margin-left: 26px;
}
.t-header .logo {
  position: absolute;
  top: 6.5px;
  width: 90%;
  margin: 0 5%;
  height: 40px;
  text-align: center;
}

.t-header .logo img {
  margin: 0 auto;
  height: 40px;
}

@media only screen and (max-width: 500px) {
  .t-header .logo > img {
    margin: 0 auto;
    height: 40px;
    padding-left: 100px;
  }
}
.t-header .box-1 {
  padding-left: 20px;
  padding-top: 7px;
}
.t-header .box-1,
.t-header .box-2 {
  height: inherit;
}
.t-header .box-2 {
  padding-right: 15px;
  padding-top: 7px;
}
.t-header .box-2 {
  background: transparent;
  font-size: 3.1em;
  width: 1em;
  height: 1em;
  line-height: 0.3em;
  overflow: hidden;
  white-space: nowrap;
  text-indent: 2em;
}
.t-header .box-2::after {
  position: absolute;
  top: 0.4em;
  right: 0.3em;
  display: block;
  background: url("");
  text-indent: 0;
  cursor: pointer;
}
.t-header .menu {
  display: block;
  position: absolute;
  right: -500px;
  top: 55px;
  width: 275px;
  height: 300px;
  padding-bottom: 10px;
  background: #001C23;
  transition-duration: 0.9s;
  -moz-border-radius-bottomleft: 29px;
  -webkit-border-bottom-left-radius: 29px;
  border-bottom-left-radius: 29px;
  border: 2px solid #fff;
  z-index: 9999;
}

.menu.openMenu {
  /* display: block; */
  transform: translateX(-500px);
  transition-duration: 0.9s;
}
.t-header .menu-flex-1 {
  display: flex;
  justify-content: center;
  width: 100%;
  height: 100%;
  align-items: center;
}
.t-header .menu-dropdown {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  width: 175px;
}
.t-header .menu-dropdown .button {
  height: 40px;
  margin-top: 10px;
  width: 160px;
  border: 1px solid #fff;
  box-sizing: border-box;
  border-radius: 8px;
  outline-width: 0;
  background: #002630;
  color: #fff;
}
.t-header .button:hover {
  cursor: pointer;
}
</style>