$(document).ready(function() {
  var $row = $('.row-featured'); // Selecciona la fila que contiene las tarjetas
  var rowWidth = $row.width(); // Obtiene el ancho total de la fila
  var productCardWidth = $('.product-card').outerWidth(true); // Obtiene el ancho de una tarjeta, incluyendo margen

  // Calcular cuántas tarjetas caben en una fila completa
  var numItemsPerRow = Math.floor(rowWidth / productCardWidth);

  // Obtener el total de tarjetas
  var totalItems = $row.children().length;

  // Calcular cuántos elementos deberían ocultarse
  var itemsToHide = totalItems % numItemsPerRow;

  if (itemsToHide > 0) {
      // Oculta los últimos 'itemsToHide' elementos
      $row.children(':nth-last-child(-n+' + itemsToHide + ')').hide();
  }
});