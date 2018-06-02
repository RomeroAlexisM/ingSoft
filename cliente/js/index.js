var app= new Vue({
  el: '#app',
  data: {
    mostrar: true
  },
  methods:{
    cambiarEstado: function(){
      this.mostrar = !this.mostrar;
    },
    cambiar: function(){
      console.log("se");
    }
  }
});

// var usuario = new Vue({
//   el: '#usuario',
//   data: {
//     mostrar: false
//   },
//   methods:{
//
//   }
// });
