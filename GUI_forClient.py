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
                            text="Please Login to a enter the GROUP", 
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

        def goAhead(self, username, room_id=0):
        self.name = username
        self.server.send(str.encode(username))
        time.sleep(0.1)
        self.server.send(str.encode(room_id))
        
        self.login.destroy()
        self.layout()

        rcv = threading.Thread(target=self.receive) 
        rcv.start()


    def layout(self):
        self.Window.deiconify()
        self.Window.title("GROUP")
        self.Window.resizable(width=False, height=False)
        self.Window.configure(width=470, height=550, bg="#17202A")
        self.chatBoxHead = tk.Label(self.Window, 
                                    bg = "#17202A", 
                                    fg = "#EAECEE", 
                                    text = self.name , 
                                    font = "Helvetica 13 bold", 
                                    pady = 5)

        self.chatBoxHead.place(relwidth = 1)

        self.line = tk.Label(self.Window, width = 450, bg = "#ABB2B9") 
		
        self.line.place(relwidth = 1, rely = 0.07, relheight = 0.012) 
		
        self.textCons = tk.Text(self.Window, 
                                width=20, 
                                height=2, 
                                bg="#17202A", 
                                fg="#EAECEE", 
                                font="Helvetica 13", 
                                padx=5, 
                                pady=5) 
		
        self.textCons.place(relheight=0.745, relwidth=1, rely=0.08) 
		
        self.labelBottom = tk.Label(self.Window, bg="#ABB2B9", height=80) 
		
        self.labelBottom.place(relwidth = 1, 
							    rely = 0.8) 
		
        self.entryMsg = tk.Entry(self.labelBottom, 
                                bg = "#2C3E50", 
                                fg = "#EAECEE", 
                                font = "Helvetica 13")
        self.entryMsg.place(relwidth = 0.74, 
							relheight = 0.03, 
							rely = 0.008, 
							relx = 0.011) 
        self.entryMsg.focus()

        self.buttonMsg = tk.Button(self.labelBottom, 
								text = "Send", 
								font = "Helvetica 11 bold", 
								width = 20, 
								bg = "#ABB2B9", 
								command = lambda : self.sendButton(self.entryMsg.get())) 
        self.buttonMsg.place(relx = 0.77, 
							rely = 0.008, 
							relheight = 0.03, 
							relwidth = 0.22) 


        self.labelFile = tk.Label(self.Window, bg="#ABB2B9", height=70) 
		
        self.labelFile.place(relwidth = 1, 
							    rely = 0.9) 
		
        self.fileLocation = tk.Label(self.labelFile, 
                                text = "Add File",
                                bg = "#2C3E50", 
                                fg = "#EAECEE", 
                                font = "Helvetica 13")
        self.fileLocation.place(relwidth = 0.65, 
                                relheight = 0.03, 
                                rely = 0.008, 
                                relx = 0.011) 

        self.browse = tk.Button(self.labelFile, 
								text = "Browse", 
								font = "Helvetica 11 bold", 
								width = 13, 
								bg = "#ABB2B9", 
								command = self.browseFile)
        self.browse.place(relx = 0.67, 
							rely = 0.008, 
							relheight = 0.03, 
							relwidth = 0.15) 

        self.sengFileBtn = tk.Button(self.labelFile, 
								text = "Send", 
								font = "Helvetica 11 bold", 
								width = 13, 
								bg = "#ABB2B9", 
								command = self.sendFile)
        self.sengFileBtn.place(relx = 0.84, 
							rely = 0.008, 
							relheight = 0.03, 
							relwidth = 0.15)
    

        self.textCons.config(cursor = "arrow")
        scrollbar = tk.Scrollbar(self.textCons) 
        scrollbar.place(relheight = 1, 
						relx = 0.974)

        scrollbar.config(command = self.textCons.yview)
        self.textCons.config(state = tk.DISABLED)


    def browseFile(self):
        self.filename = filedialog.askopenfilename(initialdir="/", 
                                    title="Select a file",
                                    filetypes = (("Text files", 
                                                "*.txt*"), 
                                                ("all files", 
                                                "*.*")))
        self.fileLocation.configure(text="File Opened: "+ self.filename)
