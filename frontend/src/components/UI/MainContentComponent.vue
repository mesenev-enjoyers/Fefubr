<template>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.3/font/bootstrap-icons.css">
  <nav-bar></nav-bar>
  <div class="container">
    <div class="row mainDiv ">
      <div class="col-9 div-first-content ">
        <div class="col col-first-content ">
          <div class="row uprow-first-content rounded-1 justify-content-center">
            <div class="row content-uprow">
              <div class="p-tag-div col-3">
                <p class="p-tag">Тэги: {{selectedTag}} </p>
              </div>
              <div class="btn-2-div">
                <button class="btn-2 " >Подписаться</button>
              </div>
              <div class="btns-div col-9">
                <button class="btn " >По времени</button>
                <button class="btn " >По рейтингу</button>
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
  components: {
    PostItem,
    TopUsers,
    NavBar,
  },
  props: {
    posts: {
      type: Object,
      required: true
    },
    selectedTag: {
      type: String,
      required: false,
      default: "Все"
    }
  },
}

</script>

<style scoped>

.btns-div{
  width: auto;
}


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
  height: auto;
  box-shadow: -1px -1px 5px rgb(191, 191, 191), 1px 1px 5px rgb(191, 191, 191);
  /*background-color: fuchsia;*/
}

.content-uprow{
  margin: 0;
  padding: 10px 0 10px 0 ;
}

.p-tag{
  margin: 0;
  padding: 8px 0 0 0;
}

.p-tag-div{
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

.downrow-first-content{
  margin: 25px 0 0 0;
  padding: 0;
  width: 97%;
  box-shadow: -1px -1px 5px rgb(191, 191, 191), 1px 1px 5px rgb(191, 191, 191);
  height: auto;
}

.div-second-content{
  margin: 0;
  padding: 0;
  box-shadow: -1px -1px 5px rgb(191, 191, 191), 1px 1px 5px rgb(191, 191, 191);
  height: 800px;
  position: sticky;
  top: 82px

}

@media (max-width: 1280px){
  .btn-2-div{
    margin-bottom: 10px;
  }
  .btns-div{
    padding: 0 0 0 12px;
  }


}




</style>