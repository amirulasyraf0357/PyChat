import socket
import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkinter import filedialog
import time
import threading
import os

class GUI:
    
    def __init__(self, ipaddr, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((ipaddr, port))

        self.Window = tk.Tk()
        self.Window.withdraw()

        self.login = tk.Toplevel()

        self.login.title("Login")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=350)

        self.pls = tk.Label(self.login, 
                            text="Please Login to a enter the chatroom", 
                            justify=tk.CENTER,
                            font="Helvetica 13 bold")

        self.pls.place(relheight=0.15, relx=0.2, rely=0.07)

        self.userLabelName = tk.Label(self.login, text="USERNAME: ", font="Helvetica 13")
        self.userLabelName.place(relheight=0.2, relx=0.1, rely=0.25)

        self.userEntryName = tk.Entry(self.login, font="Helvetica 13")
        self.userEntryName.place(relwidth=0.4 ,relheight=0.1, relx=0.35, rely=0.30)
        self.userEntryName.focus()

        self.roomLabelName = tk.Label(self.login, text="ROOM PASSWORD: ", font="Helvetica 13")
        self.roomLabelName.place(relheight=0.2, relx=0.1, rely=0.40)

        self.roomEntryName = tk.Entry(self.login, font="Helvetica 13", show="*")
        self.roomEntryName.place(relwidth=0.4 ,relheight=0.1, relx=0.35, rely=0.45)
        
        self.go = tk.Button(self.login, 
                            text="NEXT", 
                            font="Helvetica 13 bold", 
                            command = lambda: self.goAhead(self.userEntryName.get(), self.roomEntryName.get()))
        
        self.go.place(relx=0.35, rely=0.62)

        self.Window.mainloop()
        