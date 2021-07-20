#Group Project ITT440 - GUI Code

import os
import sys
import time
import base64
import threading
from PyQt5.QtCore import Qt
from client import Chat_Client
from PyQt5 import QtCore, QtGui, QtWidgets

class loginWindow(QtWidgets.QDialog):
    def __init__(self):
        super(loginWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("LoginWindow")
        self.setStyleSheet("#LoginWindow{border-image:url(./images/style/login/login.png);}")
        self.setWindowIcon(QtGui.QIcon("./images/style/icon.png"))
        self.resize(432, 300)

        self.loginButton = QtWidgets.QPushButton(self)      
        self.loginButton.setGeometry(QtCore.QRect(118, 243, 220, 35))
        self.loginButton.setObjectName("login")
        self.loginButton.setStyleSheet("border-image:url(./images/style/login/loginbutton.png);")
        self.loginButton.clicked.connect(self.loginButtonClicked)

        self.registerButton = QtWidgets.QPushButton(self)   
        self.registerButton.setGeometry(QtCore.QRect(12, 250, 65, 25))
        self.registerButton.setObjectName("register")
        self.registerButton.setStyleSheet("border:none;") 
        self.registerButton.setCursor(Qt.PointingHandCursor)
        self.registerButton.clicked.connect(self.registerButtonClicked)

        self.userName = QtWidgets.QLineEdit(self)       
        self.userName.setGeometry(QtCore.QRect(118, 140, 220, 28))
        self.userName.setObjectName("username")
        self.userName.setPlaceholderText("USERNAME")
        self.userName.setMaxLength(20)

        self.password = QtWidgets.QLineEdit(self)   
        self.password.setGeometry(QtCore.QRect(118, 170, 220, 28))
        self.password.setObjectName("password")
        self.password.setPlaceholderText("PASSWORD")
        self.password.setMaxLength(20)
        self.password.setEchoMode(self.password.Password)
        self.constuserName = QtWidgets.QLineEdit(self)      
        self.constuserName.setGeometry(QtCore.QRect(42, 140, 75, 28))
        self.constuserName.setStyleSheet("border:none;")
        self.constuserName.setReadOnly(True)
        self.constpassword = QtWidgets.QLineEdit(self)
        self.constpassword.setGeometry(QtCore.QRect(42, 170, 75, 28))
        self.constpassword.setStyleSheet("border:none;")
        self.constpassword.setReadOnly(True)

        self.loginError = QtWidgets.QLineEdit(self)        
        self.loginError.setGeometry(QtCore.QRect(118, 205, 220, 28))
        self.loginError.setStyleSheet("background-color: rgb(255, 25, 255, 60);border:none;")
        self.loginError.setAlignment(QtCore.Qt.AlignCenter)
        self.loginError.setReadOnly(True)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("LoginWindow", "PyChat"))
        self.loginButton.setText(_translate("LoginWindow", "LOGIN"))
        self.registerButton.setText(_translate("LoginWindow", "REGISTER"))
        self.constuserName.setText(_translate("LoginWindow", "USERNAME"))
        self.constpassword.setText(_translate("LoginWindow", "PASSWORD"))
        self.loginError.setText(_translate("registerWindow", "Welcome to PyChat"))

    def loginButtonClicked(self):

        Username = self.userName.text()
        Password = self.password.text()
        if len(Username) == 0 or len(Password) == 0:
            self.loginError.setText("You have not entered your account or password!")
        else:
            client.login(Username, Password)
            while client.loginBack == None:
                pass
            flag = False
            if client.loginBack["info"] == "loginSucc":
                self.loginError.setStyleSheet("background-color: rgb(100, 255, 0, 60);border:none;")
                self.loginError.setText("Login Successfull")
                self.hide()
                self.chatWindow = chatWindow(Username)  
                self.chatWindow.show()
                self.chatWindow.main()
            elif client.loginBack["info"] == "loginFail":
                self.loginError.setText("Incorrect username or password! please enter again!")
            else:
                self.loginError.setText("The account has been logged in!")
            client.loginBack = None

    def registerButtonClicked(self):

        self.registerWindow = registerWindow()
        self.registerWindow.show()

