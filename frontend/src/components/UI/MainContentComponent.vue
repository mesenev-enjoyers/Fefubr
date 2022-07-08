<template>
  <nav-bar></nav-bar>
  <div class="container">
    <div class="row mainDiv ">
      <div class="col-9 div-first-content ">
        <div class="col col-first-content ">
          <div class="row uprow-first-content rounded-1 justify-content-center">
            <div class="row content-uprow">
              <div class="p-tag-div col-3">
                <p class="p-tag">Тэги: Все </p>
              </div>
              <div class="btns-div col-9">
                <button class="btn btn-primary" @click.prevent="timeSort">По времени</button>
                <button class="btn btn-primary" @click.prevent="ratingSort">По рейтингу</button>
              </div>
            </div>
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
import PostItem from "@/Posts/PostItem";
import TopUsers from "@/components/UI/TopUsers";
import NavBar from "@/components/UI/NavBar";

export default {
  name: "MainContentComponent",
  methods: {
  },
  components: {
    PostItem,
    TopUsers,
    NavBar,
  },
  props: {
    posts: {
      type: Object,
      required: true
    }
  }
}

</script>

<style scoped>

.mainDiv {
  margin: 30px 0 0 0;
}

.div-first-content{
  margin:0;
  padding: 0;
}


.uprow-first-content{
  margin: 0;
  padding: 0;
  width: 97%;
  height: 60px;
  box-shadow: -1px -1px 5px rgb(191, 191, 191), 1px 1px 5px rgb(191, 191, 191);
  /*background-color: fuchsia;*/
}

.content-uprow{
  margin: 0;
  padding: 10px 0 0 0 ;
}

.p-tag{
  margin: 0;
  padding: 8px 0 0 0;
  width: auto;
}

.btns-div{
  padding: 0 0 0 30px;
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
  border-width: 2px;
  border-color: #5F77BF;
  background-color: #5F77BF;
  color: white;
  box-shadow: none !important;
}

.downrow-first-content{
  margin: 25px 0 0 0;
  padding: 0;
  width: 97%;
  box-shadow: -1px -1px 5px rgb(191, 191, 191), 1px 1px 5px rgb(191, 191, 191);
  height: auto;
  /*background-color: forestgreen;*/

}

.div-second-content{
  margin: 0;
  padding: 0;
  box-shadow: -1px -1px 5px rgb(191, 191, 191), 1px 1px 5px rgb(191, 191, 191);
  height: 800px;
  position: sticky;
  top: 82px

}


</style>