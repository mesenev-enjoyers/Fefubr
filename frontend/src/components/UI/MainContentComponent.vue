<template>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.3/font/bootstrap-icons.css">
  <nav-bar></nav-bar>
  <div class="container container-sun">
    <div class="row mainDiv ">
      <div class="col-9 div-first-content ">
        <div class="col col-first-content ">
          <div class="row uprow-first-content rounded-1 justify-content-center">
            <div class="row content-uprow">
              <div class="p-tag-div col-3">
                <p class="p-tag">Тэг: {{selectedTag}} </p>
              </div>
              <slot></slot>
              <p class="p-tags-menu">Навигация по тэгам:</p>
                <div class="name-rate subs-elements-div row row-cols-3">
                  <a class="sub-element" v-for="tag in allTags" :key="tag.id" @click="$router.push('/tag/' + tag.id)">{{tag.name}}</a>
                </div>
            </div>
          </div>

          <div class="row downrow-first-content  rounded-1"  v-for="post in posts"  :key = "post.id">
            <post-item  :post = "post"/>
          </div>
        </div>
      </div>
      <div class="top-users-div col-3 div-second-content rounded-1">
        <top-users></top-users>
      </div>
    </div>
  </div>
</template>

<script>
import PostItem from "@/Posts/PostItem";
import TopUsers from "@/components/UI/TopUsers";
import NavBar from "@/components/UI/NavBar";
import axios from "axios";

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
    },
  },
  data() {
    return {
      allTags: [],
    }
  },
  methods: {
    getAllTags() {
      axios.get('http://fefubr.tk/api/content/tag').then((res) => {
        this.allTags = res.data
      }).catch((error) => {
        console.log(error)
      })
    }
  },
  mounted() {
    this.getAllTags()
  }
}

</script>

<style scoped>

.sub-element{
  cursor: pointer;
  text-decoration: none;
  color: #5F77BF;
  width: auto;
}

.sub-element:hover{
  color: black;
}

.container-sun{
  margin-bottom: 50px;
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
}

.content-uprow{
  margin: 0;
  padding: 10px 0 10px 0 ;
}

.p-tag{
  margin: 0;
}

.p-tag-div{
  width: auto;
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
  height: 550px;
  position: sticky;
  top: 82px
}

.p-tags-menu{
  margin-bottom: 0;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 20px;
  line-height: 48px;
  color: #000000;
}

@media (max-width: 1100px){
  .top-users-div{
    display: none;
  }
  .div-first-content{
    width: 100%;
  }
  .uprow-first-content{
    width: 100%;
  }
  .downrow-first-content{
    width: 100%;
  }
  post-item img{
    width: 10px;
    height: 10px;
  }

}

</style>