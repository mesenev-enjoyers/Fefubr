<template>
  <nav-bar></nav-bar>
  <div class="root">
    <img :src="user.avatar">
    <form @submit="changeAvatar">
      <input type="file" ref="file" @input="handleFileUpload">
      <button>Сменить</button>
    </form>

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
      user: {
      },
      userTags: [],
      userSubscribe: [],
      isAuthorized: localStorage.getItem('token') != null,
      newAvatar: ''
    }
  },
  methods: {
    getUserData() {
      if (this.isAuthorized) {
        axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
      }
      axios.get('http://fefubr.tk/api/users/current').then((res) => {
        this.user = res.data
        this.user.avatar = 'http://fefubr.tk' + this.user.avatar
        axios.get('http://fefubr.tk/api/users/tag?user=' + this.user.id).then((res) => {
          this.userTags = res.data
        })
        axios.get('http://fefubr.tk/api/users/subscribe?user=' + this.user.id).then((res) => {
          this.userSubscribe = res.data
        })
      })
    },
    handleFileUpload() {
      this.file = this.$refs.file.files[0]
    },
    changeAvatar() {
      if (this.isAuthorized) {
        axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
      }
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
    this.getUserData()
  }
}
</script>

<style scoped>

</style>