$(document).ready(function () {
    $("#barraBusqueda").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $(".card").filter(function () {
            $(this).toggle($(this).find(".card-title").text().toLowerCase().indexOf(value) > -1)
        });
    });
});


$('#carouselExampleIndicators').on('slid.bs.carousel', function () {
    var currentItem = $('.carousel-item.active');
    var nextItem = currentItem.next('.carousel-item');
  
    currentItem.find('.old-image').removeClass('old-image');
    nextItem.find('.new-image').addClass('old-image');
  });
  
  $('#carouselExampleIndicators').on('slide.bs.carousel', function () {
    var currentItem = $('.carousel-item.active');
    var nextItem = currentItem.next('.carousel-item');
  
    nextItem.find('.new-image').removeClass('old-image');
  });