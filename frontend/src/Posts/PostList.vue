<template>
  <post-item
      v-for="post in posts"
      :post = "post"
      :key = "post.id"
  />
</template>

<script>
import PostItem from "@/Posts/PostItem";
export default {
  name: "PostList",
  components: {PostItem},
  props: {
    posts: {
      type: Array,
      required: true,
    }
  }
}
</script>

<style scoped>

</style>