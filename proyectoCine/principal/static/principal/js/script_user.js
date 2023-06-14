entradas = 0
butacasId = []

$(document).ready(
  function () {



    var titulosPeliculas = [];
    var imagenUrl = [];
    var funcion = [];
    var sala = [];
    var butacas = [];
    var precio = [];
    var peliculaID = [];


    $('.peliculaTituloJS').each(function () {
      var html = $(this).html();
      titulosPeliculas.push(html);
    });

    $('.peliculaImagenUrlJS').each(function () {
      var html = $(this).html();
      imagenUrl.push(html);
    });

    $('.funcionJS').each(function () {
      var html = $(this).html();
      funcion.push(html);
    });

    $('.salaJS').each(function () {
      var html = $(this).html();
      sala.push(html);
    });

    $('.butacasJS').each(function () {
      var html = $(this).html();
      butacas.push(html);
    });

    $('.precioJS').each(function () {
      var html = $(this).html();
      precio.push(html);
    });

    $('.peliculaIdJS').each(function () {
      var html = $(this).html();
      peliculaID.push(html);
    });

    console.log(titulosPeliculas);

    console.log($('#divCrearEntradas'))

    numEntradas = "{{entradas}}"
    if (titulosPeliculas.length === 0) {
      $('#divCrearEntradas').append(`

      <li>No se encontraron entradas asignadas.</li>,
      
      `)
    } else {
      $('#divCrearEntradas').empty()
      for (let index = 0; index < titulosPeliculas.length; index++) {
        $('#divCrearEntradas').append(`
            <div id="listarPelicula">
                <div id="divListarImg">
                    <img src="`+imagenUrl[index] +`" alt="">
                </div>
                <div id="divListarDatos">
                    <p id="nombrePelicula">`+titulosPeliculas[index] +`</p>
                    <p id="kmPelicula">`+funcion[index] +`</p>
                    <p id="kmPelicula">`+sala[index] +`</p>
                    <p id="kmPelicula"> Butacas: `+butacas[index] +` </p>
                    <p id="precioPelicula">Total: `+precio[index] +` €</p>
                </div>
            </div>
        `)
        
      }
    }

    console.log(entradas)





  }


);
