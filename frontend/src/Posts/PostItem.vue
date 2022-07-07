<template>
  <div class="container">

    <div class="creator d-inline-flex">
      <img :src="creatorAvatar" @click="$router.push('/user/' + post.creator)" alt="">
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
      <div class = " tags d-inline-flex">
        <a class="tagg " @click="$router.push('/tag/' + tag.id); " v-for = "tag in tags" :key="tag.id">{{tag.name}}⠀</a>
      </div>
      <div class="button-div">
        <button class="btn btn-primary" @click="$router.push('/post/' + post.id)">Читать далее</button>
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
<!--  <div class = "post">-->
<!--    <div class = "name">{{post.name}}</div>-->
<!--    <div class = "content">{{post.content}}</div>-->
<!--    <div class = "date">{{post.date.substring(0,10)}}</div>-->
<!--    <div class = "rating">{{post.rating}}</div>-->
<!--    <div class = "img" v-if="post.picture != null"><img :src="post.img"></div> &lt;!&ndash; FIXME &ndash;&gt;-->
<!--    <div class = "creator">{{this.creatorName}}</div>-->
<!--    <div class = "tags">-->
<!--      <h6>Теги:</h6>-->
<!--      <div v-for = "tag in tags" :key="tag.id">{{tag.name}}</div>-->
<!--    </div>-->

</template>

<script>
import axios from "axios";

export default {
  name: "PostItem",
  props: {
    post: {
      type: Object,
      required: true
    }
  },
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

</style>