class registerWindow(QtWidgets.QDialog):
    def __init__(self):
        super(registerWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("registerWindow")
        self.setStyleSheet("#registerWindow{border-image:url(./images/style/register/register.png);}")
        self.setWindowIcon(QtGui.QIcon("./images/style/icon.png"))
        self.resize(360, 330)

        self.userName = QtWidgets.QLineEdit(self)   
        self.userName.setGeometry(QtCore.QRect(118, 80, 220, 28))
        self.userName.setObjectName("username")
        self.userName.setPlaceholderText("USERNAME")
        self.userName.setMaxLength(20)

        self.password = QtWidgets.QLineEdit(self)    
        self.password.setGeometry(QtCore.QRect(118, 120, 220, 28))
        self.password.setObjectName("password")
        self.password.setPlaceholderText("PASSWORD")
        self.password.setMaxLength(20)
        self.password.setEchoMode(self.password.Password)

        self.passwordAgain = QtWidgets.QLineEdit(self)  
        self.passwordAgain.setGeometry(QtCore.QRect(118, 160, 220, 28))
        self.passwordAgain.setObjectName("passwordAgain")
        self.passwordAgain.setPlaceholderText("RE-ENTER PASSWORD")
        self.passwordAgain.setMaxLength(20)
        self.passwordAgain.setEchoMode(self.password.Password)

        self.constuserName = QtWidgets.QLineEdit(self)  
        self.constuserName.setGeometry(QtCore.QRect(30, 80, 87, 28))
        self.constuserName.setStyleSheet("border:none;")
        self.constuserName.setReadOnly(True)
        self.constpassword = QtWidgets.QLineEdit(self)
        self.constpassword.setGeometry(QtCore.QRect(30, 120, 87, 28))
        self.constpassword.setStyleSheet("border:none;")
        self.constpassword.setReadOnly(True)
        self.constpasswordAgain = QtWidgets.QLineEdit(self)
        self.constpasswordAgain.setGeometry(QtCore.QRect(30, 160, 87, 28))
        self.constpasswordAgain.setStyleSheet("border:none;")
        self.constpasswordAgain.setReadOnly(True)

        self.registerButton = QtWidgets.QPushButton(self)  
        self.registerButton.setGeometry(QtCore.QRect(118, 240, 220, 35))
        self.registerButton.setObjectName("register")
        self.registerButton.setStyleSheet("border-image:url(./images/style/register/registerbutton.png);")
        self.registerButton.clicked.connect(self.registerButtonClicked)

        self.registerError = QtWidgets.QLineEdit(self)     
        self.registerError.setGeometry(QtCore.QRect(118, 200, 220, 28))
        self.registerError.setStyleSheet("background-color: rgb(255, 25, 255, 60);border:none;")
        self.registerError.setAlignment(QtCore.Qt.AlignCenter)
        self.registerError.setReadOnly(True)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("registerWindow", "Register An PyChat Account"))
        self.constuserName.setText(_translate("registerWindow", "Username"))
        self.constpassword.setText(_translate("registerWindow", "Password"))
        self.constpasswordAgain.setText(_translate("registerWindow", "Re-Enter P/W"))
        self.registerButton.setText(_translate("registerWindow", "Fill the form"))
        self.registerError.setText(_translate("registerWindow", "Welcome to PyChat!"))

    def registerButtonClicked(self):

        Username = self.userName.text()
        password = self.password.text()
        passwordAgain = self.passwordAgain.text()
        if len(Username) == 0 or len(password) == 0 or len(passwordAgain) == 0:
            self.registerError.setText("You have not entered your account or password!")
        elif password != passwordAgain:
            self.registerError.setText("The password you entered is different twice!")
        else:
            client.register(Username, password)
            while client.registerBack == None:
                pass
            if client.registerBack["info"] == "rgtrSucc":
                self.registerError.setStyleSheet("background-color: rgb(100, 255, 0, 60);border:none;")
                self.registerError.setText("Registration Success! Please Log Back In!")
            else:
                self.registerError.setText("The Account Already Exists!")
            client.registerBack = None

