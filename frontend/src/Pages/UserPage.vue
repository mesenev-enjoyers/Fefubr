<template>
  <nav-bar></nav-bar>
  <div class="root">
    <img :src="user.avatar">
    <div v-if="isAuthorized && isCurrentUser">
      <form @submit="changeAvatar">
        <input type="file" ref="file" @input="handleFileUpload">
        <button>Сменить</button>
      </form>
  </div>
    <div v-else-if="isAuthorized">АВторизован, но не мой акк</div>
    <div v-else>не авторизован</div>
  </div>
</template>

<script>
import axios from "axios";
import NavBar from "@/components/UI/NavBar";
export default {
  name: "ProfilePage",
  components: {NavBar},
  data() {
    return {
      user: {},
      userTags: [],
      userSubscribe: [],
      isAuthorized: localStorage.getItem('token') != null,
      isCurrentUser: false,
      file: ''
    }
  },
  methods: {
    CheckUser() {
      if (this.isAuthorized) {
        axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
        axios.get('http://fefubr.tk/api/users/current').then((res) => {
          this.isCurrentUser = (res.data.id == this.$route.params.id)
        })
      }
    },
    getUserData() {
      axios.get('http://fefubr.tk/api/users/' + this.$route.params.id).then((res) => {
        this.user = res.data
        this.file = this.user.avatar
      })
    },
    handleFileUpload() {
      this.file = this.$refs.file.files[0]
    },
    changeAvatar() {
      const formData = new FormData()
      formData.append('avatar', this.file)
      axios.patch('http://fefubr.tk/api/users/' + this.user.id, formData, {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded'}
      }).then(() => {
        this.$router.go(0)
      }).catch((error) => {
        console.log(error)
      })
    },
  },
  mounted() {
    this.CheckUser()
    this.getUserData()
  }
}
</script>

<style scoped>

</style>