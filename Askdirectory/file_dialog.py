# !/usr/bin/python
"""
    #!/usr/bin/python
    It's a recommended way, proposed in documentation:
    2.2.2. Executable Python Scripts.
    In a Unix-like operating system, the program loader
    takes the presence of these two characters as an
    indication that the file is a script, and tries to
    execute that script using the interpreter specified
    by the rest of the first line in the file.
"""
# -*- coding: utf-8 -*-
"""
    # -*- coding: utf-8 -*-
    This sets the charset if it is present on the first two lines of the file.
    this is Syntax to declare the encoding of a Python source file. It's discussed
    in PEP 0263 - Defining Python Source Code Encodings.
    https://www.python.org/dev/peps/pep-0263/
"""
##
# Python Ver:   3.8.0
#
# Author:       Phanvilay Davis
#
# Purpose:      Tkinter GUI module to create a search directory.
#
# Tested OS:    This code was written and tested to work with Windows 10.


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

        #define master frame configuration
        self.master = master
        self.master.minsize(500,190) #(Height, Width)
        self.master.maxsize(500,190)
        
        #This CenterWindow method will center our app on the user's screen
        check_file_func.center_window(self,500,190)
        
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: check_file_func.ask_quit(self))

        # Creating variables to assign the StringVar for file path.
        file = StringVar()
        
        """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
        Use grid as it offers the best control
        for pacing the widgets.
        """
        self.btn_browse1 = tk.Button(self.master,width=15,height=1,text='Browse...',command=lambda:file.set(filedialog.askdirectory()))
        self.btn_browse1.grid(row=0,column=0,columnspan=1,padx=(15,0),pady=(45,10),sticky=N+W)      
        self.btn_browse2 = tk.Button(self.master,width=15,height=1,text='Browse')
        self.btn_browse2.grid(row=1,column=0,columnspan=1,padx=(15,0),pady=(5,10),sticky=N+W)
        
        # Create a entry box and add the file path from the askdirectory.
        self.txt_browse1 = tk.Entry(self.master,textvariable=file,width=55)
        self.txt_browse1.grid(row=0,column=1,rowspan=1,columnspan=1,padx=(25,0),pady=(45,10),sticky=N+E+W)
        self.txt_box = tk.Entry(self.master,textvariable=file,width=55)
        self.txt_box.grid(row=1,column=1,rowspan=1,columnspan=1,padx=(25,0),pady=(5,10),sticky=N+E+W)

        self.btn_ckFiles = tk.Button(self.master,width=15,height=2,text='Check for folder...')
        self.btn_ckFiles.grid(row=4,column=0,columnspan=1,padx=(15,0),pady=(5,10),sticky=W)

        self.btn_close = tk.Button(self.master,width=15,height=2,text='Close Program',command= lambda: check_file_func.ask_quit(self))
        self.btn_close.grid(row=4,column=1,columnspan=1,padx=(15,0),pady=(0,0),sticky=E)
        

        
if __name__ == "__main__":
    root = tk.Tk()
    App = MainWindow(root)
    root.mainloop()
