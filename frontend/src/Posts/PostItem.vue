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
      <div class="main-content" >{{post.content}}</div>
      <div class = "tags">
        <h6>Теги:</h6>
        <div v-for = "tag in tags" :key="tag.id">{{tag.name}} </div>
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
<!--    <div v-if="post.is_liked">Лайкнут</div>-->
<!--    <div v-else>Не лайкнут</div>-->
<!--  </div>-->
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
  padding: 10px;
}

img{
  max-width: 760px;
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
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 20px;
  line-height: 24px;
  color: #000000;
  margin-top: 22px;
  margin-bottom: 22px;

}

.main-content{
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 15px;
  line-height: 18px;
}

</style>