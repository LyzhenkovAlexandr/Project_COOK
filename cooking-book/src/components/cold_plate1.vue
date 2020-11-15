<template>
  <section class="hot_1">
    <span class="title">Салаты</span>
    <article class="box-line">
      <article class="box">
        <div v-if="this.value==0"><img src="@/assets/cold_plate_1.jpg" /></div>
        <span class="title">Салат Цезарь</span>
        <span class="desc" v-if="this.value==0">Салат цезарь в нашу жизнь вошёл недавно, но за короткое время успел завоевать наши сердца и желудки.</span>
        <span class="desc" v-else-if="0<this.value && this.value<=10.1"><strong>Ингредиенты</strong><br>
          Салат айсберг или подобный - 200 г                <br>
          Сыр пармезан – 50 г                  <br>
          Хлеб чиабатта (или белый батон) - 100 г                <br>
          Чеснок - 1 зубчик          <br>
          Масло оливковое - 1 ст. л.                    <br>
          Соль - по вкусу              <br>
          Перец черный молотый - по вкусу                     <br>
          Заправка для салата "Цезарь" - 4-5 ст. ложек   <br>
          <b>Для заправки:</b>      <br>
          Горчица - 1 ч. л.  <br>
          Кефир - 2 ст. л.                  <br>
          Масло оливковое - 2 ст. л.    <br>
          Желток растертый - 1 шт.<br>
          Соль - по вкусу<br>
          Соус соевый (по желанию) - 1 ст. л. <br>
          Орегано - 1 щепотка                   <br></span>

        <span class="desc" v-else-if="10.1<this.value && this.value <=20.2">Подготовьте все ингредиенты для приготовления классического салата "Цезарь"</span>
        <span class="desc" v-else-if="20.2<this.value && this.value <=30.2">Как приготовить салат "Цезарь" классический: Чиабатту или белый батон нарежьте тонкими брусочками.</span>
        <span class="desc" v-else-if="30.2<this.value && this.value <=40.2">Сбрызните хлеб оливковым маслом, немного посолите и смажьте измельченным чесноком.</span>
        <span class="desc" v-else-if="40.2<this.value && this.value <=50.2">Обжарьте чиабатту на сухой сковороде с обеих сторон до румяной корочки.</span>
        <span class="desc" v-else-if="50.2<this.value && this.value <=60.2">Натрите пармезан на мелкой терке или измельчите на специальной терке для твердых сыров.</span>
        <span class="desc" v-else-if="60.2<this.value && this.value <=70.2">На порционную тарелку нарвите руками листья салата.</span>
        <span class="desc" v-else-if="70.2<this.value && this.value <=80.1">Сверху выложите ложку натертого пармезана.</span>
        <span class="desc" v-else-if="80.1<this.value && this.value <=90.2">Для заправки смешайте растертый желток, 1 чайную ложку горчицы, 2 столовых ложки кефира, 2 столовых ложки оливкового масла, немного соли, по желанию 1 столовую ложку соевого соуса и щепотку орегано. Налейте несколько ложек заправки в салат. Перемешайте салат цезарь.</span>
        <span class="desc" v-else-if="90.2<this.value && this.value <=100.1">Сверху немного посыпьте салат натертым на мелкой терке сыром и выложите сухарики. Салат "Цезарь" классический готов. <br><br><b>Приятного аппетита!</b></span>
        <span class="desc" v-else>Прятного аппетита!</span>


        <div v-if="0<this.value && this.value<=10.1"><img src="@/assets/cold_plate_1.jpg" /></div>
        <div v-else-if="10.1<this.value && this.value <=20.2"><img src="@/assets/cold_recept_1.jpg" /></div>
        <div v-else-if="20.2<this.value && this.value <=30.2"><img src="@/assets/cold_recept_2.jpg" /></div>
        <div v-else-if="30.2<this.value && this.value <=40.2"><img src="@/assets/cold_recept_3.jpg" /></div>
        <div v-else-if="40.2<this.value && this.value <=50.2"><img src="@/assets/cold_recept_4.jpg" /></div>
        <div v-else-if="50.2<this.value && this.value <=60.2"><img src="@/assets/cold_recept_5.jpg" /></div>
        <div v-else-if="60.2<this.value && this.value <=70.2"><img src="@/assets/cold_recept_6.jpg" /></div>
        <div v-else-if="70.2<this.value && this.value <=80.1"><img src="@/assets/cold_recept_7.jpg" /></div>
        <div v-else-if="80.1<this.value && this.value <=90.2"><img src="@/assets/cold_recept_8.jpg" /></div>
        <div v-else-if="90.2<this.value && this.value <=100.1"><img src="@/assets/cold_recept_9.jpg" /></div>

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
      i: 10,
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
          this.i += 10;
          clearInterval(intval);
        }
      }, 50);
      this.getCard()
    },
    right: function () {
      let intval = setInterval(() => {
        if (this.value < this.value + this.i) {
          this.value += 10;
          this.i -= 10;
          this.title = "Продолжить";
          this.img = "@/assets/hot_1_ingredients.png";
          this.desc = "";
        } else if (this.value >= 100) {
          this.title = "Блюдо готово";
        } else {
          this.i += 10;
          clearInterval(intval);
        }
      }, 10);
      this.getCard()
    },
    left: function () {
      let intval = setInterval(() => {
        if (this.value > this.value + this.i) {
          this.value -= 10.1;
          this.i += 10;
          this.title = "Продолжить";
          this.img = "@/assets/hot_1_ingredients.png";
          this.desc = "";
        } else if (this.value <= 0) {
          this.title = "Запуск";
        } else {
          this.i -= 10;
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