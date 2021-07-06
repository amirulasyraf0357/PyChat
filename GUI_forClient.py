import os
import sys
import time
import base64
import threading
from PyQt5.QtCore import Qt
from Client import Chat_Client
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