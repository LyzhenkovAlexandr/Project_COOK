<template>
  <div>
    <div id="Bar">
      <div id="Progress" :style="{'width': value + '%'}"></div>
    </div>
    <b-button class="mt-3"  v-on:click="create" >{{title}}</b-button>
  </div>
</template>

<style scoped>
#Bar {
  margin: auto auto;
  width: 60%;
  height: 20px;
  border-radius: 8px;
  background-color: #001C23;
}
#Progress{
  height: 20px;
  background-color:  #009DC1;
  border-radius: 8px;
}
</style>

<script>
  export default {
    data: () => {
      return{
        value: 0,
        title: 'Запуск',
        i: 50,
      }
    },
    methods: {
      create: function(){
          let intval = setInterval(() => {
          if(this.value < this.value + this.i){
          this.value += 0.5;
          this.i -=0.5;
          this.title = 'Продолжить';
          }
          else if(this.value >= 100){
            this.title='Блюдо готово';
          }
          else{
            this.i += 50;
            clearInterval(intval);
          }
          }, 10)
        }
      }
    
  }
</script>