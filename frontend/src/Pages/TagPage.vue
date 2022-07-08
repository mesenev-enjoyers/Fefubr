<template>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">
  <main-content-component :selected-tag="tagName" :posts="posts"></main-content-component>
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
      tagName: '',
    }
  },
  methods: {
    async fetchPosts() {
      if (this.isAuthorized)
        axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
      else
        console.log("I'm not authorized!")
      const response = await axios.get('http://fefubr.tk/api/content/article?tag=' + this.$route.params.id)
      this.posts = response.data
    },
    getTagName() {
      axios.get('http://fefubr.tk/api/content/tag/' + this.$route.params.id).then((res) => {
        this.tagName = res.data.name
      })
    }
  },
  mounted() {
    this.fetchPosts()
    this.getTagName()
  },
  watch: {
    $route() {
      this.fetchPosts()
      this.getTagName()
    },
  }
}
</script>

<style scoped>

</style>