$(principal)

$(document).ready(function () {
  $("#barraBusqueda").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $(".card").filter(function () {
      $(this).toggle($(this).find(".card-title").text().toLowerCase().indexOf(value) > -1)
    });
    $(".peliculaCont").filter(function () {
      $(this).toggle($(this).find(".tituloPelicula").text().toLowerCase().indexOf(value) > -1)
    });
  });
});

function principal() {



  $('#registrarseID').click(function () {
    $('.divCuentas').css('visibility', 'visible');
    $('.divCuentas').empty();
    $('.divCuentas').html('<ul class="custom-tab-group">' +
      '   <li class="custom-tab active" id="tituloReg"><a href="#custom-signup">Regístrate</a></li>' +
      '   <li class="custom-tab " id="tituloIni"><a href="#custom-login">Iniciar Sesión</a></li>' +
      '</ul>' +
      ' <div id="custom-formulario">' +
      '      <h1>Regístrate</h1>' +
      '      <form action="/" method="post">' +
      '          <div class="custom-top-row">' +
      '              <div class="custom-field-wrap">' +
      '                  <input type="text" required autocomplete="off" placeholder="Nombre*" >' +
      '              </div>' +
      '              <div class="custom-field-wrap">' +
      '                  <input type="text" required autocomplete="off" placeholder="Apellidos*">' +
      '              </div>' +
      '          </div>' +
      '          <div class="custom-field-wrap">' +
      '              <input type="email" required autocomplete="off" placeholder="Correo electronico"/>' +
      '          </div>' +
      '          <div class="custom-field-wrap">' +
      '              <input type="password" required autocomplete="off" placeholder="Contraseña*">' +
      '          </div>' +
      '          <button type="submit" class="button button-block">Regístrate</button>' +
      '      </form>' +
      '  </div>');
    logRegForm()
  });

  $('#iniciarID').click(function () {
    $('.divCuentas').css('visibility', 'visible');
    $('.divCuentas').empty();
    $('.divCuentas').html('<ul class="custom-tab-group">' +
      '   <li class="custom-tab" id="tituloReg"><a href="#custom-signup">Regístrate</a></li>' +
      '   <li class="custom-tab active" id="tituloIni"><a href="#custom-login">Iniciar Sesión</a></li>' +
      '</ul>' +
      '   <div id="custom-formulario">' +
      '     <h1>Iniciar Sesión</h1>' +
      '<form action="/" method="post">' +
      '    <div class="custom-field-wrap">' +
      '        <input type="email" required autocomplete="off" placeholder="Correo electronico*"/>' +
      '    </div>' +
      '    <div class="custom-field-wrap">' +
      '        <input type="password" required autocomplete="off" placeholder="Contraseña*"/>' +
      '    </div>' +
      '    <br> <p class="forgot"><a href="#">Recuperar contraseña?</a></p>' +
      '    <button class="button button-block">Iniciar Sesion</button>' +
      '</form>' +
      '</div>');
    logRegForm()
  });

  $('.cuerpo').click(function () {
    $('.divCuentas').empty();
    $('.divCuentas').css('visibility', 'hidden');

  });
}

function logRegForm() {
  $('#tituloReg').click(function () {
    $('.divCuentas').empty();
    $('.divCuentas').html('<ul class="custom-tab-group">' +
      '   <li class="custom-tab active" id="tituloReg"><a href="#custom-signup">Regístrate</a></li>' +
      '   <li class="custom-tab " id="tituloIni"><a href="#custom-login">Iniciar Sesión</a></li>' +
      '</ul>' +
      ' <div id="custom-formulario">' +
      '      <h1>Regístrate</h1>' +
      '      <form action="/" method="post">' +
      '          <div class="custom-top-row">' +
      '              <div class="custom-field-wrap">' +
      '                  <input type="text" required autocomplete="off" placeholder="Nombre*" >' +
      '              </div>' +
      '              <div class="custom-field-wrap">' +
      '                  <input type="text" required autocomplete="off" placeholder="Apellidos*">' +
      '              </div>' +
      '          </div>' +
      '          <div class="custom-field-wrap">' +
      '              <input type="email" required autocomplete="off" placeholder="Correo electronico"/>' +
      '          </div>' +
      '          <div class="custom-field-wrap">' +
      '              <input type="password" required autocomplete="off" placeholder="Contraseña*">' +
      '          </div>' +
      '          <button type="submit" class="button button-block">Regístrate</button>' +
      '      </form>' +
      '  </div>');
    logRegForm()
  });

  $('#tituloIni').click(function () {
    $('.divCuentas').empty();
    $('.divCuentas').html('<ul class="custom-tab-group">' +
      '   <li class="custom-tab" id="tituloReg"><a href="#custom-signup">Regístrate</a></li>' +
      '   <li class="custom-tab active" id="tituloIni"><a href="#custom-login">Iniciar Sesión</a></li>' +
      '</ul>' +
      '   <div id="custom-formulario">' +
      '     <h1>Iniciar Sesión</h1>' +
      '<form action="/" method="post">' +
      '    <div class="custom-field-wrap">' +
      '        <input type="email" required autocomplete="off" placeholder="Correo electronico*"/>' +
      '    </div>' +
      '    <div class="custom-field-wrap">' +
      '        <input type="password" required autocomplete="off" placeholder="Contraseña*"/>' +
      '    </div>' +
      '    <br> <p class="forgot"><a href="#">Recuperar contraseña?</a></p>' +
      '    <button class="button button-block">Iniciar Sesion</button>' +
      '</form>' +
      '</div>');
    logRegForm()
  });
}