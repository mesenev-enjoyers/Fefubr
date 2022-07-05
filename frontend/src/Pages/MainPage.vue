<template>
  <nav-bar></nav-bar>
  <h1 v-if="isPostsLoading" style="text-align: center; margin-top: 20%">Идёт загрузка...</h1>
  <div v-else>
  <div v-if="posts.length > 0">
  <post-list :posts="posts"/>
  </div>
  <h1 v-else style="text-align: center; margin-top: 20%">Постов нет :(</h1>
  </div>
</template>

<script>
import axios from "axios";
import PostList from "@/Posts/PostList";
import NavBar from "@/components/UI/NavBar";
export default {
  components: {
    NavBar,
    PostList
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
      axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
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

</style>