<template>
  <div class="root">
    <h2>Топ пользователей</h2>
    <div  v-for="user in TopUsers" :key="user.id">
      <div class="user d-inline-flex p-2">
        <img :src="user.avatar" @click="$router.push('/user/' + user.id)">
        <div class="name-rate d-inline-flex ">
          <div class="name">{{user.username}} </div>
          <div class="rate"> {{user.rating}}</div>
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

.name{
  margin-right: 10px;
}

.rate{
  color: green;
}

.root {
  padding: 10px;
  margin-top: 15px;
  text-align: center;
}
h2{
  font-family: 'Inter';

}
.user {
  padding: 15px;
  margin: 12px 0 0 12px;
  font-family: 'Inter';
  font-style: normal;
  font-weight: bold;
  font-size: 20px;
}
.user img {
  width: 20%;
}
.name-rate{
  margin: 12px 0 0 12px;
}
</style>