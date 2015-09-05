
angular.module('facturasApp', ['ngResource'])
       .config(['$resourceProvider', function($resourceProvider) {
       // Don't strip trailing slashes from calculated URLs
          $resourceProvider.defaults.stripTrailingSlashes = false;
  }]).controller('FacturasController', [
          '$resource', // need to inject $http into controller
	  '$http',
      function($resource, $http) {
        var facturas = this;
        var Entrada = $resource('/api/enero/lineas/linea/:id', {});
	facturas.entradas = Entrada.query({}, function(data){
	    var grouped = _.groupBy(data, 'empresa');
	    facturas.entradas = _.map(grouped, function(entradas, empresa){
                return { "empresa": empresa, "entradas": entradas};
            });

	});

	facturas.nuevaEntrada = { }

        facturas.addNewEntry = function() {
          var copy = { 
	      numero: facturas.nuevaEntrada.numero, 
	      dia: facturas.nuevaEntrada.dia,
	      base_imponible: facturas.nuevaEntrada.base_imponible,
	      iva: facturas.nuevaEntrada.iva,
	      empresa: facturas.nuevaEntrada.empresa
          };
          $http({
              method: 'POST',
              url: '/api/enero/lineas/linea/',
              data: $.param(copy),
              headers: {'Content-Type': 'application/x-www-form-urlencoded'}
          })
	  facturas.entradas = Entrada.query({}, function(data){
	      var grouped = _.groupBy(data, 'empresa');
	      facturas.entradas = _.map(grouped, function(entradas, empresa){
                  return { "empresa": empresa, "entradas": entradas};
              });

	  });

          facturas.nuevaEntrada = {};
          document.getElementById("numero").focus();
        };
 
 
}]);

