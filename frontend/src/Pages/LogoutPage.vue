<template>
  <button @click="logout">Выйти</button>
</template>

<script>
import axios from "axios";

export default {
  name: "LogoutPage",
  data() {
    return {
      token: '',
    }
  },
  methods: {
    logout() {
      this.token = localStorage.getItem('token')
      localStorage.removeItem('token')
      axios.post("http://fefubr.tk/api/auth/logout",{headers: {Authorization: `Token ${this.token}`}})
      this.token = ''
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>

</style>