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
      axios.post('/login', {
    firstName: this.username,
    lastName: this.password
    })
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });
      // this.logueado = !this.logueado;

    }
  },
  components: {
    barraBienvenida
  }
}
</script>
<style lang="scss" scoped>
@import './node_modules/bootstrap/scss/bootstrap.scss';
#login {
  margin: 0 auto;
}
</style>
