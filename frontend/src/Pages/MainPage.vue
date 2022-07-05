<template>
  <nav-bar></nav-bar>
  <div class="content">
    <div class="mainContent">
      <div class="barForSort">
        <div>Теги:</div>
        <div><button>Сортировать по времени</button></div>
        <div><button>Сортировать по рейтингу</button></div>
      </div>
      <div class="posts"><post-list :posts="[]"/>ЧТо-то будет</div>
    </div>
    <div class="sideBar">
      <top-users/></div>
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
.content {
  display: flex;
  max-height: 100%;
}
.barForSort {
  display: flex;
  border: 1px solid black;
  height: 10%;
  justify-content: space-between;
  align-content: center;
}
.mainContent {
  width: 70%;
  border: 1px solid black;
}
.sideBar {
  width: 30%;
  border: 1px solid black;
}
</style>