# We adapted the code from docs.python.org (https://docs.python.org/3/library/http.server.html) and
# mdonkers (https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7) 

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import paho.mqtt.client as mqtt

hostName = ""
serverPort = 6600

mqtt_host = "test.mosquitto.org"
client_name = "Test doorbell commander."
client = mqtt.Client(client_name)

client.connect(mqtt_host)
last_connect_time = time.time()


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


        global last_connect_time
        now = time.time()

        if now - last_connect_time > 180:
            client.reconnect()
            last_connect_time = now
        

        if self.path == "/lock.html":
            client.publish("doorbell-lock-12345", "lock")
            print("Request received for", self.path)
        if self.path == "/unlock.html":
            client.publish("doorbell-lock-12345", "unlock")
            print("Request received for", self.path)
        

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

client.publish("doorbell-lock-12345", "lock")
