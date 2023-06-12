entradas=0

$(document).ready(
  function () {
    $("#barraBusqueda").on("keyup", function () {
      var value = $(this).val().toLowerCase();
      $(".card").filter(function () {
        $(this).toggle($(this).find(".card-title").text().toLowerCase().indexOf(value) > -1)
      });
      $(".peliculaCont").filter(function () {
        $(this).toggle($(this).find(".tituloPelicula").text().toLowerCase().indexOf(value) > -1)
      });
      valor = value
      console.log(valor)
    });

    $('.butaca').click(function () {
      var estado = $(this).attr('estado');
   

      if (estado === 'disponible') {
        $(this).attr('fill', '#28a745');
        $(this).attr('estado', 'seleccionada');
        entradas+=1
      } else if (estado === 'seleccionada') {
        $(this).attr('fill', '#ffffff');
        $(this).attr('estado', 'disponible');
        entradas=entradas-1
      }

      $('#numEntradas').empty();
      $('#numEntradas').html(entradas);

    });

    $('#btnComprar').click(function slideOut() {
      console.log("las")
      var myDiv = document.getElementById("divAni");
      var myDiv2 = document.getElementById("secondDiv");
      
      myDiv.classList.add("slide-out");
      myDiv2.classList.add("slide-in");

      // Esperar a que finalice la animación antes de eliminar el div
      $("#secondDiv").css('display', 'flex');
      setTimeout(function () {
        $("#divAni").css('display', 'none');
      }, 500);

    })

    $('#btnVolver').click(function slideOut() {
      var myDiv = document.getElementById("divAni");
      var myDiv2 = document.getElementById("secondDiv");
    
      // Eliminar las clases de animación
      myDiv.classList.remove("slide-out");
      myDiv2.classList.remove("slide-in");
    
      // Mostrar nuevamente el primer div y ocultar el segundo div
      $("#divAni").css('display', 'block');
      $("#secondDiv").css('display', 'none');

    })
  }
);


//   $('#registrarseID').click(function () {
//     $('.divCuentas').css('visibility', 'visible');
//     $('.divCuentas').empty();
//     $('.divCuentas').html('<ul class="custom-tab-group">' +
//       '   <li class="custom-tab active" id="tituloReg"><a href="#custom-signup">Regístrate</a></li>' +
//       '   <li class="custom-tab " id="tituloIni"><a href="#custom-login">Iniciar Sesión</a></li>' +
//       '</ul>' +
//       ' <div id="custom-formulario">' +
//       '      <h1>Regístrate</h1>' +
//       '      <form action="/" method="post">' +
//       '          <div class="custom-top-row">' +
//       '              <div class="custom-field-wrap">' +
//       '                  <input type="text" required autocomplete="off" placeholder="Nombre*" >' +
//       '              </div>' +
//       '              <div class="custom-field-wrap">' +
//       '                  <input type="text" required autocomplete="off" placeholder="Apellidos*">' +
//       '              </div>' +
//       '          </div>' +
//       '          <div class="custom-field-wrap">' +
//       '              <input type="email" required autocomplete="off" placeholder="Correo electronico"/>' +
//       '          </div>' +
//       '          <div class="custom-field-wrap">' +
//       '              <input type="password" required autocomplete="off" placeholder="Contraseña*">' +
//       '          </div>' +
//       '          <button type="submit" class="button button-block">Regístrate</button>' +
//       '      </form>' +
//       '  </div>');
//     logRegForm()
//   });

//   $('#iniciarID').click(function () {
//     $('.divCuentas').css('visibility', 'visible');
//     $('.divCuentas').empty();
//     $('.divCuentas').html('<ul class="custom-tab-group">' +
//       '   <li class="custom-tab" id="tituloReg"><a href="#custom-signup">Regístrate</a></li>' +
//       '   <li class="custom-tab active" id="tituloIni"><a href="#custom-login">Iniciar Sesión</a></li>' +
//       '</ul>' +
//       '   <div id="custom-formulario">' +
//       '     <h1>Iniciar Sesión</h1>' +
//       '<form action="/" method="post">' +
//       '    <div class="custom-field-wrap">' +
//       '        <input type="email" required autocomplete="off" placeholder="Correo electronico*"/>' +
//       '    </div>' +
//       '    <div class="custom-field-wrap">' +
//       '        <input type="password" required autocomplete="off" placeholder="Contraseña*"/>' +
//       '    </div>' +
//       '    <br> <p class="forgot"><a href="#">Recuperar contraseña?</a></p>' +
//       '    <button class="button button-block">Iniciar Sesion</button>' +
//       '</form>' +
//       '</div>');
//     logRegForm()
//   });

//   $('.cuerpo').click(function () {
//     $('.divCuentas').empty();
//     $('.divCuentas').css('visibility', 'hidden');

//   });
// }

// function logRegForm() {
//   $('#tituloReg').click(function () {
//     $('.divCuentas').empty();
//     $('.divCuentas').html('<ul class="custom-tab-group">' +
//       '   <li class="custom-tab active" id="tituloReg"><a href="#custom-signup">Regístrate</a></li>' +
//       '   <li class="custom-tab " id="tituloIni"><a href="#custom-login">Iniciar Sesión</a></li>' +
//       '</ul>' +
//       ' <div id="custom-formulario">' +
//       '      <h1>Regístrate</h1>' +
//       '      <form action="/" method="post">' +
//       '          <div class="custom-top-row">' +
//       '              <div class="custom-field-wrap">' +
//       '                  <input type="text" required autocomplete="off" placeholder="Nombre*" >' +
//       '              </div>' +
//       '              <div class="custom-field-wrap">' +
//       '                  <input type="text" required autocomplete="off" placeholder="Apellidos*">' +
//       '              </div>' +
//       '          </div>' +
//       '          <div class="custom-field-wrap">' +
//       '              <input type="email" required autocomplete="off" placeholder="Correo electronico"/>' +
//       '          </div>' +
//       '          <div class="custom-field-wrap">' +
//       '              <input type="password" required autocomplete="off" placeholder="Contraseña*">' +
//       '          </div>' +
//       '          <button type="submit" class="button button-block">Regístrate</button>' +
//       '      </form>' +
//       '  </div>');
//     logRegForm()
//   });

//   $('#tituloIni').click(function () {
//     $('.divCuentas').empty();
//     $('.divCuentas').html('<ul class="custom-tab-group">' +
//       '   <li class="custom-tab" id="tituloReg"><a href="#custom-signup">Regístrate</a></li>' +
//       '   <li class="custom-tab active" id="tituloIni"><a href="#custom-login">Iniciar Sesión</a></li>' +
//       '</ul>' +
//       '   <div id="custom-formulario">' +
//       '     <h1>Iniciar Sesión</h1>' +
//       '<form action="/" method="post">' +
//       '    <div class="custom-field-wrap">' +
//       '        <input type="email" required autocomplete="off" placeholder="Correo electronico*"/>' +
//       '    </div>' +
//       '    <div class="custom-field-wrap">' +
//       '        <input type="password" required autocomplete="off" placeholder="Contraseña*"/>' +
//       '    </div>' +
//       '    <br> <p class="forgot"><a href="#">Recuperar contraseña?</a></p>' +
//       '    <button class="button button-block">Iniciar Sesion</button>' +
//       '</form>' +
//       '</div>');
//     logRegForm()
//   });
// }

