<template>
  <section class="hot-plates">
    <span class="title">Закуски</span>
    <article class="box-line">
      <router-link tag="article" to="/Snack_list/snack_1" class="box">
        <div><img src="@/assets/snack_plate_2.jpg" /></div>
        <span class="title">Сырные палочки</span>
        <span class="desc"
          >Простой, но очень вкусный рецепт домашних сырных палочек. Пальчики оближешь! Минимум продуктов и максимум удовольствия, а с приготовлением справится даже ребёнок.</span
        >
      </router-link>

      <article class="box">
        <div><img src="@/assets/snack_plate_1.jpg" /></div>
        <span class="title">Канапе с колбасой и сыром</span>
        <span class="desc"
          >Простая в приготовлении, красивая, вкусная праздничная закуска для семейного новогоднего меню - канапе с колбасой и сыром.</span
        >
      </article>

      <article class="box">
        <div><img src="@/assets/snack_plate_3.jpg" /></div>
        <span class="title">Луковые кольца в кляре</span>
        <span class="desc"
          >Приготовим луковые кольца в кляре. Хрустящее нежное тесто, сладкий и сочный лук с особенным вкусом - отличная закуска или гарнир, с любимым соусом.</span
        >
      </article>

      <article class="box">
        <div><img src="@/assets/snack_plate_4.jpg" /></div>
        <span class="title">Закусочные пирожки из слоёного теста</span>
        <span class="desc"
          >Небольшие румяные закусочные пирожки из слоеного теста, напоминающие пельмени, - это отличная закуска из готового слоеного теста, которую совсем несложно приготовить.</span
        >
      </article>
    </article>
  </section>
</template>

<script>
export default {};
</script>

<style>
.hot-plates .box-line {
  position: absolute;
  display: block;
  width: 100%;
  text-align: center;
  margin-top: 15px;
}
.hot-plates .box {
  display: inline-block;
  width: 470px;
  height: 230px;
  background: #FFFFFF;
  box-sizing: border-box;
  box-shadow: 17px 17px 4px rgba(0, 0, 0, 0.25);
  border-radius: 40px;
  margin: 12px;
  overflow: hidden;
  text-align: left;
}
.hot-plates .box div {
  height: 210px;
  width: 200px;
  margin: 10px;
  float: left;
  overflow: hidden;
  border-radius: 32px;
  border-top-right-radius: 8px;
  border-bottom-right-radius: 8px;
  text-align: center;
}
.hot-plates .box img {
  height: 210px;
  margin: 0;
}


.hot-plates .title {
  display: block;
  color: #fff;
  font-size: 25px;
  font-weight: bold;
  text-align: center;
  padding-top: 15px;
}

.hot-plates .box .title {
  color: #000;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  padding-top: 10px;
  margin-right: 10px;
}

.hot-plates .box .desc {
  width: 220px;
  margin: 10px;
  display: block;
  color: #000;
  font-size: 14px;
  font-weight: normal;
  float: right;
  text-indent: 15px;
}

@media only screen and (max-width: 1024px) {
.hot-plates .box {
  display: inline-block;
  width: 235px;
  min-height: 470px;
}
.box div {
  height: 210px;
  width: 215px;
  margin: 10px;
  clear: both;
  border-radius: 32px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  text-align: center;
}

.hot-plates .box .desc {
  width: 215px!important;
  margin: 10px;
  display: block;
  color: #000;
  font-size: 14px;
  font-weight: normal;
  clear:both;
  text-indent: 15px;
}
}
</style>