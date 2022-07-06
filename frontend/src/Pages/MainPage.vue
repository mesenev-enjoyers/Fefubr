<template>
  <nav-bar></nav-bar>
  <div class="content">
    <div class="mainContent">
      <h1 v-if="isPostsLoading" style="text-align: center; margin-top: 20%">Идёт загрузка...</h1>
      <div v-else>
        <div v-if="posts.length > 0">
           <post-list :posts="posts"/>
        </div>
        <h1 v-else style="text-align: center; margin-top: 20%">Постов нет :(</h1>
      </div>
    </div>
    <div class="sideBar">
      <top-users></top-users>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import PostList from "@/Posts/PostList";
import NavBar from "@/components/UI/NavBar";
import TopUsers from "@/components/UI/TopUsers";
export default {
  components: {
    TopUsers,
    NavBar,
    PostList,
  },
  name: "MainPage",
  data() {
    return {
      isAuthorized: localStorage.getItem('token') != null,
      User: {
        name: '',
        rating: '',
      },
      posts: [],
      isPostsLoading: false,
    }
  },
  methods: {
    async fetchPosts() {
      if (this.isAuthorized)
        axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
      else
        console.log("I'm not authorized!")
      this.isPostsLoading = true
      const response = await axios.get('http://fefubr.tk/api/content/article')
      this.posts = response.data
      this.isPostsLoading = false
    },

  },

  mounted() {
    this.fetchPosts()
  }


}
</script>

<style scoped>
.content {
  display: flex;
}
.mainContent {
  width: 70%;
  text-align: center;
  border: 1px solid black;
  box-shadow: -1px -1px 5px gray, 1px 1px 5px gray;
}
.sideBar {
  width: 30%;
}
</style>