<template>
  <div class="container">
    <div  id="barraSuperior">
      <div class="row colorFondo">
        <div class="textoBlanco col-12">
          <a href="#" id="logOut" v-on:click="cambiarEstado" class=" textoBlanco ">LOGOUT</a>
          <p class="text-center">BIENVENIDO "usuario"</p>
        </div>
      </div>
      <div class="row navegacion tamaño colorFondo" v-if="!logueado">
        <div class="btn margen ajustarTamaño colorTexto borde fondoBlanco hover col-12 col-md-4" v-on:click="nuevoRequerimiento">
          <p class="text-center mt-1">NUEVO REQUERIMIENTO</p>
        </div>
        <div class="btn  margen ajustarTamaño colorTexto borde fondoBlanco hover col-12 col-md-4" v-on:click="nuevoError">
          <p class="text-center mt-1">INFORMAR ERROR</p>
        </div>
        <div class="btn margen mBottom ajustarTamaño colorTexto borde fondoBlanco hover col-12 col-md-4" v-on:click="pedidos" >
          <p class="text-center mt-1">MIS PEDIDOS</p>
        </div>
      </div>
    </div>
    <formRequerimiento v-if="seccionRequerimiento"></formRequerimiento>
    <formError v-if="seccionError"></formError>
    <misPedidos v-if="seccionPedidos"></misPedidos>
  </div>
</template>

<script>
import misPedidos from './misPedidos'
import formRequerimiento from './formRequerimiento'
import formError from './formError'

export default {
  name: 'barraSuperior',
  props: {
    logueado: true,
    seccionRequerimiento: false,
    seccionError: false,
    seccionPedidos: false
  },
  methods: {
  cambiarEstado: function(){
    this.logueado = !this.logueado;
  },
  nuevoRequerimiento: function(){
    this.seccionRequerimiento = !this.seccionRequerimiento;
    this.seccionError = false;
    this.seccionPedidos = false;
  },
  nuevoError: function(){
    this.seccionError = !this.seccionError;
    this.seccionRequerimiento = false;
    this.seccionPedidos = false;
  },
  pedidos: function(){
    this.seccionPedidos = !this.seccionPedidos;
    this.seccionError = false;
    this.seccionRequerimiento = false;
  }
  },
  components: {
    misPedidos,
    formRequerimiento,
    formError
  }

}
</script>

<style lang = "scss">
@import './node_modules/bootstrap/scss/bootstrap.scss';

.colorFondo {
  background-color: #2699FB;
}

.textoBlanco {
  color: #FFFFFF;
}

.hover:hover {
  background-color: #2699FB;
  color: #FFFFFF;
  border: 1px solid #FFFFFF;
  transition:   background-color 0.5s, color 0.5s, border 0.5s;
}

.borde {
  border: 1px solid #2699FB;
}

.colorFondo {
  background-color: #2699FB;
}

.fondoBlanco {
  background-color: #FFFFFF;
}

.colorTexto {
  color: #2699FB;
}

@media only screen and (max-width: 768px) {
  .margen {
    margin-top: 40px;
    border-radius: 5px;
  }
  .mBottom {
    margin-bottom: 20px;
  }

  .ajustarTamaño {
    max-width: 70%;
    margin-left: 15%;
    max-height: 60px;
    font-size: 1.3em;
  }
  .container{
    height: 630px;
  }
  .navegacion{
    height: 80%;
  }

}
</style>
