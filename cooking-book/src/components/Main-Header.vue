<template>
  <div class="header Flex">
    <span>Максимастер</span>
    <img src="@/assets/logo.png" />


    <nav class="menu" id="main-menu">
      <section class="menu-flex-1">
        <section class="menu-dropdown">
          <button class="button">На главную</button>
          <button class="button">Закуски</button>
          <button class="button">Холодные блюда</button>
          <button class="button">Горячие блюда</button>
          <button class="button">Десерты</button>
        </section>
      </section>
    </nav>

    <button class="box-2" id="toggle-menu" @click.prevent="$emit('click')"><img src="@/assets/menu_btn.png" /></button>
  </div>
</template>

<script>
import axios from "axios";

// (function () {
//   let button = document.getElementById("toggle-menu");
//   button.addEventListener("click", function (event) {
//     event.preventDefault();
//     let menu = document.getElementById("main-menu");
//     menu.classList.toggle("is-open");
//   });
// })();

export default {
  
};
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
  color: #fff;
  margin-left: 26px;
  float: left;
}

.header > button {
  background: none;
  border: none;
  width: initial;
  outline: none;
  line-height: 50px;
  float: right;
  padding-right: 26px;
}

.header > button img {
  width: 26px;
  height: 18px;
  margin-left: 26px;
}

.header > img {
  height: 40px;
  margin-left: -56px;
  margin-top: 6.5px;
}

.Flex {
  display: flex;
  width: 100%;
  justify-content: space-between;
}
.box-1 {
  padding-left: 20px;
  padding-top: 7px;
}
.box-1,
.box-2 {
  height: inherit;
}
.box-2 {
  padding-right: 15px;
  padding-top: 7px;
}
.box-2 {
  background: transparent;
  font-size: 3.1em;
  width: 1em;
  height: 1em;
  line-height: 0.3em;
  overflow: hidden;
  white-space: nowrap;
  text-indent: 2em;
}
.box-2::after {
  position: absolute;
  top: 0.4em;
  right: 0.3em;
  display: block;
  background: url("") ;
  text-indent: 0;
  cursor: pointer;
}
.menu {
  display: block;
  position: absolute;
  right: -500px;
  width: 300px;
  height: 300px;
  background: rgb(12, 238, 151);
  transition-duration: 0.9s;
}
.menu.is-open {
  /* display: block; */
  transform: translateX(-500px);
  transition-duration: 0.9s;
}
.menu-flex-1 {
  display: flex;
  justify-content: center;
  width: 100%;
  height: 100%;
}
.menu-dropdown {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  width: 175px;
}
.button {
  height: 40px;
}
.button:hover {
  cursor: pointer;
}
</style>