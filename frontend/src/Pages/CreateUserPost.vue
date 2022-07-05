<template>
 <div class="root">
   <form @submit.prevent="createPost">
     <div class="form-group">
       <label for="name">Название</label>
       <input v-model="name" type="text" class="form-control" id="name" aria-describedby="emailHelp" placeholder="Enter title">
     </div>
     <div class="form-group">
       <label for="content">Содержание статьи</label>
       <textarea v-model="content" class="form-control" id="content" placeholder="Enter some-thing"></textarea>
     </div>
     <p>Выберете теги, соответствующие вашей статье</p>
     <div v-for="tag in userTags" :key="tag.id">
       <div class="form-check form-check-inline">
         <input v-model="tags" class="form-check-input" type="checkbox" id="inlineCheckbox1" :value="tag.id">
         <label class="form-check-label" for="inlineCheckbox1">{{tag.name}}</label>
       </div>
     </div>
     <p>Выберете картинку, при необходимости</p>
     <div class="custom-file">
       <input @input="handleFileUpload" ref="file" type="file" class="custom-file-input" id="customFile">
       <label class="custom-file-label" for="customFile">Вставьте картинку </label>
     </div>
     <button>Опубликовать</button>
   </form>
 </div>
</template>

<script>
import axios from "axios";
export default {
  name: "CreateUserPost",
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
      console.log(this.tags)
      const formData = new FormData();
      formData.append('creator', this.currentUser);
      formData.append('name', this.name);
      formData.append('content', this.content);
      formData.append('tags', this.tags);
      formData.append('picture', this.file);
      axios.post('http://fefubr.tk/api/content/article', formData, {
         headers: {
           'Content-Type': 'multipart/form-data'
         }
      }).then(() => {
        this.$router.push('/')
      }).catch(function () {
        console.log("error"); // FIXME
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
    }
  },
  mounted() {
    axios.defaults.headers.common['Authorization'] = `Token ${localStorage.getItem('token')}`
    axios.get('http://fefubr.tk/api/content/tag').then((res) => {
      this.userTags = res.data
    })
    this.getCurrentUser()

  }
}
</script>

<style scoped>

</style>