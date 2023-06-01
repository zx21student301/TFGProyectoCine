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

