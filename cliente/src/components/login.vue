<template>
  <div class="container">
    <div class="row" id="login" v-if="!logueado">
      <div class="jumbotron boxLogin">
        <div class="" id="bienvenido">
          <h1>BIENVENIDO</h1>
        </div>
        <form method="POST" class="formulario" name="login" id="form_login">
          <label for="">Nombre de usuario:</label>
          <input type="text" name="username" value="username" class="form-control" v-model="username">
          <label for="">Contraseña:</label>
          <input type="password" name="password" value="password" class="form-control" v-model="password">
          <a id="recuperarContraseña" href="#">¿Haz olvidado tu contraseña?</a>
          <input type="button" v-on:click="loguear" name="" class="btn btn-primary" value="Conectarse">
        </form>
      </div>
    </div>
    <barraBienvenida v-else></barraBienvenida>
  </div>
</template>
<script>
import barraBienvenida from './barraBienvenida'
import axios from 'axios'
export default {
  name: "login",
  data: function(){
    return{
      logueado: false,
      username: '',
      password: ''
    }
  },
  methods: {
    loguear() {
      axios.post('http://127.0.0.1:8000/login', {
    firstName: this.username,
    lastName: this.password
    })
    .then(function (response) {
      this.logueado = !this.logueado;
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });


    }
  },
  components: {
    barraBienvenida
  }
}
</script>
<style lang="scss" scoped>
@import './node_modules/bootstrap/scss/bootstrap.scss';
// #login {
//   margin-left: 35%;
// }
@media only screen and (max-width: 768px) {
  #login {
    margin-left: 5%;
  }
}
</style>
