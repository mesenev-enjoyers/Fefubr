<template>
  <!--    Импорт шрифта Inter-->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">
  <!--    Импорт шрифта Inter-->

  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <div class="bg sticky-top">
    <div class="container ">
      <div class="navbar__btns row">
        <div class="logo-div col-3">
          <p class="logo block">Fefubr</p>
        </div>
        <div class="main-div col-6">
          <button class="btn block" @click="$router.push('/')" >Все статьи</button>
          <button class="btn block" v-if="isAuthorized" @click="$router.push('/mynews')">Моя лента</button>
          <button class="btn block" v-else @click="$router.push('/login')">Моя лента</button>
          <button class="btn block" v-if="isAuthorized" @click="$router.push('/chats')" >Общение</button>
          <button class="btn block" v-else @click="$router.push('/login')" >Общение</button>
        </div>
        <div class="second-div col-3">
          <button class="svg block" v-if="isAuthorized" @click="$router.push('/createpost')">
            <img src="@/assets/write.png" alt="">
          </button>
          <button class="svg block" v-else @click="$router.push('/login')">
            <img src="@/assets/write.png" alt="">
          </button>
          <button class="btn block" v-if="!isAuthorized" @click="$router.push('/login')" >Вход</button>
          <button class="btn block" v-else @click="logout" >Выйти</button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";

export default {
  name: "NavBar",
  data() {
    return {
      isAuthorized: localStorage.getItem('token') != null,
      token: localStorage.getItem('token')
    }
  },
  methods: {
    logout() {
      this.token = localStorage.getItem('token')
      localStorage.removeItem('token')
      axios.post("http://fefubr.tk/api/auth/token/logout",{headers: {Authorization: `Token ${this.token}`}})
      this.token = ''
      this.$router.go(0)
    }
  }
}
</script>

<style scoped>

.bg{
  background-color: white;
}

.container{
  padding: 0;
}

.logo-div{
  padding: 10px 0 10px 0;
  pointer-events: none;
}

.logo{
  font-family: 'Inter';
  text-transform: uppercase;
  font-style: normal;
  font-weight: bold;
  font-size: 50px;
  line-height: 61px;
  color: #000000;

}

.main-div{
  padding-top: 23px;
  padding-right: 0;
  padding-left: 0;

}

.main-div button{
  padding-right: 40px;
}

.second-div{
  padding-top: 20px;
  padding-right: 0;
  padding-left: 0;
}

.second-div img {
  padding-right: 100px;
}

.bg{
  height: 82px;
  box-shadow: 0 4px 4px gray;
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
  text-decoration-thickness: 0;
  text-underline-offset: 0;

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



</style>