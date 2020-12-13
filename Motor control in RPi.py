#!/usr/bin/python
# Most of this code came from the Scrap to Power website:
# https://www.raspberrypi-spy.co.uk/2012/07/stepper-motor-control-in-python/
# We changed several parameters including the step count and the wait time.
#
# We also added networking code to make the Python process communicate with Node-RED via UDP.

# Import required libraries

import socket
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 11,12,13,15
# GPIO17,GPIO18,GPIO21,GPIO22
StepPins = [17,18,21,22]

# Set all pins as output
for pin in StepPins:
    print ("Setup pins")
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)

# Define advanced sequence
# as shown in manufacturers datasheet
Seq = [[1,0,0,1],
[1,0,0,0],
[1,1,0,0],
[0,1,0,0],
[0,1,1,0],
[0,0,1,0],
[0,0,1,1],
[0,0,0,1]]

StepCount = len(Seq)
StepDir = 1 # Set to 1 or 2 for clockwise
# Set to -1 or -2 for anti-clockwise

# Read wait time from command line
#if len(sys.argv)>1:
#    WaitTime = int(sys.argv[1])/float(1000)
#else:
#    WaitTime = 10/float(1000)
WaitTime = 1/float(1000)



# Initialise variables
StepCounter = 0

# Start main loop

def turn(StepDir = 1, N = 1000, StepCounter = StepCounter, StepCount = StepCount):
    for i in range(N):

        #print (StepCounter)
        #print (Seq[StepCounter])

        for pin in range(0, 4):
            xpin = StepPins[pin]
            if Seq[StepCounter][pin]!=0:
                #print(" Enable GPIO %i" %(xpin))
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        StepCounter += StepDir

        # If we reach the end of the sequence
        # start again
        if (StepCounter>=StepCount):
            StepCounter = 0
        if (StepCounter<0):
            StepCounter = StepCount+StepDir

        # Wait before moving on
        time.sleep(WaitTime)
    

locked = False

def lock(locked):
    if not locked:
        turn(+1)
    return True

   
def unlock(locked):
    if locked:
        turn(-1)
    return False

def listen_for_udp_command(): 
    UDP_IP = "127.0.0.1"
    UDP_RECEIVE_PORT = 6600
    UDP_SEND_PORT = 6700
   
    sock_rx = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock_rx.bind((UDP_IP, UDP_RECEIVE_PORT))
    
    sock_tx = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    
    locked = False

    while True:
        data, addr = sock_rx.recvfrom(1024) # buffer size is 1024 bytes
        print("received message: %s" % data)
        if data == b'lock':
            if locked:
                sock_tx.sendto(b'Already locked.', (UDP_IP, UDP_SEND_PORT))
            else:
                locked = lock(locked)
                sock_tx.sendto(b'Successfully locked.', (UDP_IP, UDP_SEND_PORT))
        if data == b'unlock':
            if not locked:
                sock_tx.sendto(b'Already unlocked.', (UDP_IP, UDP_SEND_PORT))
            else:
                locked = unlock(locked)
                sock_tx.sendto(b'Successfully unlocked.', (UDP_IP, UDP_SEND_PORT))
