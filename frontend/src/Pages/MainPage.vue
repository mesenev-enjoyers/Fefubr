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
      selectedSort: 'time',
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

    timeSort() {
      this.selectedSort = "date"
    },
    ratingSort() {
      this.selectedSort = "rating"
    }

  },

  mounted() {
    this.fetchPosts()
  },

  watch: {
    selectedSort(newValue) {
      console.log(newValue)
      this.posts.sort(function (post1, post2) {
        if (post1[newValue] < post2[newValue])
          return 1
      })
    },
  }
}
</script>

<style scoped>

</style>