class chatWindow(QtWidgets.QDialog):
    def __init__(self, name):
        self.Username = name
        super(chatWindow, self).__init__()
        self.setupUi()
        try:
            os.mkdir(self.Username)         
        except FileExistsError:
            pass

    def setupUi(self):

        self.setObjectName("PyChat")
        self.setStyleSheet("#PyChat{border-image:url(./images/style/PyChat/PyChat.png);}")
        self.setWindowIcon(QtGui.QIcon("./images/style/icon.png"))
        self.resize(1005, 463)

        self.grprecvText = QtWidgets.QTextEdit(self)        
        self.grprecvText.setGeometry(QtCore.QRect(200, 20, 670, 280))
        self.grprecvText.setObjectName("textRecv")
        self.grprecvText.setAlignment(QtCore.Qt.AlignTop)
        self.grprecvText.setStyleSheet("border-image:url(./images/style/PyChat/recvtext.png);")
        self.grprecvText.setReadOnly(True)

        self.prtrecvText1 = QtWidgets.QTextEdit(self)       
        self.prtrecvText1.setGeometry(QtCore.QRect(200, 20, 670, 280))
        self.prtrecvText1.setAlignment(QtCore.Qt.AlignTop)
        self.prtrecvText1.setStyleSheet("border-image:url(./images/style/PyChat/recvtext.png);")
        self.prtrecvText1.setReadOnly(True)
        self.prtrecvText1.hide()
        self.prtrecvText2 = QtWidgets.QTextEdit(self)      
        self.prtrecvText2.setGeometry(QtCore.QRect(200, 20, 670, 280))
        self.prtrecvText2.setAlignment(QtCore.Qt.AlignTop)
        self.prtrecvText2.setStyleSheet("border-image:url(./images/style/PyChat/recvtext.png);")
        self.prtrecvText2.setReadOnly(True)
        self.prtrecvText2.hide()
        self.prtrecvText3 = QtWidgets.QTextEdit(self)      
        self.prtrecvText3.setGeometry(QtCore.QRect(200, 20, 670, 280))
        self.prtrecvText3.setAlignment(QtCore.Qt.AlignTop)
        self.prtrecvText3.setStyleSheet("border-image:url(./images/style/MyChat/recvtext.png);")
        self.prtrecvText3.setReadOnly(True)
        self.prtrecvText3.hide()
        self.prtrecvText = [self.prtrecvText1, self.prtrecvText2, self.prtrecvText3]

        self.sendText = QtWidgets.QTextEdit(self)          
        self.sendText.setGeometry(QtCore.QRect(200, 335, 670, 85)) #
        self.sendText.setObjectName("textSend")
        self.sendText.setAlignment(QtCore.Qt.AlignTop)
        self.sendText.setStyleSheet("border-image:url(./images/style/PyChat/sendtext.png);")
        # self.sendText.keyPressEvent()
        self.destsend = 'all'

        self.sendtxtButton = QtWidgets.QPushButton(self)   
        self.sendtxtButton.setGeometry(QtCore.QRect(765, 425, 65, 27))
        self.sendtxtButton.setObjectName("txtsendButton")
        self.sendtxtButton.setStyleSheet("border-image:url(./images/style/PyChat/sendtxtbutton.png);")
        self.sendtxtButton.clicked.connect(self.txtsendButtonClicked)


        self.friendlistHeader = QtWidgets.QTextEdit(self)   
        self.friendlistHeader.setGeometry(QtCore.QRect(870, 120, 125, 25))
        self.friendlistHeader.setObjectName("friendlistHeader")
        self.friendlistHeader.setAlignment(QtCore.Qt.AlignTop)
        self.friendlistHeader.setStyleSheet("border-image:url(./images/style/PyChat/sendtext.png);")
        self.friendlistHeader.setReadOnly(True)

        self.friendlist = QtWidgets.QListWidget(self)      
        self.friendlist.setGeometry(QtCore.QRect(870, 140, 125, 280))
        self.friendlist.setObjectName("friendlist")
        self.friendlist.setStyleSheet("border-image:url(./images/style/PyChat/friendlist.png);")
        self.friendlist.doubleClicked.connect(self.friendlistDoubleClicked)
        self.friendlist.addItems(client.userlist)

        self.grpButton = QtWidgets.QPushButton(self)       
        self.grpButton.setGeometry(QtCore.QRect(0, 0, 200, 62))
        self.grpButton.setObjectName("grpButton")
        self.grpButton.setStyleSheet("border-image:url(./images/style/PyChat/nowfriendbutton.png);")
        self.grpButton.clicked.connect(self.grpbuttonClicked)

        self.destprtbutton = {}
        self.prtbutton1 = QtWidgets.QPushButton(self)       
        self.prtbutton1.setGeometry(QtCore.QRect(0, 62, 200, 62))
        self.prtbutton1.setStyleSheet("border-image:url(./images/style/PyChat/friendbutton.png);")
        self.prtbutton1.clicked.connect(self.prtbutton1Clicked)
        self.prtbutton2 = QtWidgets.QPushButton(self)       
        self.prtbutton2.setGeometry(QtCore.QRect(0, 124, 200, 62))
        self.prtbutton2.setStyleSheet("border-image:url(./images/style/PyChat/friendbutton.png);")
        self.prtbutton2.clicked.connect(self.prtbutton2Clicked)
        self.prtbutton3 = QtWidgets.QPushButton(self)      
        self.prtbutton3.setGeometry(QtCore.QRect(0, 186, 200, 62))
        self.prtbutton3.setStyleSheet("border-image:url(./images/style/PyChat/friendbutton.png);")
        self.prtbutton3.clicked.connect(self.prtbutton3Clicked)
        self.buttontotext = {}                             
        self.buttontotext[self.prtbutton1] = self.prtrecvText1
        self.buttontotext[self.prtbutton2] = self.prtrecvText2
        self.buttontotext[self.prtbutton3] = self.prtrecvText3
        self.prtbutton = [self.prtbutton1, self.prtbutton2, self.prtbutton3]

        self.fileButton = QtWidgets.QPushButton(self)       
        self.fileButton.setGeometry(QtCore.QRect(200, 300, 35, 35))
        self.fileButton.setStyleSheet("border-image:url(./images/style/PyChat/filebutton.png);")
        self.fileButton.clicked.connect(self.fileButtonClicked)

        self.imageButton = QtWidgets.QPushButton(self)      
        self.imageButton.setGeometry(QtCore.QRect(235, 300, 35, 35))
        self.imageButton.setStyleSheet("border-image:url(./images/style/PyChat/imagebutton.png);")
        self.imageButton.clicked.connect(self.imageButtonClicked)

        self.emojiButton = QtWidgets.QPushButton(self)     
        self.emojiButton.setGeometry(QtCore.QRect(270, 300, 35, 35))
        self.emojiButton.setStyleSheet("border-image:url(./images/style/PyChat/emojibutton.png);")
        self.emojiButton.clicked.connect(self.emojiButtonClicked)

        self.fileselect = QtWidgets.QFileDialog(self)      
        self.fileselect.setGeometry(QtCore.QRect(248, 341, 500, 62))

        self.emoji = QtWidgets.QTableWidget(self)          
        self.emoji.setGeometry(QtCore.QRect(270, 175, 120, 120))
        self.emoji.verticalHeader().setVisible(False)      
        self.emoji.horizontalHeader().setVisible(False)     
        self.emoji.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)   
        self.emoji.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)     
        self.emoji.setColumnCount(3)
        self.emoji.setRowCount(3)
        label = []
        for i in range(9):
            icon = QtWidgets.QLabel()
            icon.setMargin(4)
            movie = QtGui.QMovie()
            movie.setScaledSize(QtCore.QSize(30, 30))
            movie.setFileName("./images/emoji/"+str(i)+".gif")
            movie.start()
            icon.setMovie(movie)
            self.emoji.setCellWidget(int(i/3), i%3, icon)
            self.emoji.setColumnWidth(i%3, 40)          
            self.emoji.setRowHeight(int(i/3), 40)      
        self.emoji.hide()
        self.emoji.cellClicked.connect(self.emojiClicked)

        for i in self.prtbutton:
            self.destprtbutton[i] = None

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("PyChat", "PyChat"))
        self.sendtxtButton.setText(_translate("txtsendButton", "SEND"))
        self.grpButton.setText(_translate("grpButton", "PyChat Group"))
        self.friendlistHeader.setText(_translate("friendlistHeader", "Online Now"))

    def txtsendButtonClicked(self):

        text = self.sendText.toPlainText()
        if len(text):
            client.send_Msg(text, self.destsend)
            self.sendText.clear()


    def friendlistDoubleClicked(self):

        name = self.friendlist.currentItem().text()    
        if name == self.Username:
            return
        for i in self.prtbutton:
            if self.destprtbutton[i] == None or self.destprtbutton[i] == name:
                self.destprtbutton[i] = name
                i.setText(name)
                break

    def grpbuttonClicked(self):
        for i in self.prtrecvText:
            i.hide()
        self.grpButton.setStyleSheet("border-image:url(./images/style/PyChat/nowfriendbutton.png);")
        self.prtbutton1.setStyleSheet("border-image:url(./images/style/PyChat/friendbutton.png);")
        self.prtbutton2.setStyleSheet("border-image:url(./images/style/PyChat/friendbutton.png);")
        self.prtbutton3.setStyleSheet("border-image:url(./images/style/PyChat/friendbutton.png);")
        self.grprecvText.show()
        self.destsend = "all"
    def prtbutton1Clicked(self):
        if self.destprtbutton[self.prtbutton1] != None:
            for i in self.prtrecvText:
                i.hide()
            self.grpButton.setStyleSheet("border-image:url(./images/style/PyChat/friendbutton.png);")
            self.prtbutton1.setStyleSheet("border-image:url(./images/style/PyChat/nowfriendbutton.png);")
            self.prtbutton2.setStyleSheet("border-image:url(./images/style/PyChat/friendbutton.png);")
            self.prtbutton3.setStyleSheet("border-image:url(./images/style/PyChat/friendbutton.png);")
            self.grprecvText.hide()
            self.buttontotext[self.prtbutton1].show()
            self.destsend = self.destprtbutton[self.prtbutton1]
    def prtbutton2Clicked(self):
        if self.destprtbutton[self.prtbutton2] != None:
            for i in self.prtrecvText:
                i.hide()
            self.grpButton.setStyleSheet("border-image:url(./images/style/PyChat/friendbutton.png);")
            self.prtbutton1.setStyleSheet("border-image:url(./images/style/PyChat/friendbutton.png);")
            self.prtbutton2.setStyleSheet("border-image:url(./images/style/PyChat/nowfriendbutton.png);")
            self.prtbutton3.setStyleSheet("border-image:url(./images/style/PyChat/friendbutton.png);")
            self.grprecvText.hide()
            self.buttontotext[self.prtbutton2].show()
            self.destsend = self.destprtbutton[self.prtbutton2]
    def prtbutton3Clicked(self):
        if self.destprtbutton[self.prtbutton3] != None:
            for i in self.prtrecvText:
                i.hide()
            self.grpButton.setStyleSheet("border-image:url(./images/style/PyChat/friendbutton.png);")
            self.prtbutton1.setStyleSheet("border-image:url(./images/style/PyChat/friendbutton.png);")
            self.prtbutton2.setStyleSheet("border-image:url(./images/style/PyChat/friendbutton.png);")
            self.prtbutton3.setStyleSheet("border-image:url(./images/style/PyChat/nowfriendbutton.png);")
            self.grprecvText.hide()
            self.buttontotext[self.prtbutton3].show()
            self.destsend = self.destprtbutton[self.prtbutton3]

    def fileButtonClicked(self):
        # self.fileselect.show()
        fileinfo = self.fileselect.getOpenFileName(self, 'OpenFile', "e:/")
        print(fileinfo)
        filepath, filetype = os.path.splitext(fileinfo[0])
        filename = filepath.split("/")[-1]
        if fileinfo[0] != '':
            with open(fileinfo[0], mode='rb') as f:
                r = f.read()
                f.close()
            file_r = base64.encodebytes(r).decode("utf-8")
            client.send_Msg(file_r, self.destsend, filetype, filename)
        # while self.fileselect.getOpenFileName() == None:

    def imageButtonClicked(self):
        fileinfo = self.fileselect.getOpenFileName(self,'OpenFile',"e:/","Image files (*.jpg *.gif *.png)")
        print(fileinfo)
        filepath, filetype = os.path.splitext(fileinfo[0])
        filename = filepath.split("/")[-1]
        if fileinfo[0] != '':
            with open(fileinfo[0], mode='rb') as f:
                r = f.read()
                f.close()
            file_r = base64.encodebytes(r).decode("utf-8")
            client.send_Msg(file_r, self.destsend, filetype, filename)

    def emojiButtonClicked(self):
        self.emoji.show()

    def emojiClicked(self, row, column):
        client.send_Msg(row*3+column , self.destsend, "emoji")
        self.emoji.hide()



