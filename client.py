#Group Project ITT440 - Client Code

import time
import queue
import socket
import threading #import time, socket,threading modules

class Chat_Client(object):
    def __init__(self, addr="", port=""):

        self.addr = addr
        self.port = port
        self.username = None
        self.queue = queue.Queue()
        self.status = True
        self.loginStatus = False
        self.loginBack = None
        self.registerBack = None
        self.userlist = []
        self.usermsg = []
        self.sysmsg = []

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          #using tcp

        try:
            self.s.connect((self.addr, self.port)) #connect socket
            self.s.settimeout(0.000001)
        except socket.error as err:
            if err.errno == 10061:
                print("Connection with {addr}:{port} refused".format(addr=self.addr, port=self.port))
                return
            else:
                raise
        else:
            print("initial successfully!")

    def register(self, name, password): #Register

        self.s.send(str({"type": "register",
                                "name": name,
                                "password": password,
                                "time": time.time()}).encode())

    def login(self, name, password): #Login

        self.username = name
        self.s.send(str({"type": "login",
                                "name": name,
                                "password": password,
                                "time": time.time()}).encode())

    def send_Msg(self, msg_send, destname, mtype = "msg", fname = ""): #Send message

        a = str({"type": "usermsg",
                        "mtype": mtype,
                        "destname": destname,
                        "fname": fname,
                        "name": self.username,
                        "time": time.time(),
                        "msg": msg_send}).encode()
        constlen = len(a)

        self.s.send(str({"type": "msglen",
                                "destname": destname,
                                "name": self.username,
                                "len": constlen}).encode())
        print("send     ")
        print(str({"type": "msglen",
                          "destname": destname,
                          "name": self.username,
                          "len": constlen}).encode())
        time.sleep(0.01)
        self.s.send(a)

    def receive_msg(self): #Receive message

        while self.status:
            try:
                msg_recv = eval(self.s.recv(1024))
            except socket.timeout:
                pass
            except socket.error as err:
                if err.errno == 10053:
                    print("Software caused connection abort ")
                    self.status = False
            else:
                if msg_recv["type"] == "msglen":
                    self.queue.put(msg_recv)
                    print("recv             ")
                    length = msg_recv["len"]
                    mlen = 0
                    while msg_recv["type"] != "usermsg":
                        try:
                            msg_recv = "".encode()

                            while mlen < length:
                                try:
                                    msg_recv_ = self.s.recv(length)
                                    msg_recv = msg_recv + msg_recv_
                                    mlen = mlen + len(msg_recv_)
                                    msg_recv = eval(msg_recv)
                                    time.sleep(length * 0.00000001)
                                except socket.timeout:
                                    continue
                                except SyntaxError:
                                    continue
                                else:
                                    break
                        except socket.timeout:
                            continue
                        except socket.error as err:
                            if err.errno == 10053:
                                print("Software caused connection abort ")
                                self.status = False
                    self.queue.put(msg_recv)
                    print("recv             ")
                else:
                    self.queue.put(msg_recv)
                    print("recv             ")

    def handle_msg(self): #Error message handling

        while True:
            msg = self.queue.get()
            print("handle              ",end='')

            if msg["type"] == "loginBack":
                self.loginBack = msg
                if msg["info"] == "loginSucc":
                    self.userlist = msg["userlist"]
            elif msg["type"] == "rgtrBack":
                self.registerBack = msg
            elif msg["type"] == "usermsg":
                self.usermsg.append(msg)
            elif msg["type"] == "sysmsg":
                self.sysmsg.append(msg)

    def main(self): #threading
        
        func1 = threading.Thread(target=self.receive_msg) #receive_msg() module
        func2 = threading.Thread(target=self.handle_msg) #handle_msg() module
        func1.start()
        func2.start()

    def __del__(self):
        self.s.close() #close socket connection

if __name__ == '__main__':
    client = Chat_Client(addr="192.168.56.101", port=8888)
    client.main() #start main modules
    client.login("0", "0")