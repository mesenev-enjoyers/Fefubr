<template>
    <button class="btn btn-primary">
      <slot></slot>
    </button>
</template>

<script>
export default {
  name: "ClassicBtn",
  methods: {
  }
}
</script>

<style scoped>
.btn{
  width: 300px;
  height: 54px;
  color: black;
  background-color:white;
  border-width: 2px;
  border-color: #5F77BF;
}

.btn:hover{
  width: 300px;
  height: 54px;
  color: white;
  background-color: #5F77BF;
  border-color: #5F77BF;
}

.btn:active {
  width: 300px;
  height: 54px;
  color: black;
  background-color:white;
  border-width: 2px;
  border-color: #5F77BF;
}


</style>