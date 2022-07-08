<template>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">
  <main-content-component :selected-tag="currentTag.name" :posts="posts">
    <div class="row uprow-first-content rounded-1 justify-content-center">
      <div class="row content-uprow">
        <div class="btn-2-div">
          <button class="btn-2 " @click="unsubscribeFromTag" v-if="isSubscribe && isAuthorized">Отписаться</button>
          <button class="btn-2 " @click="subscribeToTag" v-else-if="isAuthorized && !isSubscribe">Подписаться</button>
        </div>
      </div>
    </div>
  </main-content-component>
</template>

<script>
import axios from "axios";
import MainContentComponent from "@/components/UI/MainContentComponent";
export default {
  name: "TagPage",
  components: {MainContentComponent},
  data() {
    return {
      isAuthorized: localStorage.getItem('token') != null,
      posts: [],
      currentTag: {
        name: '',
        id: ''
      },
      currentUser: {
        id: '',
        tags: []
      },
      isSubscribe: false,
      subscribeId: '',
    }
  },
  methods: {
    fetchPosts() {
      if (this.isAuthorized) {
        axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
        this.getCurrentUser()
      }
      this.getCurrentTag()
      axios.get('http://fefubr.tk/api/content/article?tag=' + this.$route.params.id).then((response) => {
        this.posts = response.data
      })
    },

    getCurrentUser() {
      axios.get('http://fefubr.tk/api/users/current').then((res) => {
        this.currentUser = res.data
        this.checkSubscriptionTo()
      })
    },

    getCurrentTag(){
      axios.get('http://fefubr.tk/api/content/tag/' + this.$route.params.id).then((res) => {
        this.currentTag.id = res.data.id
        this.currentTag.name = res.data.name
      })
    },

    checkSubscriptionTo() {
      axios.get('http://fefubr.tk/api/users/tag?user=' + this.currentUser.id).then((res) => { //Подписки чела, который першел на страницу
        this.currentUser.tags = res.data
        let check = false
        for (let i = 0; i < res.data.length; ++i) {
          if (this.currentTag.id === res.data[i].tag_subscribe) {
            check = true
            this.subscribeId = this.currentUser.tags[i].id
            break
          }
        }
        this.isSubscribe = check
        console.log((this.isSubscribe))
      })
    },
    subscribeToTag() {
      axios.post('http://fefubr.tk/api/users/tag/', {
        'user': this.currentUser.id,
        'tag_subscribe': this.$route.params.id
      }).then(() => {
        this.$router.go(0)
      })
    },
    unsubscribeFromTag() {
      axios.delete('http://fefubr.tk/api/users/tag/' + this.subscribeId).then(() => {
        this.$router.go(0)
      })
    }
  },
  mounted() {
    this.fetchPosts()
  },
  watch: {
    $route() {
      this.fetchPosts()
    },
  }
}
</script>

<style scoped>
.btns-div{
  width: auto;
}
.btn-2-div{
  width: auto;
  padding-top: 5px;
  padding-left: 0;
  margin-right: 50px;
}
.btns-div{
  padding: 0 0 0 30px;
  width: auto;
}


.btn{
  width: 200px;
  height: 40px;
  padding: 2px 5px 5px 5px;
  margin-right: 20px;
  color: black;
  background-color:white;
  border-width: 2px;
  border-color: #5F77BF;
}

.btn:hover{
  width: 200px;
  height: 40px;
  color: white;
  background-color: #5F77BF;
  border-color: #5F77BF;
}

.btn:active {
  width: 200px;
  height: 40px;
  color: black;
  background-color:white;
  border-width: 2px;
  border-color: #5F77BF;
}

.btn:focus {
  box-shadow: none !important;
}

.btn-2{
  width: 120px;
  height: 30px;
  color: black;
  background-color:white;
  border-width: 2px;
  border-color: #5F77BF;
  border-radius: 5px;
}

.btn-2:hover{
  color: white;
  background-color: #5F77BF;
  border-color: #5F77BF;
}

.btn-2:active {
  color: black;
  background-color:white;
  border-width: 2px;
  border-color: #5F77BF;
}
</style>