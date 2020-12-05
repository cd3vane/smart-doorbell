
function lockDoor(){
    document.getElementById("demo").innerHTML = "Lock";
    broker_address="iot.eclipse.org" 
    client = mqtt.Client("P1") 
    client.connect(broker_address, port=1883) 
    client.publish("door/lock/unlock","Lock")
}

function unlockDoor(){
    document.getElementById("demo2").innerHTML = "Unlock";
    broker_address="iot.eclipse.org" 
    client = mqtt.Client("P1") 
    client.connect(broker_address, port=1883) 
    client.publish("door/lock/unlock","Unlock")
}


var mqtt = require('mqtt')
var client  = mqtt.connect('mqtt://test.mosquitto.org')
 
client.on('connect', function () {
  client.subscribe('door/lock/unlock', function (err) {
    if (!err) {
      client.publish('door/lock/unlock', 'Hello mqtt')
    }
  })
})
 
client.on('message', function (topic, message) {
  // message is Buffer
  console.log(message.toString())
  client.end()
})