<template>
  <section class="main-content">
    <span class="title">Рецепты</span>
    <span class="desc"
      >Ищете рецепт? Тогда наш сайт идеально для вас подходит! Выберете наиболее
      подходящую для вас категорию блюд и увидите список всех доступных
      рецептов. Удачной готовки!
    </span>
    <article class="box-line">
      <article class="box">
          <img src="@/assets/category1.png">
        <router-link to="/snack" tag="button">Закуски</router-link>
      </article>

      <article class="box">
          <img src="@/assets/category2.png">
        <router-link to="/cold_list" tag="button">Салаты</router-link>
      </article>

      <article class="box">
          <img src="@/assets/category3.png">
        <router-link to="/hot_list" tag="button">Горячие блюда</router-link>
      </article>

      <article class="box">
          <img src="@/assets/category4.png">
        <router-link to="/desert" tag="button">Десерты</router-link>
      </article>
    </article>
  </section>
</template>

<script>
export default {};
</script>

<style>
.main-content .box-line {
  position: absolute;
  display: block;
  width: 100%;
  text-align: center;
  margin-top: 35px;
}
.main-content .box {
  display: inline-block;
  width: 235px;
  height: 235px;
  background: #FFFFFF;
  box-sizing: border-box;
  box-shadow: 17px 17px 4px rgba(0, 0, 0, 0.25);
  border-radius: 40px;
  margin: 12px;
}

.main-content .box img {
    width:160px;
    height: 160px;
}
.main-content .box button {
    margin-top: 10px;
  width: 160px;
  height: 30px;

  border: 1.5px solid #000000;
  box-sizing: border-box;
  border-radius: 8px;
  outline-width: 0;
  background: #fff;
}
.box button :hover{
background: #001C23;
color:#fff;
}

.main-content .title {
    display: block;
    color: #fff;
    font-size: 25px;
    font-weight: bold;
    text-align: center;
    padding-top: 15px;
}

.main-content .desc {
    display: block;
    color: #fff;
    font-size: 17px;
    font-weight: normal;
    text-align: center;
    padding-top: 8px;
    padding: 0 17%;
}
</style>