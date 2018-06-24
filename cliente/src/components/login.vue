<template>
  <div class="container" id="login" >
    <div class="row " v-if="!logueado">
      <div class="jumbotron boxLogin centrar">
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
      axios.post('http://127.0.0.1:8000/login/', {
        username: this.username,
        password: this.password
      })
      .then((response) => {
        this.logueado = !this.logueado;
        // console.log(response);
      })
      .catch((error) => {
      alert("usuario desconosido");
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

  .centrar {
    margin: 0 auto;
  }

</style>
