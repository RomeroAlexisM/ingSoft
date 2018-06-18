<template>
  <div id="formError">
    <div class="row">
      <div class="col-12">
        <form action="" id="formulario">
          <label for="asunto" method="post">asunto</label>
          <input type="text" id="asunto" class="form-control">
          <label for="detalle" method="post">detalle</label>
          <textarea id="detalle" class="form-control" rows="5"></textarea>
          <label for="prioridad" method="post">prioridad</label>
          <div class="form-group">
            <select name="" class="form-control">
                  <option value="uno">uno</option>
                  <option value="cuatro">cuatro</option>
                  <option value="tres">tres</option>
            </select>
          </div>
          <label for="sistema" method="post">sistema</label>
          <div class="form-group">
            <select name="" class="form-control">
                  <option value="uno">uno</option>
                  <option value="cuatro">cuatro</option>
                  <option value="tres">tres</option>
            </select>
          </div>
          <button type="submit" class="btn btn-primary form-control">ENVIAR</button>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "formError",
  data: () => ({

  })
}
</script>
<style lang="scss" scoped>
#formulario {
  margin: 0 auto;
  width: 50%;
}

#formulario label {
  margin-left: 42%;
}

#formulario button{
  width: 25%;
  margin-left: 35%;
}
</style>
