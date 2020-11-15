<template>
  <section class="hot-plates">
    <span class="title">Десерты</span>
    <article class="box-line">
      <router-link tag="article" to="" class="box">
        <div><img src="@/assets/desert_plate_1.jpg" /></div>
        <span class="title">Рулет "Баунти"</span>
        <span class="desc"
          >Рулет "Баунти" - это очень простой в приготовлении рулет без выпечки, напоминающий по вкусу одноимённый батончик. Рекомендуем попробовать.</span
        >
      </router-link>

      <article class="box">
        <div><img src="@/assets/desert_plate_2.jpg" /></div>
        <span class="title">Шоколадные маффины</span>
        <span class="desc"
          >25 лет пеку, и всегда удачно! Рецепт, который проверен на детях! Много лет на каждый школьный праздник печем эти замечательные шоколадные маффины! Продукты простые, получается много и очень вкусно! Попробуйте раз, и вы сами все поймете! Получаются всегда!</span
        >
      </article>

      <article class="box">
        <div><img src="@/assets/desert_plate_3.jpg" /></div>
        <span class="title">Чак-Чак</span>
        <span class="desc"
          >В этом рецепте мы научим вас готовить самую популярную восточную сладость – чак-чак. Рецепт чак-чака с медом в домашних условиях позволяет приготовить великолепное сладкое блюдо из пресного теста и ароматного меда.</span
        >
      </article>

      <article class="box">
        <div><img src="@/assets/desert_plate_4.jpg" /></div>
        <span class="title">Десерт "Птичье молоко"</span>
        <span class="desc"
          >Десерт "Птичье молоко" - воздушный сливочно-ванильный мусс и шоколадная глазурь. Это не классический рецепт на агар-агаре, а вариация на желатине. Прекрасный вариант десерта без выпечки. Все гарантированно будут в восторге! Лучше один раз попробовать, потому как словами не передать этот вкус!</span
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