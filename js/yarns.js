app.factory('yarnData', ['$http', function($http) {
        return $http.get('https://yarnsh.firebaseio.com/.json')
        .success(function(data) {
            return data;
        })
        .error(function(err) {
            return err;
        });
}]);