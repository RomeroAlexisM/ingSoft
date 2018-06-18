<template>
  <div id="editarPedido">
    <h1>EDITAR</h1>
  </div>
</template>
<script>
import EventBus from './bus'
export default {
  name: "editarPedido",
  data: () => ({
    // pedido: []
  }),
 created: function() {

      EventBus.$on('editarPedido',function(detallePedido){
        console.log(detallePedido)
        // this.pedido = detallePedido
      });

  }
}
</script>
<style lang="scss" scoped>
</style>
