app.controller('MainController', function($scope, $http){
	$http.get('https://yarnsh.firebaseio.com/.json')
		.then(function(response) {
			$scope.yarns = response.data;
	});
});

app.filter('nospace', function () {
    return function (value) {
        return (!value) ? '' : value.replace(/ /g, '');
    };
});