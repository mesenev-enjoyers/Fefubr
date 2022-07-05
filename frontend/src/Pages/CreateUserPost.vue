<template>
 <div class="root">
   <form>
     <div class="form-group">
       <label for="name">Название</label>
       <input type="text" class="form-control" id="name" aria-describedby="emailHelp" placeholder="Enter title">
     </div>
     <div class="form-group">
       <label for="content">Содержание статьи</label>
       <textarea class="form-control" id="content" placeholder="Enter some-thing"></textarea>
     </div>
     <p>Выберете теги, соответствующие вашей статье</p>
     <div v-for="tag in userTags" :key="tag.id">
       <div class="form-check form-check-inline">
         <input @click.stop="addTag(tag)" class="form-check-input" type="checkbox" id="inlineCheckbox1" value="option1">
         <label class="form-check-label" for="inlineCheckbox1">{{tag.name}}</label>
       </div>
     </div>
     <p>Выберете картинку, при необходимости</p>
     <div class="custom-file">
       <input type="file" class="custom-file-input" id="customFile">
       <label class="custom-file-label" for="customFile">Вставьте картинку </label>
     </div>
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
      tags: []
    }
  },
  methods: {
    addTag(tag) {
      this.tags.push(tag.id);
      console.log(this.tags)
    }
  },
  mounted() {
    axios.get('http://fefubr.tk/api/content/tag').then((res) => {
      this.userTags = res.data
    })
  }
}
</script>

<style scoped>

</style>