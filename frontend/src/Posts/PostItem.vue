<template>
  <div class = "post">
    <div class = "name">{{post.name}}</div>
    <div class = "content">{{post.content}}</div>
    <div class = "date">{{post.date}}</div>
    <div class = "rating">{{post.rating}}</div>
    <div class = "img" v-if="post.picture != null"><img :src="post.img"></div> <!-- FIXME -->
    <div class = "creator">{{post.creator}}</div>
    <div class = "tags">
      <div v-for = "tag in post.tags" :key="tag.id">{{tag.name}}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PostItem",
  props: {
    post: {
      type: Object,
      required: true,
    }
  }
}
</script>

<style scoped>

</style>