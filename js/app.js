(function(){

	var myApp = angular.module('myApp', []);

	myApp.controller('MyController', ['$scope', '$http', function($scope, $http) {
	  $http.get('yarn.json').success(function(data) {
	    $scope.yarns = data.results;
	  });

	}]);


})();



