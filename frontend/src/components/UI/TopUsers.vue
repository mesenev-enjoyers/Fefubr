<template>
  <div class="root">
    <div><h2>Топ пользователей</h2></div>
      <div  v-for="user in TopUsers" :key="user.id">
        <div class="user d-inline-flex p-2">
          <img class="avavav" :src="user.avatar" @click="$router.push('/user/' + user.id)">
          <div class="name-rate d-inline-flex ">
            <div class="name">{{user.username}} </div>
            <div class="rate"> {{user.rating}}</div>
          </div>
        </div>
      </div>
    <div><h2>Все доступные Тэги: </h2></div>
    <div v-for="tag in allTags" :key="tag.id">
      <div class="name-rate d-inline-flex">
        <a @click="$router.push('/tag/' + tag.id)">{{tag.name}}</a>
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
      allTags: []
    }
  },
  methods: {
    getTopUsers() {
      axios.get('http://fefubr.tk/api/users/?top=5').then((res) =>{
        this.TopUsers = res.data
      })
    },
    getAllTags() {
      axios.get('http://fefubr.tk/api/content/tag').then((res) => {
        this.allTags = res.data
      }).catch((error) => {
        console.log(error)
      })
    }
  },
  mounted() {
    this.getTopUsers()
    this.getAllTags()
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

.avavav{
  cursor: pointer;
}
</style>