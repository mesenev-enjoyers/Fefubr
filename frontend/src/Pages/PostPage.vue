<template>
  <nav-bar></nav-bar>
  <div class="container">

    <div class="creator d-inline-flex">
      <img :src="postCreator.avatar" @click="$router.push('/user/' + postCreator.id)" alt="">
      <div class="creator-name">
        {{postCreator.name}}
      </div>
      <div class="creator-date">
        {{post.date}}
      </div>
    </div>
    <div class="content">
      <div class="title">{{post.name}}</div>
      <div class = "img" v-if="post.picture != null"><img :src="post.picture"></div>
      <div class="main-content" >{{post.content}}</div>
      <div class = " tags d-inline-flex">
        <a class="tagg " href="#" v-for = "tag in tags" :key="tag.id">{{tag.name}}⠀</a>
      </div>
      <!--      <div v-if="post.is_liked">Лайкнут{{post.rating}}</div>-->
      <div>
        <svg id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="33px" height="33px" viewBox="0 0 64 64" enable-background="new 0 0 64 64" xml:space="preserve">
              <g>
              <path d="M29.695,38l-6.661,24.74l1.776,0.845l26-36L50,26H37.166l3.823-24.848l-1.831-0.69l-23,36L17,38H29.695z M38.291,5.532 l-3.279,21.316L36,28h12.044l-21.66,29.991l5.582-20.731L31,36H18.826L38.291,5.532z"/>
              </g>
            </svg>
        {{post.rating}}
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import NavBar from "@/components/UI/NavBar";
export default {
  name: "PostPage",
  components: {NavBar},
  data() {
    return {
      post: {},
      postCreator: {},
      tags: []
    }
  },
  methods: {
    getCurrentPost() {
      axios.get('http://fefubr.tk/api/content/article/' + this.$route.params.id).then((res) => {
        this.post = res.data
        this.post.date=this.post.date.substring(0,10)
        this.getPostCreator()
        this.getPostTags()
      }).catch(() => {
        console.log("We got some problems")
      })
    },
    getPostCreator() {
      axios.get('http://fefubr.tk/api/users/' + this.post.creator).then((res) => {
        this.postCreator = res.data
        console.log(this.postCreator)
      })
    },
    getPostTags() {
      for(let i = 0; i < this.post.tags.length; ++i) {
        axios.get(`http://fefubr.tk/api/content/tag/${this.post.tags[i]}`).then((res) => {
          this.tags.push({id: this.post.tags[i], name: res.data.name})
        })
      }
    }
  },
  mounted() {
    this.getCurrentPost()
  }
}
</script>

<style scoped>
.container {
  padding: 20px;
}

img{
  max-width: 900px;
  max-height: 700px;
  margin-bottom: 22px;
}
.creator img {
  max-height: 35px;
  max-width: 35px;
  margin-right: 10px;
}
.creator-name{
  margin-top: 5px;
  margin-right: 10px;
  font-family: 'Inter';
  font-style: normal;
  font-weight: bold;
  font-size: 15px;
}

.creator-date{
  margin-top: 5px;
  font-family: 'Inter';
  font-style: normal;
  font-weight: normal;
  font-size: 15px;
  color: #767676;
}

.title{
  max-width: 900px;

  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 20px;
  line-height: 24px;
  color: #000000;
  margin-bottom: 22px;

}

.main-content{
  max-width: 900px;
  margin-bottom: 22px;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  /*line-height: 18px;*/
}

.tagg{
  margin-bottom: 22px;
}

a{
  cursor: pointer;
  text-decoration: none;
  color: #5F77BF;
}
</style>