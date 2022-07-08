<template>
  <main-content-component :posts="posts"></main-content-component>
</template>

<script>
import axios from "axios";
import MainContentComponent from "@/components/UI/MainContentComponent";
export default {
  components: {
    MainContentComponent,
  },
  name: "MainPage",
  data() {
    return {
      isAuthorized: localStorage.getItem('token') != null,
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
  },
}
</script>

<style scoped>

</style>