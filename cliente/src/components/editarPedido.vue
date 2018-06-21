<template>
  <div id="editarPedido">
    <h1>{{ pedido_id }} la wea</h1>
  </div>
</template>
<script>
import eventBus from '../bus.js'
export default {
  name: "editarPedido",
  data: function(){
    return {
      pedido_id: ''
    }
  },
 created: function() {
      eventBus.$on('editarPedido', function(detallePedido){
        this.pedido_id = detallePedido.id
      });

  }
}
</script>
<style lang="scss" scoped>
</style>
