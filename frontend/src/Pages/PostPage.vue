<template>
  <nav-bar></nav-bar>
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
import NavBar from "@/components/UI/NavBar";
export default {
  name: "PostPage",
  components: {NavBar}
}
</script>

<style scoped>

</style>