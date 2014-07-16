"use strict";

var app = angular.module("mgcrea.ngStrapDocs",['ngAnimate', 'ngSanitize', 'mgcrea.ngStrap']);

app.controller('MainCtrl', function($scope) {});
    
angular.module("mgcrea.ngStrapDocs").config(
    ["$asideProvider",function(e){
            angular.extend(e.defaults,{container:"body",html:!0})
        }]).controller("AsideDemoCtrl",
            ["$scope",function(e){
                e.aside={
                    title:"Settings",
                    content:"Hello Aside<br />This is a multiline message!"
                }
    }
]);

