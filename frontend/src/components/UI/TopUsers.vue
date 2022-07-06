<template>
  <div class="root">
    <h2>Топ пользователей</h2>
    <div  v-for="user in TopUsers" :key="user.id">
      <div class="user d-inline-flex p-2">
        <img :src="user.avatar">
        <div class="name-rate">
        {{user.username}} {{user.rating}}
        </div>
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
  padding: 15px;
  font-size: 22px;
}
.user img {
  width: 20%;
}
.name-rate{
  margin: 12px 0 0 12px;
}
</style>