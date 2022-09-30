
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope, $http) {
  console.log("controller registered")
  $scope.httpcall=function(){
  $http({
    method : "GET",
    url : "http://127.0.0.1:8000/list/"
  }).then(function mySuccess(response) {
    var x=[]
    var cpu=[]
    var ram=[]
      $scope.mydata = response.data;
      console.log($scope.mydata)
      for(var i=0;i<$scope.mydata.length;i++){
        x.push($scope.mydata[i]['date_time'])
        cpu.push($scope.mydata[i]['cpu_usage'])
        ram.push($scope.mydata[i]['ram_usage'])
      }
      var trace1 = {
        x: x,
        y: cpu,
        type: 'scatter',
        mode: 'lines',
        name: 'CPU Usage',
        line: {
          color: 'rgb(219, 64, 82)',
          width: 3
        }
      };
      
      var trace2 = {
        x: x,
        y: ram,
        type: 'scatter',
         mode: 'lines',
        name: 'RAM Usage',
        line: {
          color: 'rgb(55, 128, 191)',
          width: 3
        }
      };
      
      var data = [trace1, trace2];
      
      Plotly.newPlot('myDiv', data, {}, {showSendToCloud: true});

      var trace1 = {
        x: x,
        y: cpu,
        type: 'bar',
        
        name: 'CPU Usage',
        
      };
      
      var trace2 = {
        x: x,
        y: ram,
        type: 'bar',
        name: 'RAM Usage',
       
      };
      
      var data = [trace1, trace2];
      var layout = {barmode: 'group'};

      Plotly.newPlot('myDiv1', data, layout, {}, {showSendToCloud:true});




      console.log(cpu,ram,x)
    }, function myError(response) {
      $scope.mydata = response.statusText;
      console.log($scope.mydata);
  });

}


setInterval(function(){
  $scope.httpcall();
}, 2000)
});