IoT Device - Smart Doorbell and Lock

Authors: Charles DeVane, Donovan Graham, Yuri Villanueva

Version Number: 1.0.0
Project Overview
In this project, a Raspberry Pi or an Arduino will be used as the controller for a smart doorbell and lock. Doorbell presses will be time stamped and logged in a cloud database, along with optional images or video clips taken by one or more nearby cameras. This event will result in push notifications being sent to the owner’s mobile device(s), where they can view all tagged information in the cloud via web interface or optional mobile application. They can also lock or unlock the door using the same user interface. The cloud service will relay commands to the doorbell and lock controller and its actuator(s).


Team Member/Roles
Charles DeVane: Web Portal
Donovan Graham: Cloud Computing
Yuri Villanueva: Hardware- Raspberry Pi or Arduino

High Level Requirements
The cloud service should have the following functions:
Accept messages from the hardware controller.
Authenticate users who are logging on.
Send push notifications to user
Register first time users.
Allow owners to view their own information.
The hardware controller should have the following functions:
Detect sensor data (doorbell, lock, camera, etc.), 
Communicate the event to the cloud service.
Accept command originating from the user.
The user interface should have the following functions:
Register and sign in users.
Display owner's data.
Accept commands to control the IoT device.
Alert the user when push messages arrive from the cloud.

User Level Requirements
Accept first time user registration information
Name, email, phone number
Billing information, e.g credit card numbers.
Accept user login
View user's own information in the database
Display the state of the lock
Show the buttons to lock/unlock the door


System Level Requirements
The hardware controller detects sensor events, e.g., doorbell presses, door open/close, lock/unlocked, camera, etc.
The hardware controller will log sensor events and associated data to the cloud service.
The cloud service should accept commands from the user and relay them to the hardware controller.
 Commands and sensor events will be time stamped and logged in the database.



Technologies and Languages
GitHub for version control
SwaggerHub for API documentation
Microsoft Azure for cloud computing 
Python/Django for Web Portal
Bootstrap for CSS
Python on Raspberry Pi, C on Arduino


Platform/HW Selection
Raspberry Pi 3, Raspberry Pi 4, or Arduino Uno/ATMega
Video or still-image camera?


Milestones

First set of milestones. Work on these can proceed simultaneously:
PC/Mac/Linux computer simulating the IoT device (the doorbell/lock controller--a Raspberry Pi or Arduino) can log events to cloud database in Azure.
PC/Mac/Linux computer simulating owner's mobile device can view events and associated tagged data in the cloud database.
IoT hardware controller receives input signals from sensors--the doorbell, the lock, and the camera. It can send and receive electrical or radio signals to and from the door lock. Work on this can proceed independently from the first two. It can be moved to the second set of milestones if necessary.
Second set of milestones:
The computer simulating the owner's mobile device can send commands to the cloud service. The computer simulating the hardware controller can receive the same commands after being relayed by the cloud service.
Third set of milestones:
Hardware doorbell/lock controller can log messages and associated data to the cloud database. 
Owner mobile devices can view logged events and associated data in the cloud.
Fourth milestone: Lock and unlock commands are successful after owner sends them from mobile device or web interface, and the cloud service relays them.
Fifth milestone: Security!
Authenticate users and devices.
Ensure confidentiality and integrity by encrypting and hashing all network communications. (This might already come free if we use SSL/TLS from the start.)
etc.

