<template>
 <div class="root">
   <form>
     <label>Название</label>
     <input type="text" v-model="name">
      <label>Содержание</label>
     <textarea v-model="content"></textarea>
     <label>Теги</label>
      <label>Вставьте картинку</label>
     <input type="file">
     <button>Опубликовать</button>
   </form>
 </div>
</template>

<script>
export default {
  name: "CreateUserPost",
  data() {
    return {
      name: '',
      content: '',
    }
  }
}
</script>

<style scoped>

</style>