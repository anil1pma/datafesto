var app = angular.module('sendMessage', ["angularjs-datetime-picker"]);
app.controller('sendMessageController', function($scope, $http, $window, $timeout) {
    $scope.names = ["Email","SMS"];
    $scope.minDate = new Date()
    $scope.sendMessage = function() {
         var current_time = new Date().getTime();
         var user_time = new Date($scope.message_time).getTime();
         if($scope.emailaddress === undefined || $scope.mobnumber === undefined){
              alert("Please select mobile number or eimal or both");
             }

          else if(($scope.emailaddress && $scope.mobnumber) && !($scope.checkboxModel.value1 || $scope.checkboxModel.value2)){
              alert("Please select sms or email");
             }

          else if(!($scope.emailaddress && $scope.mobnumber) && !(($scope.emailaddress && $scope.checkboxModel.value1) || ($scope.mobnumber && $scope.checkboxModel.value2))){
                alert("Please select email");
                }
          else if( user_time < current_time){
            alert("Please select correct time");
             }
        else {
        var message_through;
        if( $scope.checkboxModel.value1 && $scope.checkboxModel.value12 )
            message_through = "Email" + "|" + "SMS";
        else if($scope.checkboxModel.value1)
            message_through = "Email"
        else
            message_through = "SMS"

        $http({
            url: "/polls/savedata",
            method: "POST",
            data: {"mobnumber": $scope.mobnumber, "emailaddress": $scope.emailaddress,"message": $scope.message,"message_time":$scope.message_time, "message_through":message_through}
        }).success ( function () {
            $window.location.href = '/';
        });
       }
      }
});
