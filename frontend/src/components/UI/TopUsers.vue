<template>
  <div class="root">
    <h2>Топ пользователей</h2>
    <div  v-for="user in TopUsers" :key="user.id">
      <div class="user">
        <img :src="user.avatar"> {{user.username}} {{user.rating}}
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: "TopUsers",
  data() {
    return {
      TopUsers: [],
    }
  },
  mounted() {
    axios.get('http://fefubr.tk/api/users/?top=5').then((res) =>{
      this.TopUsers = res.data
    })
  }
}
</script>

<style scoped>
.root {
  padding: 10px;
  margin-top: 15px;
  text-align: center;
}
.user {
  display: block;
  padding: 15px;
  font-size: 22px;
  margin: auto;
}
.user img {
  width: 10%;

}
</style>