<template>
  <section>
    <span>Рецепты</span>
    <span
      >Ищете рецепт? Тогда наш сайт идеально для вас подходит! Выберете наиболее
      подходящую для вас категорию блюд и увидите список всех доступных
      рецептов. Удачной готовки!
    </span>
    <article class="box-line">
      <article class="box">
        <button>Закуски</button>
      </article>

      <article class="box">
        <button>Холодные блюда</button>
      </article>

      <article class="box">
        <button>Горячие блюда</button>
      </article>

      <article class="box">
        <button>Десерты</button>
      </article>
    </article>
  </section>
</template>

<script>
export default {};
</script>

<style>
.box-line {
  position: absolute;
  display: block;
  width: 100%;
  text-align: center;
  margin-top: 150px;
}
.box {
  display: inline-block;
  width: 235px;
  height: 235px;
  background: #FFFFFF;
  box-sizing: border-box;
  box-shadow: 17px 17px 4px rgba(0, 0, 0, 0.25);
  border-radius: 40px;
  margin-right: 25px;
}
.box:last-child {
  margin-right: 0;
}
.box button {
    position: relative;
    top:0;
  width: 180px;
  height: 40px;

  border: 1.5px solid #000000;
  box-sizing: border-box;
  border-radius: 8px;
  outline-width: 0;
  background: #fff;
}
</style>