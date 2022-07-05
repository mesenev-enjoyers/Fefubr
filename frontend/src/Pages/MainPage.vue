<template>
  <nav-bar></nav-bar>
  <post-list :posts="[]"/>
</template>

<script>
import axios from "axios";
import PostList from "@/Posts/PostList";
import NavBar from "@/components/UI/NavBar";
export default {
  components: {
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
      Posts: []
    }
  },

  beforeMount() {
        if (this.isAuthorized) {
          axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
          axios.get('http://fefubr.tk/api/users/current').then((res) =>
              (this.User.name = res.data.username, this.User.rating = res.data.rating))
              .then((err) => (console.log(err)))
        }
      },


}
</script>

<style scoped>

</style>