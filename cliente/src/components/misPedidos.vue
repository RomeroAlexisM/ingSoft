<template>
  <div id="pedidos">
    <div class="row margenSuperior">
      <!-- <button class="btn btn-primary"type="button" name="button" v-on:click='obtenerPedidos'>Pedidos</button> -->
      <div class="card tarjetas text-center centrar" v-for="pedido in pedidos" :key="pedido.key">
        <div class="card-body">
          <h3 class="tamañoTitulo">{{ pedido.tipo_de_pedido }}</h3>
          <p>{{ pedido.asunto }}</p>
          <h3 class="tamañoTitulo">PRIORIDAD</h3>
          <p>{{ pedido.prioridad }}</p>
          <h3 class="tamañoTitulo">FECHA</h3>
          <p>{{ pedido.fecha }}</p>
          <button type="button" name="cancelar" class="btn btn-danger">CANCELAR</button>
          <button type="button" name="editar" class="btn btn-primary"  v-on:click="editarPedido(pedido.id)">EDITAR</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
// import editarPedido from './editarPedido'
import axios from 'axios'
// import EventBus from './bus'
export default {
  name: "pedidos",
  data() {
    // editar =false;
    return {
      pedidos: []
    }
  },
  created: function() {
      // axios.get("http://127.0.0.1:8000/pedidos/")
    axios.get("pedidos.json")
    .then((response)  =>  {
      this.pedidos = response.data;
    }, (error)  =>  {
      console.log(error);
    })

  },
  methods: {
    editarPedido(idPedido) {
      this.editar = !this.editar;
      EventBus.$emit('editarPedido', this.pedidos[idPedido]);
    }

  }
}
</script>
<style lang="scss" scoped>
.row p {
  font-size: 1.1em;
}

.tarjetas {
  /* left: 30%; */
  border: 1px solid black;
  width: 20em;
  // margin-left: 1em;
  // margin-top: 1em;
}

.margenSuperior {
  margin-top: 10px;
}

.tamañoTitulo {
  font-size: 1.3em;
}

.centrar {
  margin: 1em auto;
}
</style>
