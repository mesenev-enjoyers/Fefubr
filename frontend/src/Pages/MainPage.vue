<template>
 <div class="root" v-if="isAuthorized">Hello, {{User.name}}</div>
  <div v-else>Not Logined :(</div>

</template>

<script>
import axios from "axios";

export default {
  name: "MainPage",
  data() {
    return {
      isAuthorized: localStorage.getItem('token') != null,
      User: {
        name: '',
        rating: '',
      }
    }
  },

  beforeMount() {
        if (this.isAuthorized) {
          axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
          axios.get('http://fefubr.tk/api/users/current').then((res) =>
              (this.User.name = res.data.username, this.User.rating = res.data.rating))
              .then((err) => (console.log(err)))
        }
      },


}




</script>

<style scoped>

</style>