import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
import check_file_func


class MainWindow():
    def __init__(self, master):
        self.master = master
        master.title("Check files")

        self.master = master
        self.master.minsize(500,190) #(Height, Width)
        self.master.maxsize(500,190)
        check_file_func.center_window(self,500,190)
        
        self.master.protocol("WM_DELETE_WINDOW", lambda: check_file_func.ask_quit(self))

        self.btn_browse1 = tk.Button(self.master,width=15,height=1,text='Browse Folder...',command=lambda:var2.set(filedialog.askopenfilename()))
        self.btn_browse1.grid(row=0,column=0,columnspan=1,padx=(15,0),pady=(45,10),sticky=N+W)      
        self.lbl_filename = tk.Label(self.master,width=15,height=1,text='File Name:')
        self.lbl_filename.grid(row=1,column=0,columnspan=1,padx=(15,0),pady=(5,10),sticky=N+W)

        var1 = StringVar()
        var2 = StringVar()
        
        
        self.txt_browse1 = tk.Entry(self.master,textvariable=var1,width=50)
        self.txt_browse1.grid(row=0,column=1,rowspan=1,columnspan=1,padx=(25,0),pady=(45,10),sticky=N+E+W)
        self.txt_box = tk.Entry(self.master,textvariable=var2,width=50)
        self.txt_box.grid(row=1,column=1,rowspan=1,columnspan=1,padx=(25,0),pady=(5,10),sticky=N+E+W)

        self.btn_ckFiles = tk.Button(self.master,width=15,height=2,text='Check for folder',command=lambda:var1.set(filedialog.askdirectory()))
        self.btn_ckFiles.grid(row=4,column=0,columnspan=1,padx=(15,0),pady=(5,10),sticky=W)

        self.btn_close = tk.Button(self.master,width=15,height=2,text='Close Program',command= lambda: check_file_func.ask_quit(self))
        self.btn_close.grid(row=4,column=1,columnspan=1,padx=(15,0),pady=(0,0),sticky=E)
        

        
if __name__ == "__main__":
    root = tk.Tk()
    App = MainWindow(root)
    root.mainloop()
