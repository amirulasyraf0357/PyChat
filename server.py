#Group Project ITT440 - Server Code

import time
import queue
import socket
import sqlite3
import threading

class Chat_Server(object):
    def __init__(self, addr="", port=""): #this module responsible for creating socket and handling database
        self.addr = addr
        self.port = port
        self.connections = []
        self.name = {}
        self.nametoconn = {}
        self.userlist = []
        self.queue = queue.Queue()

        self.dbconn = sqlite3.connect('UserInfo.db') #database name
        self.dbcursor = self.dbconn.cursor()
        #database attribute
        #if database file not exits, execute() will create a new ones
        self.dbcursor.execute('''CREATE TABLE IF NOT EXISTS USERINFO
               (USERNAME    VARCHAR(20) PRIMARY KEY     NOT NULL,
                PASSWORD    VARCHAR(20)                 NOT NULL,
                LASTLOGIN   VARCHAR(50)                 NOT NULL,
                STATUS      INT(1)                      NOT NULL
                               );''')
        self.dbcursor.execute("UPDATE USERINFO set STATUS = 0")
        self.dbconn.commit()

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP socket
        print("Successfully created socket")

        self.s.bind((self.addr, self.port))                               
        print("Socket bind to "+str(self.port)) #socket bind

    def portlisten(self): #Listen for connections 
        
        self.s.listen(10)
        print("Waiting for chat's client to connect...")
        while True:
            conn, address = self.s.accept() #socket accept conenction from client
            print("Successfully establish connection to chat's client ")        
            conn.settimeout(0.000001)
            add = address[0] + ":" + str(address[1])
            self.connections.append(conn)       
            self.name[add] = add

    def msg_queue(self): #message queue

        while True:
            for c in self.connections:
                try:
                    msg_recv = eval(c.recv(1024))
                except socket.timeout:
                    continue
                except SyntaxError:
                    pass
                except socket.error as err:     #10053 – Software caused connection abort //10054 – connection reset by peer
                    if err.errno == 10053 or err.errno == 10054:
                        self.remove_connection(c)
                except ValueError:
                    pass
                else:
                    addr = c.getpeername()
                    self.queue.put((addr, msg_recv, c))
                    if msg_recv["type"] == "msglen":
                        length = msg_recv["len"]
                        time.sleep(length * 0.0000001)
                        mlen = 0
                        while msg_recv["type"] != "usermsg":
                            try:
                                msg_recv = "".encode()
                                while mlen < length:        #this part will mark sure message is coming
                                    try:
                                        msg_recv_ = c.recv(length)
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
                            except socket.error as err:  # 10053 – Software caused connection abort //10054 – connection reset by peer
                                if err.errno == 10053 or err.errno == 10054:
                                    self.remove_connection(c)
                            except ValueError:
                                pass
                        self.queue.put((addr, msg_recv, c))

    def loginPychat(self, msg_recv, addr): #Login to PyChat

        Username = msg_recv["name"]
        self.dbcursor.execute("SELECT * from USERINFO where USERNAME = \"{Uname}\"".format(Uname = Username)) 
        Userinfo = self.dbcursor.fetchone()

        if Userinfo == None or Userinfo[1] != msg_recv["password"]:       
            flag = False
            back = {"type": "loginBack",
                    "info": "loginFail"}
        elif Userinfo[3] == 1:
            flag = False
            back = {"type": "loginBack",
                    "info": "loginAlready"}
        else:
            flag = True
            address = addr[0] + ":" + str(addr[1])

            self.name[address] = Username
            self.userlist.append(Username)
            self.lastlogintime = Userinfo[2]
            self.dbcursor.execute("UPDATE USERINFO set LASTLOGIN = {logintime}, STATUS = 1 where USERNAME=\"{Uname}\"".format(
                logintime = time.time(),          
                Uname = Username))
            self.dbconn.commit()
            back = {"type": "loginBack",
                    "info": "loginSucc",
                    "userlist": self.userlist}
            forward = {"type": "sysmsg",
                       "info": "userlogin",
                       "name": Username,
                       "time": time.time(),
                       "msg": "Welcome {name} to PyChat~".format(name=Username)}

        for c in self.connections:
            c_addr = c.getpeername()
            if c_addr == addr:
                if flag:
                    self.nametoconn[self.name[address]] = c
                c.send(str(back).encode())
            elif flag:
                c.send(str(forward).encode())

    def registerPychat(self, msg_recv, addr): #Register PyChat

        Username = msg_recv["name"]
        self.dbcursor.execute("SELECT * from USERINFO where USERNAME=\"{Uname}\"".format(Uname = Username))
        Userinfo = self.dbcursor.fetchone()

        if Userinfo == None:    
            self.dbcursor.execute("INSERT INTO USERINFO (USERNAME, PASSWORD, LASTLOGIN, STATUS) \
            VALUES (\"{Uname}\", \"{Passwd}\", \"Never\", 0)".format(Uname = Username, Passwd = msg_recv["password"]))
            self.dbconn.commit()

            self.name[addr] = Username
            self.lastlogintime = "Never"
            back = {"type": "rgtrBack",
                    "info": "rgtrSucc"}
        else:
            back = {"type": "rgtrBack",
                    "info": "rgtrFail"}

        for c in self.connections:
            c_addr = c.getpeername()
            if c_addr == addr:
                c.send(str(back).encode())

    def remove_connection(self, conn): #The user exits, cut the connection, so the system need to remove it otherwise the user will stay in chat 

        try:
            self.connections.remove(conn)
        except ValueError:
            pass
        address = conn.getpeername()
        addr = address[0] + ":" + str(address[1])
        Username = self.name[addr]
        self.name.pop(addr)    #remove user from the list
        if Username in self.userlist:
            self.userlist.remove(Username)
        dbconn1 = sqlite3.connect('userinfo.db') #connect to databse
        dbcursor1 = dbconn1.cursor()#choose which perimeter to change
        dbcursor1.execute("UPDATE USERINFO set STATUS=0 where USERNAME=\"{Uname}\"".format(Uname=Username))
        dbconn1.commit() #commit change
        back = {"type": "sysmsg",
                "info": "userexit",
                "name": Username,
                "time": time.time(),
                "msg": "{name} Exits PyChat~".format(name=Username)}
        for c in self.connections:
            c.send(str(back).encode())

    def msg_forward(self, msg_forward, addr): #determine where to foward the message whether to private chat or public chat
        address = addr[0] + ":" + str(addr[1])
        if msg_forward["destname"] == "all": #public chat
            for c in self.connections:
                print("forward     ")
                c.send(str(msg_forward).encode())
        else:
            self.nametoconn[msg_forward["destname"]].send(str(msg_forward).encode()) #private chat
            self.nametoconn[msg_forward["name"]].send(str(msg_forward).encode())
            print("forward     ")

    def run(self): #threading

        func1 = threading.Thread(target=self.portlisten) #threading use for module portliste()
        func2 = threading.Thread(target=self.msg_queue) #threading use for module msg_queue()
        func1.start()
        func2.start()
        while True:
            if self.queue.empty():
                continue
            addr, msg, conn = self.queue.get() #sys message received
            if msg["type"] == "login": #if string is login
                self.loginPychat(msg, addr)
            elif msg["type"] in ("usermsg", "msglen"): #if it a message
                self.msg_forward(msg, addr)
            elif msg["type"] == "register": #if it a command to register
                self.registerPychat(msg, addr)
                
    def __del__(self):
        self.s.close() #close socket
        self.dbconn.close() #close database

if __name__ == '__main__':
    server = Chat_Server(addr="192.168.56.101", port=8888)
    server.run() #when server start, it will start with run() module

