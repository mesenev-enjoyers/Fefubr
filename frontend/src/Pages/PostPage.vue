<template>
 <div class="root">
   <h1>Страница с постами</h1>
   <h1>{{ $store.state.likes }}</h1>
   <div>
     <button @click="$store.commit('incrementLikes')">Like</button>
     <button @click="$store.commit('decrementLikes')">Dislike</button>
   </div>
 </div>
</template>

<script>
export default {
  name: "PostPage"
}
</script>

<style scoped>

</style>