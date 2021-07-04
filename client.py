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

while True:
    sockListen = [sys.stdin, Server]
    sockRead, sockWrite, sockError = select.select(sockListen, [], [])
    for socket in read_socket:
        if socket == Server:
            message = socket.recv(1024)
            
            print(str(message.decode()))

            if str(message.decode()) == "FILE":
                fileName = socket.recv(1024).decode()
                fileLen = socket.recv(1024).decode()
                sendUser = socket.recv(1024).decode()

                if os.path.exists(fileName):
                    os.remove(fileName)

                print(fileName, fileLen, sendUser)

                total = 0
                with open(fileName, 'wb') as file:
                    while str(total) != fileLen:
                        message = socket.recv(1024)
                        total = total + len(message)     
                        file.write(message)
                print("<" + str(sendUser) + "> " + fileName + " sent")
                       
            else:
                print(message.decode())

        else:
            message = sys.stdin.readline()

            if str(message) == "FILE\n":
                fileName = input("Enter the file name : ")
                Server.send("FILE".encode())
                time.sleep(0.1)
                Server.send(str("client_" + fileName).encode())
                time.sleep(0.1)
                server.send(str(os.path.getsize(fileName)).encode())
                time.sleep(0.1)

                file = open(fileName, "rb")
                message = file.read(1024)
                while message:
                    server.send(message)
                    message = file.read(1024)
                sys.stdout.write("<You>")
                sys.stdout.write("File sent successfully\n")
                sys.stdout.flush()

            else:
                Server.send(message.encode())
                sys.stdout.write("<You>")
                sys.stdout.write(message)
                sys.stdout.flush()
Server.close()