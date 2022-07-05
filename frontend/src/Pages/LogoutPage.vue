<template>
  <button @click="logout">Выйти</button>
</template>

<script>
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


    }
  }
}
</script>

<style scoped>

</style>