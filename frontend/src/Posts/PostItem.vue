<template>
  <div class = "post">
    <div class = "name">{{post.name}}</div>
    <div class = "content">{{post.content}}</div>
    <div class = "date">{{post.date.substring(0,10)}}</div>
    <div class = "rating">{{post.rating}}</div>
    <div class = "img" v-if="post.picture != null"><img :src="post.img"></div> <!-- FIXME -->
    <div class = "creator">{{this.creatorName}}</div>
    <div class = "tags">
      <h6>Теги:</h6>
      <div v-for = "tag in tags" :key="tag.id">{{tag.name}}</div>
    </div>
    <div v-if="post.is_liked">Лайкнут</div>
    <div v-else>Не лайкнут</div>
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
    }
  },
  data() {
    return {
      tags: [],
      creatorName: '',
      date : this.post.date
    }
  },

  mounted() {
    axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
    axios.get(`http://fefubr.tk/api/users/${this.post.creator}`).then((res) => {this.creatorName = res.data.username})
    for(let i = 0; i < this.post.tags.length; ++i)
    axios.get(`http://fefubr.tk/api/content/tag/${this.post.tags[i]}`).then((res) =>{
    this.tags.push({id: this.post.tags[i], name: res.data.name})
  })
  }
}

</script>

<style scoped>
* {
  background: white;
}
</style>