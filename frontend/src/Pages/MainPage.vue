<template>
 <div class="root">Hello, world</div>
  likes: {{ $store.getters.doubleLikes}}
</template>

<script>
export default {
  name: "MainPage"
}
</script>

<style scoped>

</style>