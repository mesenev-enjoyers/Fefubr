<template>
  <div class="root">
    <form action="" @submit.prevent="authorize">
      <input
          type="text"
          placeholder="Введите логин"
          v-model="login"
      >
      <input
          type="password"
          placeholder="Введите пароль"
          v-model="password"
      >
      <button>Войти</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "LoginPage",
  data() {
    return {
      isAuthorized: localStorage.getItem('token') != null,
      login: '',
      password: '',
      token: '',
    }
  },
  methods: {
    authorize() {
      axios.post('http://fefubr.tk/api/auth/token/login',{
        username: this.login,
        password: this.password
      }).then((response) => {
        localStorage.setItem('token', response.data.auth_token);
        axios.defaults.headers.common['Authorization'] = `Token ${response.data.auth_token}`
        this.$router.push('/')
      }).catch(function () {
        console.log("error"); // FIXME
      })
    },

  }
}
</script>

<style scoped>

</style>