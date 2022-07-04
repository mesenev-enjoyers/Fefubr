<template>
  <div class="root">
    <form action="" @submit.prevent="createUser">
      <input
          type="text"
          placeholder="Введлите ваше имя"
          v-model="login"
      >      <input
        type="text"
        placeholder="Введлите ваш мейл"
        v-model="mail"
    >
      <input
          type="password"
          placeholder="Введите ваш пароль"
          v-model="password"
      >
      <input
          type="password"
          placeholder="Подвердите ваш пароль"
          v-model="passwordConfirm"
      >
      <button>Зарегистрироваться</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "RegPage",
  data() {
    return {
      login: '',
      mail: '',
      password: '',
      passwordConfirm: '',
    }
  },
  methods: {
    createUser() {
      if (this.password !== this.passwordConfirm) {
        return
      }
      axios.post('http://fefubr.tk/api/auth/users/', {
        email: this.mail,
        username: this.login,
        password: this.password
      }).then(() => {
        axios.post('http://fefubr.tk/api/auth/token/login',{
          username: this.login,
          password: this.password
        }).then((response) => {
          localStorage.setItem('token', response.data.auth_token);
          axios.defaults.headers.common['Authorization'] = `Token ${response.data.auth_token}`
          this.$router.push('/')
          console.log(response)
        })
      }).catch(function () {
        console.log("error"); // FIXME
      })
    },
  }
}
</script>

<style scoped>

</style>