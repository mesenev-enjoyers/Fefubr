<template>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">

  <nav-bar></nav-bar>
  <div class="container mdc">
    <div class="creator d-inline-flex">
      <img :src="postCreator.avatar" @click="$router.push('/user/' + postCreator.id)" alt="">
      <div class="creator-name">
        {{postCreator.username}}
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
        <a class="tagg "  v-for = "tag in tags" :key="tag.id" @click="$router.push('/tag/' + tag.id)" >{{tag.name}}</a>
      </div>
      <div>
        <button class="button-liked" v-if="post.is_liked" @click="removeLike">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-lightning-charge svg-liked" viewBox="0 0 16 16">
            <path d="M11.251.068a.5.5 0 0 1 .227.58L9.677 6.5H13a.5.5 0 0 1 .364.843l-8 8.5a.5.5 0 0 1-.842-.49L6.323 9.5H3a.5.5 0 0 1-.364-.843l8-8.5a.5.5 0 0 1 .615-.09zM4.157 8.5H7a.5.5 0 0 1 .478.647L6.11 13.59l5.732-6.09H9a.5.5 0 0 1-.478-.647L9.89 2.41 4.157 8.5z"/>
          </svg>
          {{post.rating}}
        </button>
        <button class="button-unliked" v-else @click="addLike">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-lightning-charge svg-not-liked" viewBox="0 0 16 16">
            <path d="M11.251.068a.5.5 0 0 1 .227.58L9.677 6.5H13a.5.5 0 0 1 .364.843l-8 8.5a.5.5 0 0 1-.842-.49L6.323 9.5H3a.5.5 0 0 1-.364-.843l8-8.5a.5.5 0 0 1 .615-.09zM4.157 8.5H7a.5.5 0 0 1 .478.647L6.11 13.59l5.732-6.09H9a.5.5 0 0 1-.478-.647L9.89 2.41 4.157 8.5z"/>
          </svg>
          {{post.rating}}
        </button>
      </div>
    </div>
    <div class="container" style="margin-top: 15px"><p class="p-com">Комментарии:</p>
      <div class="comments" v-for="comment in comments" :key="comment.id">
        <div class="avaCommentCreator">
          <img :src="getCommentCreatorAvatar(comment)"> <strong>{{comment.creator_name}}</strong> {{getNormalDate(comment)}}
        </div>
        <div>{{comment.content}}</div>
      </div>
      <form v-if="isAuthorized" @submit.prevent="makeComment">
        <div class="form-group">
          <label for="content">Оставить комментарий</label>
          <textarea v-model="commentContent" class="form-control main-content" id="content"></textarea>
        </div>
        <button class="btn">Опубликовать</button>
      </form>
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
      tags: [],
      comments: [],
      commentContent: '',
      isAuthorized: localStorage.getItem('token') != null,
      currentUserId: ''
    }
  },
  methods: {
    getCurrentPost() {
      axios.get('http://fefubr.tk/api/content/article/' + this.$route.params.id).then((res) => {
        this.post = res.data
        this.post.date=this.post.date.substring(0,10)
        this.getPostCreator()
        this.getPostTags()
        this.getPostCom()
      }).catch(() => {
        console.log("We got some problems")
      })
    },
    getPostCreator() {
      axios.get('http://fefubr.tk/api/users/' + this.post.creator).then((res) => {
        this.postCreator = res.data
      })
    },
    getPostTags() {
      for(let i = 0; i < this.post.tags.length; ++i) {
        axios.get(`http://fefubr.tk/api/content/tag/${this.post.tags[i]}`).then((res) => {
          this.tags.push({id: this.post.tags[i], name: res.data.name})
        })
      }
    },
    getPostCom() {
      axios.get('http://fefubr.tk/api/content/comment?article=' + this.post.id).then((res) => {
        this.comments = res.data
      })
    },
    getCommentCreatorAvatar(comment) {
      return ('http://fefubr.tk/api/media/' + comment.creator_avatar)
    },
    getNormalDate(comment) {
      return (comment.date.substring(0,10) + ' в ' + comment.date.substring(11,16))
    },
    makeComment() {
      axios.post('http://fefubr.tk/api/content/comment', {
        creator: this.currentUserId,
        article: this.post.id,
        content: this.commentContent
      }).then(() => {
        this.$router.go(0)
      })
    },
    addLike() {
      if(!this.isAuthorized)
        return;

      axios.get('http://fefubr.tk/api/content/article/' + this.post.id + '?like=true').then(() =>{
        // eslint-disable-next-line vue/no-mutating-props
        this.post.is_liked = true
        // eslint-disable-next-line vue/no-mutating-props
        this.post.rating++
      })
    },
    removeLike() {
      axios.get('http://fefubr.tk/api/content/article/' + this.post.id + '?unlike=true').then(() =>{
        // eslint-disable-next-line vue/no-mutating-props
        this.post.is_liked = false
        // eslint-disable-next-line vue/no-mutating-props
        this.post.rating--
      })
    }
  },
  mounted() {
    if (this.isAuthorized)
      axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
    axios.get('http://fefubr.tk/api/users/current').then((res) => {
      this.currentUserId = res.data.id
    }).catch('Id isn`t here')
    this.getCurrentPost()
  }
}
</script>

<style scoped>

.mdc{
  margin-top: 40px;
  margin-bottom: 40px;
  box-shadow: -1px -1px 5px rgb(191, 191, 191), 1px 1px 5px rgb(191, 191, 191);
}

.button-liked{
  outline: none; /* Для синий ободки */
  border: 0;
  background: transparent;
}

.button-liked svg:hover{
  color: black;

}

.button-unliked{
  outline: none; /* Для синий ободки */
  border: 0;
  background: transparent;
}

.button-unliked svg:hover{
  color: #5F77BF;
}

svg{
  width: 30px;
  height: 30px;
}

.svg-liked{
  color: #5F77BF;
}

.svg-not-liked{
  color: black;
}

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

.avaCommentCreator{
  margin-bottom: 10px;
}

.avaCommentCreator img{
  max-height: 30px;
  height: 30px;
  margin-bottom: auto;
}
.comments {
  margin-top: 15px;
  padding: 10px 10px 10px 0;
}
.form-group {
  margin-top: 10px;
}
.btn{
  width: 150px;
  height: 54px;
  color: black;
  background-color:white;
  border-width: 2px;
  border-color: #5F77BF;
}

.btn:hover{
  width: 150px;
  height: 54px;
  color: white;
  background-color: #5F77BF;
  border-color: #5F77BF;
}

.btn:active {
  width: 150px;
  height: 54px;
  color: black;
  background-color:white;
  border-width: 2px;
  border-color: #5F77BF;
}

.btn:focus {
  /*border-width: 2px;*/
  /*border-color: #5F77BF;*/
  /*background-color: #5F77BF;*/
  /*color: white;*/
  box-shadow: none !important;
}

.p-com{
  margin-top: 5px;
  margin-right: 10px;
  font-family: 'Inter';
  font-style: normal;
  font-weight: bold;
  font-size: 30px;
}
</style>