<template>
  <!--    Импорт шрифта Inter-->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">
  <!--    Импорт шрифта Inter-->

  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <nav class="navbar navbar-expand-lg navbar-light bg mx-auto">
    <div class="container-fluid container d-flex">
      <div class="a-div">
        <a class="navbar-brand logo " href="#">Fefubr <span class="account">Аккаунт</span></a>
      </div>

    </div>
  </nav>

</template>


<script>
export default {
  name: "HeaderLogPage",
  methods: {
  }
}
</script>

<style>

.bg{
  height: 82px;
  box-shadow: 0px 4px 4px gray;
  margin: 0;
}
.container{
  padding: 0;

}
.navbar__btns {
  height: 82px;
  max-width: 100%;
  margin: 0;
}

.logo-div{
  padding: 10px 0 10px 0;
}

.main-div button{
  padding-right: 40px;
}

.logo{
  font-family: 'Inter';
  text-transform: uppercase;
  font-style: normal;
  font-weight: bold;
  font-size: 50px;
  line-height: 61px;
  color: #000000;
  text-decoration: none;
  cursor: pointer;
}

.logo:hover{
  color: black;
}

.account{
  font-family: 'Inter';
  font-style: normal;
  font-weight: normal;
  font-size: 45px;
  line-height: 61px;
  color: #000000;
}

</style>