<template>
  <!--    Импорт шрифта Inter-->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.3/font/bootstrap-icons.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">
  <!--    Импорт шрифта Inter-->
  <nav class="navbar navbar-expand-lg navbar-light bg sticky-top mx-auto">
    <div class="container-fluid container">
      <a class="navbar-brand logo block" href="#">Fefubr</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse sm" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0 ">
          <li class="nav-item ps-lg-5 px-lg-3">
            <button class="btn block " @click="$router.push('/')" >Все статьи</button>
          </li>
          <li class="nav-item px-lg-3">
            <button class="btn block" v-if="isAuthorized" @click="$router.push('/mynews')">Моя лента</button>
            <button class="btn block" v-else @click="$router.push('/login')">Моя лента</button>
          </li>
          <li class="nav-item px-lg-3">
            <button class="btn block" v-if="isAuthorized" @click="$router.push('/chats')" >Рассылка</button>
            <button class="btn block" v-else @click="$router.push('/login')" >Общение</button>
          </li>
        </ul>
        <div class="second-content-navbar">
          <button class="svg write float-start" v-if="isAuthorized" @click="$router.push('/createpost')">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
              <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
              <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
            </svg>
          </button>

          <button class="svg write float-start" v-else @click="$router.push('/login')">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
              <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
              <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
            </svg>
          </button>

          <button class="svg float-end" v-if="isAuthorized" @click="getCurrentUser">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
              <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
              <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
            </svg>
          </button>

          <button class="btn float-end exit" v-if="!isAuthorized" @click="$router.push('/login')" >Вход</button>
          <button class="btn float-end exit" v-else @click="logout" >Выйти</button>
        </div>
      </div>
    </div>
  </nav>
</template>


<script>
import axios from "axios";

export default {
  name: "NavBar",
  data() {
    return {
      isAuthorized: localStorage.getItem('token') != null,
      token: localStorage.getItem('token'),
      userId: ''
    }
  },
  methods: {
    logout() {
      this.token = localStorage.getItem('token')
      localStorage.removeItem('token')
      axios.post("http://fefubr.tk/api/auth/token/logout",{headers: {Authorization: `Token ${this.token}`}})
      this.token = ''
      this.$router.go(0)
    },
    getCurrentUser() {
      axios.get('http://fefubr.tk/api/users/current').then((res) => {
        this.userId = res.data.id
        this.$router.push("/user/" + this.userId)
      })
    }
  }
}
</script>

<style scoped>




.navbar-collapse{
  background-color: white;
}

.collapse{
  margin-top: 10px;
}

.second-content-navbar{
  width: 30%;
}


.write{
  text-align: left;
}

svg{
  width: 45px;
  height: 45px;
}

svg:hover{
  fill: #5F77BF;
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

/*.main-div button{*/
/*  padding-right: 40px;*/
/*}*/

.second-div{
  /*padding-top: 20px;*/
  padding-right: 0;
  padding-left: 0;
}


.bg{
  background-color: white;
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
  font-size: 25px;
  line-height: 31px;
  color: black;
  text-decoration: none;
  text-decoration-thickness: 0;
  text-underline-offset: 0;
  transition-duration: 0.2s;
  transition-property: color, text-decoration-thickness, text-underline-offset, text-decoration;
}

.btn:hover{
  text-decoration: underline;
  text-decoration-thickness: 4px;
  text-underline-offset: 9px;
  color: #5F77BF;

}

.btn:focus {
  box-shadow: none !important;
}

.navbar-toggler:focus{
  box-shadow: none;
}

.exit{
  padding-right: 10px;
}




@media (max-width: 1350px){
  .logo{
    font-size: 35px;
  }
  button{
    padding: 0 0 10px 0;
  }
  .exit{
    padding: 5px 5px 10px 0;
  }
  .btn{
    font-size: 20px;
  }
  .bg{
    margin-bottom: 20px;
  }
  .navbar-nav{
    padding-top: 10px;
  }

}

@media (max-width: 1001px){

  .second-content-navbar{
    width: 50%;
  }
  .collapse{
    box-shadow: -1px -1px 5px rgb(191, 191, 191), 1px 1px 5px rgb(191, 191, 191);
    border-radius: 10px;
    padding: 10px;
    margin-top: 0;
  }

  .navbar{
    height: 55px;
    padding-top: 0;
  }

  .navbar-brand{
    padding-top: 0;
  }



}


</style>