<template>
  <section>
    <span class="title">Закуски</span>
    <article class="box-line">
      <article class="box">
        <div><img src="@/assets/hot_plate_1.jpg" /></div>
        <span class="title">Запечённые свиные рёбрышки</span>
        <span class="desc">{{ desc }}</span>

        <article class="progress_bar">
          <b-button class="mt-3 button" v-on:click="create">{{
            title
          }}</b-button>
          <div id="Bar">
            <div id="Progress" :style="{ width: value + '%' }"></div>
          </div>
        </article>
      </article>
    </article>
  </section>
</template>

<script>
export default {
  data: () => {
    return {
      value: 0,
      title: "Начать готовить",
      desc:
        "Свиные рёбрышки в пикантном томатно-медовом маринаде, буквально тающие во рту!",
      i: 50,
    };
  },
  methods: {
    create: function () {
      let intval = setInterval(() => {
        if (this.value < this.value + this.i) {
          this.value += 0.01;
          this.i -= 0.05;
          this.title = "Продолжить";
          this.img = "@/assets/hot_1_ingredients.png"
          this.desc="Ингредиенты \r\n Рёбрышки свиные - 1 кг\r\nЛук репчатый - 1 шт.\nСок лимона - 1 ст. ложка</br>Томатная паста - 1,5 ст. ложки</br>Мёд - 1 ст. ложка</br>Горчица - 0,5 ст. ложки</br>Гвоздика - 2 шт.</br>Перец чёрный горошком - 10 шт.</br>Перец красный молотый - по вкусу</br>Соль - по вкусу</br>Вода - 650 мл"
        } else if (this.value >= 100) {
          this.title = "Блюдо готово";
        } else {
          this.i += 50;
          clearInterval(intval);
        }
      }, 10);
    },
  },
};
</script>

<style scoped>
#Bar {
  margin: 0 10px;
  width: 580px;
  height: 20px;
  border-radius: 9px;
  background-color: #001C23;
}
#Progress {
  position: relative;
  top: 0;
  left: 0;
  height: 20px;
  margin: 0;
  background-color: #009DC1;
  border-radius: 8px;
}

.progress_bar {
  clear: both;
  display: block;
  width: 100%;
  text-align: center;
}

.progress_bar .button {
  float: left;
  margin-bottom: 10px;
  margin-left: 30px;
  width: 160px;
  height: 30px;

  border: 1.5px solid #000000;
  box-sizing: border-box;
  border-radius: 8px;
  outline-width: 0;
  background: #fff;
}

.box-line {
  position: absolute;
  display: block;
  width: 100%;
  text-align: center;
  margin-top: 10px;
}

.box {
  display: inline-block;
  width: 600px;
  height: 300px;
  background: #FFFFFF;
  box-sizing: border-box;
  box-shadow: 17px 17px 4px rgba(0, 0, 0, 0.25);
  border-radius: 40px;
  margin: 12px;
  padding-bottom: 20px;
  overflow: hidden;
  text-align: left;
  border-bottom-right-radius: 8px;
  border-bottom-left-radius: 8px;
}
.box div {
  height: 210px;
  width: 200px;
  margin: 10px;
  float: left;
  overflow: hidden;
  border-radius: 32px;
  border-top-right-radius: 8px;
  text-align: center;
}
.box img {
  height: 210px;
  margin: 0;
}

.title {
  display: block;
  color: #fff;
  font-size: 25px;
  font-weight: bold;
  text-align: center;
  padding-top: 15px;
}

.box .title {
  color: #000;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  padding-top: 10px;
  margin-right: 10px;
}

.box .desc {
  width: 340px;
  margin: 10px 20px 10px 0;
  display: block;
  color: #000;
  font-size: 14px;
  font-weight: normal;
  float: right;
  text-indent: 15px;
}
</style>