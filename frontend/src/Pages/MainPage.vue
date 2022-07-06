<template>
<!--  <nav-bar></nav-bar>-->

<!--    <div class="content">-->
<!--    <div class="mainContent">-->
<!--      <h1 v-if="isPostsLoading" style="text-align: center; margin-top: 20%">Идёт загрузка...</h1>-->
<!--      <div v-else>-->
<!--        <div v-if="posts.length > 0">-->
<!--           <post-list :posts="posts"/>-->
<!--        </div>-->
<!--        <h1 v-else style="text-align: center; margin-top: 20%">Постов нет :(</h1>-->
<!--      </div>-->
<!--    </div>-->
<!--    <div class="sideBar">-->
<!--      <top-users></top-users>-->
<!--    </div>-->
<!--  </div>-->




  <nav-bar></nav-bar>
  <div class="container">
    <div class="row mainDiv ">
      <div class="col-9 div-first-content ">
        <div class="col col-first-content ">
          <div class="row uprow-first-content  rounded-1">
            <p>dddd</p>
          </div>
          <div class="row downrow-first-content  rounded-1"  v-for="post in posts"  :key = "post.id">
            <post-item  :post = "post"/>
          </div>
        </div>
      </div>
      <div class="col-3 div-second-content rounded-1">
              <top-users></top-users>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
// import PostList from "@/Posts/PostList";
import NavBar from "@/components/UI/NavBar";
import TopUsers from "@/components/UI/TopUsers";
import PostItem from "@/Posts/PostItem";
export default {
  components: {
    PostItem,
    TopUsers,
    NavBar,
    // PostList,
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

.mainDiv {
  margin: 30px 0 0 0;
  position: relative;

}
.div-first-content{
  margin:0;
  padding: 0;
  /*border: orangered 1px solid;*/
}


.uprow-first-content{
  margin: 0;
  padding: 0;
  width: 97%;

  box-shadow: -1px -1px 5px rgb(191, 191, 191), 1px 1px 5px rgb(191, 191, 191);
  background-color: fuchsia;
}

.downrow-first-content{
  margin: 25px 0 0 0;
  padding: 0;
  width: 97%;
  box-shadow: -1px -1px 5px rgb(191, 191, 191), 1px 1px 5px rgb(191, 191, 191);
  height: auto;
  background-color: forestgreen;

}

.div-second-content{
  margin: 0;
  padding: 0;
  box-shadow: -1px -1px 5px rgb(191, 191, 191), 1px 1px 5px rgb(191, 191, 191);
  background-color: aqua;
  height: 500px;
  position: sticky;
  top: 82px
}

/*......................*/


/*.content {*/
/*  display: flex;*/
/*}*/
/*.mainContent {*/
/*  width: 70%;*/
/*  text-align: center;*/
/*  border: 1px solid black;*/
/*  box-shadow: -1px -1px 5px gray, 1px 1px 5px gray;*/
/*}*/
/*.sideBar {*/
/*  width: 30%;*/
/*}*/




</style>