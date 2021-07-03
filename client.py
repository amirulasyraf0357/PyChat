import socket
import select
import sys
import time
import os

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IPaddr = ""
PORTaddr = 8888

Server.connect((IPaddr, PORTaddr))
print("Connected To server")

IDuser = input("Please enter user ID : ")
IDroom = input("Please enter room ID : ")

Server.send(str.encode(IDuser))
time.sleep(0.1)
Server.send(str.encode(IDroom))