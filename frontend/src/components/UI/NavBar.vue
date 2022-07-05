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
<<<<<<< HEAD
            <svg width="46" height="46" viewBox="0 0 46 46" fill="none" xmlns="http://www.w3.org/2000/svg" >
              <path d="M21.0835 7.66669H7.66683C6.65017 7.66669 5.67514 8.07055 4.95625 8.78944C4.23736 9.50833 3.8335 10.4834 3.8335 11.5V38.3334C3.8335 39.35 4.23736 40.325 4.95625 41.0439C5.67514 41.7628 6.65017 42.1667 7.66683 42.1667H34.5002C35.5168 42.1667 36.4918 41.7628 37.2107 41.0439C37.9296 40.325 38.3335 39.35 38.3335 38.3334V24.9167" stroke="#5F77BF" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M35.4585 4.79169C36.221 4.0292 37.2552 3.60083 38.3335 3.60083C39.4118 3.60083 40.446 4.0292 41.2085 4.79169C41.971 5.55419 42.3994 6.58836 42.3994 7.66669C42.3994 8.74503 41.971 9.7792 41.2085 10.5417L23.0002 28.75L15.3335 30.6667L17.2502 23L35.4585 4.79169Z" stroke="#5F77BF" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
=======
            <img src="@/assets/write.png" alt="">
>>>>>>> d47b801a5a87a5c740415c17aebac3c4c527854a
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

<style scoped>

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