<template>
  <!--    Импорт шрифта Inter-->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">
  <!--    Импорт шрифта Inter-->

  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <div class="bg">
    <div class="container">
      <div class="navbar__btns row">
        <div class="logo-div col-3">
          <p class="logo block">Fefubr</p>
        </div>
        <div class="main-div col-6">
          <button class="btn block" @click="$router.push('/')" >Все статьи</button>
          <button class="btn block" @click="$router.push('/mynews')" >Моя лента</button>
          <button class="btn block" @click="$router.push('/chats')" >Общение</button>
        </div>
        <div class="second-div col-3">
          <button class="svg block" @click="$router.push('/createpost')" >
            <img src="@/assets/write.png" alt="">
          </button>
          <button class="btn block" @click="$router.push('/login')" >Вход</button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: "NavBar",
  methods: {
  }
}
</script>

<style>

*{
  padding: 0;
  margin: 0;
}

.logo-div{
  padding-top: 10px;
  padding-bottom: 10px;
  pointer-events: none;
}

.main-div{
  padding-top: 23px;
}

.main-div button{
  padding-right: 40px;
}

.second-div{
  padding-top: 20px;
}

.second-div img {
  padding-right: 100px;
}

.bg{
  height: 82px;
  box-shadow: 0px 4px 4px gray;
  margin: 0;
}

.navbar__btns {
  height: 82px;
  max-width: 100%;
  margin: 0;
}

/*дизайн кнопок + эффект*/
button{
  outline: none; /* Для синий ободки */
  border: 0;
  background: transparent;}


.btn{
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 26px;
  line-height: 31px;
  color: black;
  text-decoration: none;
  text-decoration-thickness: 0px;
  text-underline-offset: 0px;

  transition-duration: 0.2s;
  transition-property: text-decoration-thickness, color, text-underline-offset, text-decoration;
}

.btn:hover{
  color: #5F77BF;
  text-decoration: underline;
  text-decoration-thickness: 4px;
  text-underline-offset: 9px;
}

/*дизайн кнопок + эффект*/

.logo{
  font-family: 'Inter';
  text-transform: uppercase;
  font-style: normal;
  font-weight: bold;
  font-size: 50px;
  line-height: 61px;
  color: #000000;
}

</style>