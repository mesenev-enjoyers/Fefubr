<template>
  <nav-bar></nav-bar>
 <div class="container">
   <div class="header-create ">
     <h1 class="text-center">Создание статьи</h1>
   </div>
   <form @submit.prevent="createPost">
     <div class="form-group">
       <label for="name">Название</label>
       <input v-model="name" type="text" class="form-control title" id="name" aria-describedby="emailHelp" placeholder="Enter title">
     </div>
     <div class="form-group">
       <label for="content">Содержание статьи</label>
       <textarea v-model="content" class="form-control main-content" id="content" placeholder="Enter some-thing"></textarea>
     </div>
     <p>Выберете теги, соответствующие вашей статье</p>
     <div v-for="tag in userTags" :key="tag.id">
       <div class="form-check form-check-inline">
         <input v-model="tags" class="form-check-input checkbox" type="checkbox" id="inlineCheckbox1" :value="tag.id">
         <label class="form-check-label checkbox-name" for="inlineCheckbox1">{{tag.name}}</label>
       </div>
     </div>
     <p class="p-choose-img">Выберете картинку, при необходимости</p>
     <div class="custom-file">
       <input @input="handleFileUpload" ref="file" type="file" class="custom-file-input btn-choose-img" id="customFile">
     </div>
     <button class="btn">Опубликовать</button>
   </form>
 </div>
</template>

<script>
import axios from "axios";
import NavBar from "@/components/UI/NavBar";
export default {
  name: "CreateUserPost",
  components: {NavBar},
  data() {
    return {
      name: '',
      content: '',
      userTags: [],
      tags: [],
      tagsId: [],
      currentUser: {
      },
      file: '',
    }
  },
  methods: {
    createPost() {
      const formData = new FormData();
      formData.append('creator', this.currentUser);
      formData.append('name', this.name);
      formData.append('content', this.content);
      for (let i = 0; i < this.tags.length; ++i) {
        formData.append('tags', this.tags[i])
      }
      formData.append('picture', this.file);
      axios.post('http://fefubr.tk/api/content/article', formData, {
         headers: {
           'Content-Type': 'multipart/form-data'
         }
      }).then(() => {
        this.$router.push('/')
      }).catch(() => {
        if (this.tags.length < 1) {
          alert("Выберете хотя бы один тег")
        }
        else {
          alert("Вы выбрали слишком большой файл, пожалуйста пощадите наш сервер((") //FIXME спросить Месенева
        }
      })
    },
    handleFileUpload() {
      this.file = this.$refs.file.files[0]
    },
    getCurrentUser() {
      axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
      axios.get('http://fefubr.tk/api/users/current').then((res) =>{
        this.currentUser = res.data.id
      })
    },
  },
  mounted() {
    const isAuthorized = localStorage.getItem('token') != null;
    if (isAuthorized)
    axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`

    axios.get('http://fefubr.tk/api/content/tag').then((res) => {
      this.userTags = res.data
    })
    this.getCurrentUser()

  }
}
</script>

<style scoped>

p{
  margin-bottom: 10px;
}

.container{
  margin-top: 40px;
  margin-bottom: 40px;
  padding: 20px;
  box-shadow: -1px -1px 5px rgb(191, 191, 191), 1px 1px 5px rgb(191, 191, 191);
}

label{
  margin-bottom: 5px;
}

.title{
  margin-bottom: 20px;
  border-color: #5F77BF;
}

.main-content{
  margin-bottom: 10px;
  height: 300px;
  border-color: #5F77BF;
}

.checkbox{
  border-color: #5F77BF;
}

.checkbox-name{
  margin: 0;
  pointer-events: none;
  cursor: default;
}

.p-choose-img{
  margin-top: 10px;
  margin-bottom: 10px;
}

.btn-choose-img{
  color: black;
  width: auto;
  margin-bottom: 20px;
}

.btn{
  width: 150px;
  height: 40px;
  padding: 2px 5px 5px 5px;
  margin-right: 20px;
  color: black;
  background-color:white;
  border-width: 2px;
  border-color: #5F77BF;
}

.btn:hover{
  width: 150px;
  height: 40px;
  color: white;
  background-color: #5F77BF;
  border-color: #5F77BF;
}

.btn:active {
  width: 150px;
  height: 40px;
  color: black;
  background-color:white;
  border-width: 2px;
  border-color: #5F77BF;
}

</style>