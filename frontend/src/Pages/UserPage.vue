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
      <div v-if="isSubscribeTo" class="btn-sub-div">
        <button  class="btn-photo" @click="unsubscribeFromUser">Отписаться</button>
      </div>
      <div v-else class="btn-sub-div">
        <button  class="btn-photo" @click="subscribeToUser">Подписаться</button>
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
          <a  class="sub-element col"  v-for="tag in userTags" :key="tag.id" @click="$router.push('/tag/' + tag.tag_subscribe)">{{tag.tag_name}}</a>
        </div>
      </div>
    </div>
    <p class="p-subs p-article">Cтатьи пользователя {{user.username}}:</p>
    <div class="articles-div row row-cols-2 d-flex justify-content-between">
      <div class="article-one-div col " v-for="article in userArticle" :key="article.id">
        <p class="p-article-content">{{article.name}}</p>
        <div class="button-read-div d-flex justify-content-center">
          <button class="button-read" @click="$router.push('/post/' + article.id)">Читать</button>
        </div>
      </div>

    </div>

    </div>
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
      currentUserId: '',
      userTags: [], //Теги, на которые чел подписан
      userSubscribe: [], //Люди, на которых чел подписан
      userArticle: [], //Статье данного чела
      isAuthorized: localStorage.getItem('token') != null,
      isCurrentUser: false, // Проверка, что за чел перешл на страницу
      isSubscribeTo: false,
      subscribeId: '',
      file: ''
    }
  },
  methods: {
    CheckUser() {
      if (this.isAuthorized) {
        axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
        axios.get('http://fefubr.tk/api/users/current').then((res) => {
          this.isCurrentUser = (res.data.id == this.$route.params.id)
          this.currentUserId = res.data.id
          this.checkSubscriptionTo()
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
      this.getUserArticle()
    },
    getUserTags() {
      axios.get('http://fefubr.tk/api/users/tag?user=' + this.$route.params.id).then((res) => {
        let tmp_userTags = []
        for (let i = 0; i < res.data.length; ++i) {
          tmp_userTags.push(res.data[i])
        }
        this.userTags = tmp_userTags
      })
    },
    getUserSubscribe() {
      axios.get('http://fefubr.tk/api/users/subscribe?user=' + this.$route.params.id).then((res) => { //Подписки чела, на страницу
        let tmp_userSubscribe = []                                                                        // мы перешли
        for (let i = 0; i < res.data.length; ++i) {
          tmp_userSubscribe.push(res.data[i])
        }
        this.userSubscribe = tmp_userSubscribe
      })
    },
    getUserArticle() {
      axios.get('http://fefubr.tk/api/content/article?user=' + this.$route.params.id).then((res) => {
        let tmp_userArticle = []
            for (let i = 0; i < res.data.length; ++i) {
              tmp_userArticle.push(res.data[i])
            }
            this.userArticle = tmp_userArticle
      })
    },

    checkSubscriptionTo() {
      axios.get('http://fefubr.tk/api/users/subscribe?user=' + this.currentUserId).then((res) => { //Подписки чела, который першел на страницу
        let currentUserSubs = res.data
        let check = false
        for (let i = 0; i < currentUserSubs.length; ++i) {
          if (this.user.id === currentUserSubs[i].subscribe) {
            check = true
            this.subscribeId = currentUserSubs[i].id
            break
          }
        }
        this.isSubscribeTo = check
      })
    },
    subscribeToUser() {
      if (this.isAuthorized)
        axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
      axios.post('http://fefubr.tk/api/users/subscribe/', {
        'user': this.currentUserId,
        'subscribe': this.$route.params.id
      }).then(() => {
        this.$router.go(0)
      })
    },
    unsubscribeFromUser() {
      axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
      axios.delete('http://fefubr.tk/api/users/subscribe/' + this.subscribeId).then(() => {
        this.$router.go(0)
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
      this.CheckUser()
      this.getUserData()
    },
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
  color: #14A61A;

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

.p-article{
  margin-top: 40px;
}

.articles-div{
  margin-top: 20px;
}

.article-one-div{
  border: #5F77BF 2px solid;
  border-radius: 5px;
  width: 45%;
  padding: 0;
  margin-left: 11px;
  margin-right: 12px;
  margin-top: 20px;
  height: auto;
  word-wrap: break-word;
}


.p-article-content{
  padding: 10px;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 20px;
  color: #000000;
  margin-bottom: 0;
  text-align: center;
}

.button-read{
  width: 100px;
  height: 30px;
  color: black;
  background-color:white;
  border-width: 2px;
  border-color: #5F77BF;
  border-radius: 10px;
  margin-bottom: 10px;
}

.button-read:hover{
  width: 100px;
  height: 30px;
  color: white;
  background-color: #5F77BF;
  border-color: #5F77BF;
}

.button-read:active {
  width: 100px;
  height: 30px;
  color: black;
  background-color:white;
  border-width: 2px;
  border-color: #5F77BF;
}

@media (max-width: 1100px){
  .user-name{
    font-size: 25px;

  }
  .user-rate{
    font-size: 15px;

  }
}

@media (max-width: 550px){
  .d1{
    margin-right: 100px;
  }
}






</style>