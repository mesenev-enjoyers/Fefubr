<template>
  <nav-bar></nav-bar>
  <div class="root">

  </div>
</template>

<script>
import axios from "axios";
import NavBar from "@/components/UI/NavBar";

export default {
  name: "UserPage",
  components: {NavBar},

  data() {
    return {
      user: {},
      isAuthorized: localStorage.getItem('token') != null,
    }
  },
  mounted() {
    axios.get('http://fefubr.tk/api/users/' + this.$route.params.id).then((res) =>{
      this.user = res.data
    })
    if (this.isAuthorized) {
      console.log(this.user.id)
      axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
      axios.get('http://fefubr.tk/api/users/current').then((res) => {
        if (this.user.id === res.data.id) {
          this.$router.push('/profile')
        }
      })
    }
  }
}
</script>

<style scoped>

</style>