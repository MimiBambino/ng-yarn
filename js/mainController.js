app.controller('MainController', function($scope, $http){
	$http.get('data.json')
		.then(function(response) {
			$scope.yarns = response.data;
	});
});

app.directive('yarnImage', function(){
	return {
		restrict: 'E',
		templateUrl: 'templates/yarns.html'
	};
});

app.filter('nospace', function () {
    return function (value) {
        return (!value) ? '' : value.replace(/ /g, '');
    };
});