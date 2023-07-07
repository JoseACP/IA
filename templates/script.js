$(document).ready(function() {
    $.ajax({
        url: 'http://127.0.0.1:5000',  // Reemplaza con la URL de tu API
        method: 'GET',
        dataType: 'json',
        success: function(response) {
            var apiDataElement = $('#api-data');
            
            // Limpia el contenido existente
            apiDataElement.empty();
            
            // Recorre los datos y agrega elementos de lista a la página
            response.forEach(function(item) {
                var listItem = $('<li>').text(item);
                apiDataElement.append(listItem);
            });
        },
        error: function() {
            console.log('Error al obtener los datos de la API');
        }
    });
});
