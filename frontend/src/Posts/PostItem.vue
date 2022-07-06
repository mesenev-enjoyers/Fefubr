<template>
  <div class="container">
    <div class="creator">
      <img :src="creatorAvatar" alt=""> {{creatorName}} {{post.date.substring(0,10)}}
    </div>
    <div class="content">
      <div class="title">{{post.name}}</div>
      <div class = "img" v-if="post.picture != null"><img :src="post.picture"></div>
      <div class="mainContent" >{{post.content}}</div>
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

img{
  max-width: 760px;
  max-height: 700px;
}
.container {
  margin-top: 15px;
  padding: 10px;
}
.creator {
  display: flex;
}
.creator img {
  max-height: 25px;
  max-width: 25px;
}
.tags {
  display: flex;
}
</style>