#MESSEGE BOX AREA


    def recv(self):

        while True:
            while len(client.usermsg):
                msg_recv = client.usermsg.pop()
                msgtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(msg_recv["time"]))
                if msg_recv["mtype"] == "msg":
                    msg_recv["msg"] = msg_recv["msg"].replace("\n","\n  ")
                    if msg_recv["name"] == self.Username:       
                        if msg_recv["destname"] == "all":
                            self.grprecvText.moveCursor(QtGui.QTextCursor.End)
                            self.grprecvText.setTextColor(Qt.blue)
                            self.grprecvText.insertPlainText(
                                " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                            self.grprecvText.setTextColor(Qt.black)
                            self.grprecvText.insertPlainText(msg_recv["msg"] + "\n")
                        else:
                            for i in self.prtbutton:
                                print(msg_recv["destname"])
                                print(self.destprtbutton[i])
                                if msg_recv["destname"] == self.destprtbutton[i]:
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.blue)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    self.buttontotext[i].setTextColor(Qt.black)
                                    self.buttontotext[i].insertPlainText(msg_recv["msg"] + "\n")
                    elif msg_recv["destname"] in (self.Username, "all"):       
                        if msg_recv["destname"] == "all":
                            self.grprecvText.moveCursor(QtGui.QTextCursor.End)
                            self.grprecvText.setTextColor(Qt.blue)
                            self.grprecvText.insertPlainText(
                                " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                            self.grprecvText.setTextColor(Qt.black)
                            self.grprecvText.insertPlainText(msg_recv["msg"] + "\n")
                        else:
                            for i in self.prtbutton:
                                if self.destprtbutton[i] == msg_recv["name"]:
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.blue)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    self.buttontotext[i].setTextColor(Qt.black)
                                    self.buttontotext[i].insertPlainText(msg_recv["msg"] + "\n")
                                    break
                                elif self.destprtbutton[i] == None:
                                    self.destprtbutton[i] = msg_recv["name"]
                                    i.setText(msg_recv["name"])
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.blue)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    self.buttontotext[i].setTextColor(Qt.black)
                                    self.buttontotext[i].insertPlainText(msg_recv["msg"] + "\n")
                                    break
                elif msg_recv["mtype"] == "emoji":
                    if msg_recv["name"] == self.Username:  
                        if msg_recv["destname"] == "all":
                            self.grprecvText.moveCursor(QtGui.QTextCursor.End)
                            self.grprecvText.setTextColor(Qt.blue)
                            self.grprecvText.insertPlainText(
                                " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                            path = "./images/emoji/"+ str(msg_recv["msg"]) +".gif"
                            tcursor = self.grprecvText.textCursor()
                            img = QtGui.QTextImageFormat()
                            img.setName(path)
                            img.setHeight(28)
                            img.setWidth(28)
                            tcursor.insertImage(img)
                            self.grprecvText.insertPlainText("\n")
                        else:
                            for i in self.prtbutton:
                                print(msg_recv["destname"])
                                print(self.destprtbutton[i])
                                if msg_recv["destname"] == self.destprtbutton[i]:
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.blue)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    path = "./images/emoji/" + str(msg_recv["msg"]) + ".gif"
                                    tcursor = self.buttontotext[i].textCursor()
                                    img = QtGui.QTextImageFormat()
                                    img.setName(path)
                                    img.setHeight(28)
                                    img.setWidth(28)
                                    tcursor.insertImage(img)
                                    self.buttontotext[i].insertPlainText("\n")
                    elif msg_recv["destname"] in (self.Username, "all"):  
                        if msg_recv["destname"] == "all":
                            self.grprecvText.moveCursor(QtGui.QTextCursor.End)
                            self.grprecvText.setTextColor(Qt.blue)
                            self.grprecvText.insertPlainText(
                                " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                            path = "./images/emoji/"+ str(msg_recv["msg"]) +".gif"
                            tcursor = self.grprecvText.textCursor()
                            img = QtGui.QTextImageFormat()
                            img.setName(path)
                            img.setHeight(28)
                            img.setWidth(28)
                            tcursor.insertImage(img)
                            self.grprecvText.insertPlainText("\n")
                        else:
                            for i in self.prtbutton:
                                if self.destprtbutton[i] == msg_recv["name"]:
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.blue)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    path = "./images/emoji/" + str(msg_recv["msg"]) + ".gif"
                                    tcursor = self.buttontotext[i].textCursor()
                                    img = QtGui.QTextImageFormat()
                                    img.setName(path)
                                    img.setHeight(28)
                                    img.setWidth(28)
                                    tcursor.insertImage(img)
                                    self.buttontotext[i].insertPlainText("\n")
                                    break
                                elif self.destprtbutton[i] == None:
                                    self.destprtbutton[i] = msg_recv["name"]
                                    i.setText(msg_recv["name"])
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.blue)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    path = "./images/emoji/" + str(msg_recv["msg"]) + ".gif"
                                    tcursor = self.buttontotext[i].textCursor()
                                    img = QtGui.QTextImageFormat()
                                    img.setName(path)
                                    img.setHeight(28)
                                    img.setWidth(28)
                                    tcursor.insertImage(img)
                                    self.buttontotext[i].insertPlainText("\n")
                                    break
                else:
                    if msg_recv["name"] == self.Username: 
                        if msg_recv["destname"] == "all":
                            self.grprecvText.moveCursor(QtGui.QTextCursor.End)
                            self.grprecvText.setTextColor(Qt.blue)
                            self.grprecvText.insertPlainText(
                                " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                            path = "./" + self.Username + "/" + msg_recv["fname"] + msg_recv["mtype"]
                            with open(path,"wb") as f:
                                f.write(base64.b64decode(msg_recv["msg"]))
                                f.close()
                            tcursor = self.grprecvText.textCursor()
                            img = QtGui.QTextImageFormat()
                            if msg_recv["mtype"] in (".png", ".gif", ".jpg"):
                                img.setName(path)
                                img.setHeight(100)
                                img.setWidth(100)
                                tcursor.insertImage(img)
                            else:
                                img.setName("./images/style/PyChat/filebutton.png")
                                img.setHeight(30)
                                img.setWidth(30)
                                tcursor.insertImage(img)
                                self.grprecvText.insertPlainText("The File Has Been Saved at" + path)
                            self.grprecvText.insertPlainText("\n")
                        else:
                            for i in self.prtbutton:
                                print(msg_recv["destname"])
                                print(self.destprtbutton[i])
                                if msg_recv["destname"] == self.destprtbutton[i]:
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.blue)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    path = "./" + self.Username + "/" + msg_recv["fname"] + msg_recv["mtype"]
                                    with open(path, "wb") as f:
                                        f.write(base64.b64decode(msg_recv["msg"]))
                                        f.close()
                                    tcursor = self.buttontotext[i].textCursor()
                                    img = QtGui.QTextImageFormat()
                                    if msg_recv["mtype"] in (".png", ".gif", ".jpg"):
                                        img.setName(path)
                                        img.setHeight(100)
                                        img.setWidth(100)
                                        tcursor.insertImage(img)
                                    else:
                                        img.setName("./images/style/MyChat/filebutton.png")
                                        img.setHeight(30)
                                        img.setWidth(30)
                                        tcursor.insertImage(img)
                                        self.buttontotext[i].insertPlainText("The File Has Been Saved at"+path)
                                    self.buttontotext[i].insertPlainText("\n")
                    elif msg_recv["destname"] in (self.Username, "all"): 
                        if msg_recv["destname"] == "all":
                            self.grprecvText.moveCursor(QtGui.QTextCursor.End)
                            self.grprecvText.setTextColor(Qt.blue)
                            self.grprecvText.insertPlainText(
                                " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                            path = "./" + self.Username + "/" + msg_recv["fname"] + msg_recv["mtype"]
                            with open(path, "wb") as f:
                                f.write(base64.b64decode(msg_recv["msg"]))
                                f.close()
                            tcursor = self.grprecvText.textCursor()
                            img = QtGui.QTextImageFormat()
                            if msg_recv["mtype"] in (".png", ".gif", ".jpg"):
                                img.setName(path)
                                img.setHeight(100)
                                img.setWidth(100)
                                tcursor.insertImage(img)
                            else:
                                img.setName("./images/style/MyChat/filebutton.png")
                                img.setHeight(30)
                                img.setWidth(30)
                                tcursor.insertImage(img)
                                self.grprecvText.insertPlainText("The File Has Been Saved at" + path)
                            self.grprecvText.insertPlainText("\n")
                        else:
                            for i in self.prtbutton:
                                if self.destprtbutton[i] == msg_recv["name"]:
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.blue)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    path = "./" + self.Username + "/" + msg_recv["fname"] + msg_recv["mtype"]
                                    with open(path, "wb") as f:
                                        f.write(base64.b64decode(msg_recv["msg"]))
                                        f.close()
                                    tcursor = self.buttontotext[i].textCursor()
                                    img = QtGui.QTextImageFormat()
                                    if msg_recv["mtype"] in (".png", ".gif", ".jpg"):
                                        img.setName(path)
                                        img.setHeight(100)
                                        img.setWidth(100)
                                        tcursor.insertImage(img)
                                    else:
                                        img.setName("./images/style/MyChat/filebutton.png")
                                        img.setHeight(30)
                                        img.setWidth(30)
                                        tcursor.insertImage(img)
                                        self.buttontotext[i].insertPlainText("The File Has Been Saved at"+path)
                                    self.buttontotext[i].insertPlainText("\n")
                                    break
                                elif self.destprtbutton[i] == None:
                                    self.destprtbutton[i] = msg_recv["name"]
                                    i.setText(msg_recv["name"])
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.blue)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    path = "./" + self.Username + "/" + msg_recv["fname"] + msg_recv["mtype"]
                                    with open(path, "wb") as f:
                                        f.write(base64.b64decode(msg_recv["msg"]))
                                        f.close()
                                    tcursor = self.buttontotext[i].textCursor()
                                    img = QtGui.QTextImageFormat()
                                    if msg_recv["mtype"] in (".png", ".gif", ".jpg"):
                                        img.setName(path)
                                        img.setHeight(100)
                                        img.setWidth(100)
                                        tcursor.insertImage(img)
                                    else:
                                        img.setName("./images/style/MyChat/filebutton.png")
                                        img.setHeight(30)
                                        img.setWidth(30)
                                        tcursor.insertImage(img)
                                        self.buttontotext[i].insertPlainText("The File Has Been Saved at"+path)
                                    self.buttontotext[i].insertPlainText("\n")
                                    break

            while len(client.sysmsg):
                msg_recv = client.sysmsg.pop()
                # msgtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(msg_recv["time"]))
                if msg_recv["info"] == "userlogin":
                    if msg_recv["name"] not in client.userlist:
                        client.userlist.append(msg_recv["name"])
                        self.friendlist.clear()
                        self.friendlist.addItems(client.userlist)
                elif msg_recv["info"] == "userexit":
                    if msg_recv["name"] in client.userlist:
                        client.userlist.remove(msg_recv["name"])
                        self.friendlist.clear()
                        self.friendlist.addItems(client.userlist)
                self.grprecvText.moveCursor(QtGui.QTextCursor.End)
                self.grprecvText.setTextColor(Qt.gray)
                self.grprecvText.insertPlainText("      "+msg_recv["msg"]+"\n")

    def main(self):
        func1 = threading.Thread(target=self.recv)
        func1.start()

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)  #
    client = Chat_Client(addr="localhost", port=14396)
    client.main()
    login = loginWindow()
    login.show()
    sys.exit(app.exec_())
