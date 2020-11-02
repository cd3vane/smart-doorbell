# importing socket module 
import socket 
  
UDP_IP = "192.168.1.129"
UDP_PORT = 8080
  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT)) 
  
while True: 
    # buffer size is 1024 bytes 
    data, addr = sock.recvfrom(1024)  
    print ("Received message:", data) 
