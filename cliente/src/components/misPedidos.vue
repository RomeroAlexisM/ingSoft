<template>
  <div id="pedidos">
    <div class="row margenSuperior">
      <div class="card tarjetas text-center centrar" v-if="!editar" v-for="pedido in pedidos" :key="pedido.key">
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
      <editarPedido v-else-if="editar"></editarPedido>
    </div>
  </div>
</template>
<script>
import editarPedido from './editarPedido'
import axios from 'axios'
import eventBus from '../bus'
export default {
  name: "pedidos",
  data() {
    return {
      editar: false,
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
      eventBus.$emit('editarPedido', this.pedidos[idPedido]);
      this.editar = !this.editar;
    }
  },
  components: {
    editarPedido
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
