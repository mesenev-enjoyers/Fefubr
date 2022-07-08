<template>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">

  <nav-bar></nav-bar>
  <div class="container">
    <table style="height: 100px;">
      <tbody>
      <tr>
        <td class="align-baseline"><img class="avatar" :src="user.avatar"></td>
        <td class="align-middle user-name">{{user.username}}</td>
        <td class="align-middle user-rate">Рейтинг: {{user.rating}}</td>
      </tr>
      </tbody>
    </table>
    <div class="change-btn-div" v-if="isAuthorized && isCurrentUser">
      <div class="question">
        <p>Вы можете поменять фото, выберите файл:</p>
      </div>
      <form @submit="changeAvatar">
        <div class="form-input">
          <input type="file" ref="file" @input="handleFileUpload">
        </div>
        <div class="form-btn">
          <button class="btn-photo">Поменять</button>
        </div>
      </form>
    </div>
    <div v-else-if="isAuthorized">
      <div class="btn-sub-div">
        <button class="btn-photo">Подписаться</button>
<!--        ИЛИ ОТПИСАТЬСЯ-->
      </div>
    </div>
    <div class="sorry" v-else>
      <a class="sorry-link" @click="$router.push('/login')">Авторизуйтесь</a>, чтобы следить за {{user.username}}
    </div>

    <div class="main-div row row-cols-2">
      <div class="user-subs-div d1 col">
        <p class="p-subs">Подписки:</p>
        <div class="subs-elements-div row row-cols-3">
          <a  class="sub-element col" v-for="sub in userSubscribe" :key="sub.id"  @click="$router.push('/user/' + sub.subscribe)">{{sub.subscribe_name}}</a>
        </div>
      </div>
      <div class="user-subs-div d2 col">
        <p class="p-subs">Тэги:</p>
        <div class="subs-elements-div row row-cols-3">
          <a  class="sub-element col" v-for="tag in userTags" :key="tag.id">{{tag.tag_name}}</a>
        </div>
      </div>
    </div>

  </div>
  <!--    <div class="user d-inline-flex ">-->
  <!--      <img class="avatar" :src="user.avatar">-->
  <!--      <div class="user-name align-middle">-->
  <!--        {{user.username}}-->
  <!--      </div>-->
  <!--      <div class="user-rate align-middle">-->
  <!--        Рейтинг: {{user.rating}}-->
  <!--      </div>-->
  <!--    </div>-->

  <!--  <nav-bar></nav-bar>-->
  <!--  <div class="root">-->
  <!--    <img :src="user.avatar">-->
  <!--    <div v-if="isAuthorized && isCurrentUser">-->
  <!--      <form @submit="changeAvatar">-->
  <!--        <input type="file" ref="file" @input="handleFileUpload">-->
  <!--        <button>Сменить</button>-->
  <!--      </form>-->
  <!--  </div>-->
  <!--    <div v-else-if="isAuthorized">АВторизован, но не мой акк</div>-->
  <!--    <div v-else>не авторизован</div>-->
  <!--  </div>-->
</template>

<script>
import axios from "axios";
import NavBar from "@/components/UI/NavBar";
export default {
  name: "ProfilePage",
  components: {NavBar},
  data() {
    return {
      user: {},
      userTags: [], //Теги, на которые чел подписан
      userSubscribe: [], //Люди, на которых чел подписан
      isAuthorized: localStorage.getItem('token') != null,
      isCurrentUser: false, // Проверка, что за чел перешл на страницу
      file: ''
    }
  },
  methods: {
    CheckUser() {
      if (this.isAuthorized) {
        axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
        axios.get('http://fefubr.tk/api/users/current').then((res) => {
          this.isCurrentUser = (res.data.id == this.$route.params.id)
        })
      }
    },
    getUserData() {
      axios.get('http://fefubr.tk/api/users/' + this.$route.params.id).then((res) => {
        this.user = res.data
        this.file = this.user.avatar
      })
      this.getUserTags()
      this.getUserSubscribe()
    },
    getUserTags() {
      axios.get('http://fefubr.tk/api/users/tag?user=' + this.$route.params.id).then((res) => {
        let tmp_uesrTags = []
        for (let i = 0; i < res.data.length; ++i) {
          tmp_uesrTags.push(res.data[i])
        }
        this.userTags = tmp_uesrTags
        console.log('i was here(tags)')
      })
    },
    getUserSubscribe() {
      axios.get('http://fefubr.tk/api/users/subscribe?user=' + this.$route.params.id).then((res) => {
        let tmp_userSubscribe = []
        for (let i = 0; i < res.data.length; ++i) {
          tmp_userSubscribe.push(res.data[i])
        }
        this.userSubscribe = tmp_userSubscribe
        console.log('i was here(subs)')
      })
    },
    handleFileUpload() {
      this.file = this.$refs.file.files[0]
    },
    changeAvatar() {
      const formData = new FormData()
      formData.append('avatar', this.file)
      axios.patch('http://fefubr.tk/api/users/' + this.user.id, formData, {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded'}
      }).then(() => {
        this.$router.go(0)
      }).catch((error) => {
        console.log(error)
      })
    },
  },
  mounted() {
    this.CheckUser()
    this.getUserData()
  },
  watch: {
    $route() {
      this.getUserData()
    }
  }
}
</script>

<style scoped>

.container{
  margin-top: 40px;
  margin-bottom: 40px;
  padding: 20px;
  box-shadow: -1px -1px 5px rgb(191, 191, 191), 1px 1px 5px rgb(191, 191, 191);
}

.avatar{
  width: 140px;
  height: 140px;
  margin-right: 30px;
}

.user-name{
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 40px;
  line-height: 48px;
  color: #000000;
  padding-right: 30px;

}

.user-rate{
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 30px;
  line-height: 30px;
  margin-right: 30px;
  color: #000000;
}

.change-btn-div{
  margin-top: 15px;
}

.question{
  margin-top: 10px;
}

.question p{
  margin-bottom: 10px;
}

.btn-photo{
  width: 150px;
  height: 40px;
  padding: 2px 5px 5px 5px;
  margin-right: 20px;
  color: black;
  background-color:white;
  border-width: 2px;
  border-color: #5F77BF;
  border-radius: 5px;
}

.btn-photo:hover{
  width: 150px;
  height: 40px;
  color: white;
  background-color: #5F77BF;
  border-color: #5F77BF;
}

.btn-photo:active {
  width: 150px;
  height: 40px;
  color: black;
  background-color:white;
  border-width: 2px;
  border-color: #5F77BF;
}

.form-input{
  margin-bottom: 20px;
}

.user-subs-div{
  margin-top: 60px;
  max-width: 30%;
}

.d1{
  margin-right: 50px;
}

.p-subs{
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 35px;
  line-height: 30px;
  color: #000000;
}

.sub-element{
  cursor: pointer;
  text-decoration: none;
  color: #5F77BF;
  width: auto;
}

.sub-element:hover{
  color: black;
}

.btn-sub-div{
  margin-top: 20px;
}

.sorry{
  margin-top: 10px;
}

.sorry-link{
  text-decoration: none;
  color: #5F77BF;
  cursor: pointer;
}






</style>