var myApp = angular.module("myApp", []);
	
myApp.controller("userCtrl" , function($scope, $http){

    $scope.master = {username: "", password: "", fname: "", lname: "", birthday: "", email: "", phone: ""};

    $scope.reset = function() {
        $scope.user = angular.copy($scope.master);
    };
        
    $scope.reset();      
});

myApp.controller("loginCtrl" , function($scope, $http){

    $scope.master = {userName: "", password: ""};

    $scope.reset = function() {
        $scope.user = angular.copy($scope.master);
    };
        
    $scope.reset();      
});

myApp.controller("postCtrl" , function($scope, $http){

    $scope.master = {title: "", subtitle: "", content: "", author: ""};

    $scope.reset = function() {
        $scope.post = angular.copy($scope.master);
    };
        
    $scope.reset();      
});