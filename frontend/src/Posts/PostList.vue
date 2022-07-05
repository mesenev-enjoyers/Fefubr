<template>
  <div class="post" v-for="post in posts" :key="post.id">
  {{post.name}}
  </div>
</template>

<script>
export default {
  name: "PostList",
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