<template>
  <section class="hot_1">
    <span class="title">Закуски</span>
    <article class="box-line">
      <article class="box">
        <div v-if="this.value==0"><img src="@/assets/snack_plate_2.jpg" /></div>
        <span class="title">Сырные палочки</span>
        <span class="desc" v-if="this.value==0">Простой, но очень вкусный рецепт домашних сырных палочек. Пальчики оближешь! Минимум продуктов и максимум удовольствия, а с приготовлением справится даже ребёнок</span>
        <span class="desc" v-else-if="0<this.value && this.value<=20.1"><strong>Ингредиенты</strong><br>
          Сыр твердый - 300 г              <br>
          Яйцо - 1 шт.                                   <br>
          Мука - 30 г                <br>
          Масло растительное - 70 мл                                <br></span>

        <span class="desc" v-else-if="20.1<this.value && this.value <=40.1">Приготовим продукты для сырных палочек.</span>
        <span class="desc" v-else-if="40.1<this.value && this.value <=60.1">Сыр натереть на мелкой терке, добавить муку, яйцо. Перемешать. Сформировать сырные палочки.</span>
        <span class="desc" v-else-if="60.1<this.value && this.value <=80">Обжарить их в растительном масле до золотистого цвета.</span>
        <span class="desc" v-else-if="80<this.value && this.value <=100">Сырные палочки готовы! <br><br><b>Приятного аппетита!</b></span>
        <span class="desc" v-else>Прятного аппетита!</span>

        <div v-if="0<this.value && this.value<=20.1"><img src="@/assets/snack_plate_2.jpg" /></div>
        <div v-else-if="20.1<this.value && this.value <=40.1"><img src="@/assets/snack_recept_1.jpg" /></div>
        <div v-else-if="40.1<this.value && this.value <=60.1"><img src="@/assets/snack_recept_2.jpg" /></div>
        <div v-else-if="60.1<this.value && this.value <=80"><img src="@/assets/snack_recept_3.jpg" /></div>
        <div v-else-if="80<this.value && this.value <=100"><img src="@/assets/snack_recept_4.jpg" /></div>

        <article class="progress_bar">
          <b-button class="mt-3 button" v-on:click="left">Вернуться на шаг</b-button>
          <b-button class="mt-3 button" v-on:click="create">{{
            title
          }}</b-button>
          <b-button class="mt-3 button" v-on:click="right">Пропустить шаг</b-button>
          <div id="Bar">
            <div id="Progress" :style="{ width: value + '%' }"></div>
          </div>
          <!-- <span class="mark"
            >*Нажав на кнопку запуска таймера несколько раз, можно ускорить ход
            времени</span
          > -->
        </article>
      </article>
    </article>
  </section>
</template>

<script>
import axios from 'axios';

export default {
  data: () => {
    return {
      value: 0,
      title: "Начать готовить",
      desc:
        "Свиные рёбрышки в пикантном томатно-медовом маринаде, буквально тающие во рту!",
      i: 20,
      current: 0,
      cards: [],
    };
  },
  methods: {
    create: function () {
      let intval = setInterval(() => {
        if (this.value < this.value + this.i) {
          this.value += 0.1;
          this.i -= 0.1;
          this.title = "Продолжить";
          this.img = "@/assets/hot_1_ingredients.png";
          this.desc = "";
          this.current = this.cards.find(i => i.id ++)
          
          console.log(this.value);
        } else if (this.value >= 100) {
          this.title = "Блюдо готово";
        } else {
          this.i += 20;
          clearInterval(intval);
        }
      }, 1);
      this.getCard()
    },
    right: function () {
      let intval = setInterval(() => {
        if (this.value < this.value + this.i) {
          this.value += 20;
          this.i -= 20;
          this.title = "Продолжить";
          this.img = "@/assets/hot_1_ingredients.png";
          this.desc = "";
        } else if (this.value >= 100) {
          this.title = "Блюдо готово";
        } else {
          this.i += 20;
          clearInterval(intval);
        }
      }, 10);
      this.getCard()
    },
    left: function () {
      let intval = setInterval(() => {
        if (this.value > this.value + this.i) {
          this.value -= 20;
          this.i += 20;
          this.title = "Продолжить";
          this.img = "@/assets/hot_1_ingredients.png";
          this.desc = "";
        } else if (this.value <= 0) {
          this.title = "Запуск";
        } else {
          this.i -= 20;
          clearInterval(intval);
        }
      }, 10);
      this.getCard()
    },
    getCard() {
      const path = 'http://localhost:5000//hot_list/hot_1';
      axios.get(path)
        .then((res) => {
          this.cards = res.data.card;
        })
        .catch((error) => {
          // eslint-выключение следующей строки
          console.error(error);
        });
    },
  },
  created() {
    this.getCard();
  },
}
</script>

<style>
#Bar {
  margin: 0 10px;
  width: 580px;
  height: 20px;
  border-radius: 9px;
  background-color: #012d38;
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

.hot_1 .progress_bar {
  clear: both;
  display: block;
  width: 100%;
  text-align: center;
}

.hot_1 .progress_bar .button {
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

.hot_1 .box-line {
  position: absolute;
  display: block;
  width: 100%;
  text-align: center;
  margin-top: 10px;
}

.hot_1 .box {
  display: inline-block;
  width: 600px;
  min-height: 300px;
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
.hot_1 .box div {
  height: 210px;
  width: 200px;
  margin: 10px;
  float: left;
  overflow: hidden;
  border-radius: 32px;
  border-bottom-right-radius: 8px;
  text-align: center;
}
.hot_1 .box img {
  height: 210px;
  margin: 0;
}
.hot_1 .title {
  display: block;
  color: #fff;
  font-size: 25px;
  font-weight: bold;
  text-align: center;
  padding-top: 15px;
}
.hot_1 .box .title {
  color: #000;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  padding-top: 10px;
  margin-right: 10px;
}

.hot_1 .box .desc {
  width: 340px;
  margin: 10px 20px 10px 0;
  display: block;
  color: #000;
  font-size: 14px;
  font-weight: normal;
  float: right;
  text-indent: 15px;
}

.hot_1 .mark {
  background: none;
  margin-bottom: -15px;
  float: left;
  width: 100%;
}

@media only screen and (max-width: 500px) {
  #Bar {
    margin: 0 10px;
    width: 280px;
    height: 20px;
    border-radius: 9px;
    background-color: #001C23;
  }

  .hot_1 .progress_bar .button {
    clear: both;
    margin-left: 10px;
    width: 160px;
    height: 30px;
  }

  .hot_1 .progress_bar {
    text-align: center;
  }

  .hot_1 .box {
    display: inline-block;
    width: 300px;
    min-height: 300px;
    margin: 10px;
  }
  .hot_1 .box div {
    height: 230px;
    width: 280px;
    clear: both;
    border-radius: 32px;
    border-bottom-right-radius: 8px;
    border-bottom-left-radius: 8px;
  }
  .hot_1 .box img {
    height: 230px;
  }

  .hot_1 .box .desc {
    width: 280px;
    margin: 10px;
    clear: both;
    text-indent: 15px;
  }

  /* .hot_1 .mark {
    background: none;
    margin-bottom: -15px;
    float: left;
    width: 100%;
  } */
}
</style>