<template>
 <div class="root">
   <nav-bar></nav-bar>
   <div class="container-fluid d-flex h-100 justify-content-center align-items-center p-0 mt-15" id="pictures">
     <a href="https://t.me/Silly_bot_bot"><h2>Переходите в нашего телеграм бота</h2></a>
   </div>
   <div class="container-fluid d-flex h-100 justify-content-center align-items-center p-0 mt-15" id="pictures">
     <img src="https://i.imgur.com/FYjJbTP.png">
   </div>
 </div>
</template>

<script>
import NavBar from "@/components/UI/NavBar";
export default {
  name: "UserChats",
  components: {NavBar}

}
</script>

<style scoped>
#pictures {
  margin-top: 15px;
}
#pictures img {
  max-height: 30%;
  max-width: 30%;
}
a {
  text-decoration: none;
  color: #5F77BF;
}

a:hover {
  color: black;
}
</style>