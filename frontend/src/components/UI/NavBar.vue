<template>
  <div class="navbar">
    <div>Fefubr</div>
    <div class="navbar__btns">
      <button  @click="$router.push('/')" >Все статьи</button>
      <button @click="$router.push('/mynews')" >Моя лента</button>
      <button @click="$router.push('/chats')" >Общение</button>
      <button @click="$router.push('/createpost')" >Создать статью</button>
      <button @click="$router.push('/login')" >Вход</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  methods: {
  }
}
</script>

<style scoped>
.navbar {
  height: 50px;
  background-color: teal;
  box-shadow: 2px 2px 4px gray;
  display: flex;
  align-items: center;
  padding: 0 15px;
}
</style>