<template>
  <nav-bar></nav-bar>
 <div class="app">
   <router-view></router-view>
 </div>
</template>

<script>


import NavBar from "@/components/UI/NavBar";
export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>

<style>
*{
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
</style>
