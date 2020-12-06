
function lockDoor(){
  var url = "http://52.147.197.133:6600/lock.html";
  var method = "GET";
  var postData = "1";

  var shouldBeAsync = true;

  var request = new XMLHttpRequest();

  request.onload = function () {
    var status = request.status;
    var data = request.responseText; 
 }
 
 request.open(method, url, shouldBeAsync);
 
 request.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");

 request.send(postData);
}


function unlockDoor(){
  var url = "http://52.147.197.133:6600/unlock.html";
  var method = "GET";
  var postData = "0";

  var shouldBeAsync = true;

  var request = new XMLHttpRequest();

  request.onload = function () {
    var status = request.status;
    var data = request.responseText; 
 }
 
 request.open(method, url, shouldBeAsync);
 
 request.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");

 request.send(postData);
}
