<template>
<div class="root">
  <nav class="top-menu">
    <ul class="menu-main">
      <li class="left-item"><a href="">Все публикации</a></li>
      <li class="left-item"><a href="">Моя лента</a></li>
      <li class="left-item"><a href="">Общение</a></li>
      <li class="right-item"><a href="">Войти/Зарегистрироваьтся</a></li>
      <li class="right-item"><a href="">Профиль</a></li>
    </ul>
  </nav>
</div>
</template>

<script>
export default {
  name: "NavBar"
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Arimo');
.top-menu {
  position: relative;
  background: #5f77bf;
}
.menu-main {
  list-style: none;
  margin: 0;
  padding: 0;
}
.menu-main:after {
  content: "";
  display: table;
  clear: both;
}
.left-item {float: left;}
.right-item {float: right;}
.menu-main a {
  text-decoration: none;
  display: block;
  line-height: 80px;
  padding: 0 20px;
  font-size: 16px;
  letter-spacing: 2px;
  font-family: 'Arimo', sans-serif;
  font-weight: bold;
  color: white;
  transition: .3s linear;
}
.menu-main a:hover {background: rgba(0,0,0,.3);}
@media (max-width: 830px) {
  .menu-main {
    padding-top: 90px;
    text-align: center;
  }
  .menu-main li {
    float: none;
    display: inline-block;
  }
  .menu-main a {
    line-height: normal;
    padding: 10px 15px;
    font-size: 16px;
  }
}
@media (max-width: 630px) {
  .menu-main li {display: block;}
}
</style>