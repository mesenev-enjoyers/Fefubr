<template>
  <div class="container">

    <div class="creator d-inline-flex">
      <img class="avavav" :src="creatorAvatar" @click="$router.push('/user/' + post.creator)" alt="">
      <div class="creator-name">
        {{creatorName}}
      </div>
      <div class="creator-date">
        {{post.date.substring(0,10)}}
      </div>
    </div>
    <div class="content">
      <div class="title">{{post.name}}</div>
      <div class = "img" v-if="post.picture != null"><img :src="post.picture"></div>
      <div class="main-content" >{{truncate(post.content, 400)}}</div>
      <div class = " tags d-inline-flex" >
        <a class="tagg " @click="$router.push('/tag/' + tag.id); " v-for = "tag in tags" :key="tag.id">{{tag.name}}⠀</a>
      </div>
      <div class="button-div">
        <button class="btn btn-primary" @click="$router.push('/post/' + post.id)">Читать далее</button>
      </div>
          <button class="button-liked" v-if="post.is_liked" @click="removeLike">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-lightning-charge svg-liked" viewBox="0 0 16 16">
              <path d="M11.251.068a.5.5 0 0 1 .227.58L9.677 6.5H13a.5.5 0 0 1 .364.843l-8 8.5a.5.5 0 0 1-.842-.49L6.323 9.5H3a.5.5 0 0 1-.364-.843l8-8.5a.5.5 0 0 1 .615-.09zM4.157 8.5H7a.5.5 0 0 1 .478.647L6.11 13.59l5.732-6.09H9a.5.5 0 0 1-.478-.647L9.89 2.41 4.157 8.5z"/>
            </svg>
            {{post.rating}}
          </button>
          <button class="button-unliked" v-else @click="makeLike">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-lightning-charge svg-not-liked" viewBox="0 0 16 16">
              <path d="M11.251.068a.5.5 0 0 1 .227.58L9.677 6.5H13a.5.5 0 0 1 .364.843l-8 8.5a.5.5 0 0 1-.842-.49L6.323 9.5H3a.5.5 0 0 1-.364-.843l8-8.5a.5.5 0 0 1 .615-.09zM4.157 8.5H7a.5.5 0 0 1 .478.647L6.11 13.59l5.732-6.09H9a.5.5 0 0 1-.478-.647L9.89 2.41 4.157 8.5z"/>
            </svg>
            {{post.rating}}
          </button>
    </div>
  </div>

</template>

<script>
import axios from "axios";

export default {
  name: "PostItem",
  props: {
    post: {
      type: Object,
      required: true
    },

  },
  emits: ['addLike', 'removeLike'],
  data() {
    return {
      tags: [],
      creatorName: '',
      creatorAvatar: '',
      date : this.post.date,
      isAuthorized: localStorage.getItem('token') != null,
    }
  },
  methods: {
    truncate(value, length) {
      if (value.length > length) {
        return value.substring(0, length) + "...";
      } else {
        return value;
      }
    },
    makeLike() {
      if(!this.isAuthorized)
        return;

      axios.get('http://fefubr.tk/api/content/article/' + this.post.id + '?like=true').then((res) =>{
        // eslint-disable-next-line vue/no-mutating-props
        this.post.is_liked = true
        // eslint-disable-next-line vue/no-mutating-props
        this.post.rating++
        console.log(res.data.id)
      })
    },
    removeLike() {
      axios.get('http://fefubr.tk/api/content/article/' + this.post.id + '?unlike=true').then((res) =>{
        // eslint-disable-next-line vue/no-mutating-props
        this.post.is_liked = false
        // eslint-disable-next-line vue/no-mutating-props
        this.post.rating--
        console.log(res.data.id)
    })

  }
},

    mounted() {

    if (this.isAuthorized)
      axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
    axios.get(`http://fefubr.tk/api/users/${this.post.creator}`).then((res) => {this.creatorName = res.data.username,
    this.creatorAvatar = res.data.avatar})
    for(let i = 0; i < this.post.tags.length; ++i)
      axios.get(`http://fefubr.tk/api/content/tag/${this.post.tags[i]}`).then((res) =>{
    this.tags.push({id: this.post.tags[i], name: res.data.name})

  })
  }
}

</script>

<style scoped>

.container {
  padding: 20px;
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

img{
  max-width: 650px;
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
  /*line-height: 25px;*/
}

.tagg{
  margin-bottom: 22px;
}

a{
  cursor: pointer;
  text-decoration: none;
  color: #5F77BF;
}

.button-div{
  margin-bottom: 22px;
}

.btn{
  width: 150px;
  height: 40px;
  padding: 3px 5px 5px 5px;
  margin-right: 20px;
  color: black;
  background-color:white;
  border-width: 2px;
  border-color: #5F77BF;
}

.btn:hover{
  width: 150px;
  height: 40px;
  color: white;
  background-color: #5F77BF;
  border-color: #5F77BF;
}

.btn:active {
  width: 150px;
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

.avavav{
  cursor: pointer;
}



</style>