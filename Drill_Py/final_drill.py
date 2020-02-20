# !/usr/bin/python

# -*- coding: utf-8 -*-

#
# Python Ver:   3.8.0
#
# Author:       Phanvilay Davis
#
# Purpose:      To create a working GUI with these conditions:
#               - Two buttons to pick source folder and destination folder.
#               - Show these paths in text fields
#               - Execute button - Search for .txt in source, cut and move to destination.
#               - Record the files that were moved and time stamps in DB
#               - Print text files and time stamps to the console.
#
# Tested OS:    This code was written and tested to work with Windows 10.



import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import shutil
import time

import final_drill_func
import final_drill_gui


class MainWindow():
    def __init__(self, master):
        self.master = master
        master.title("Move text files")

        # Define master frame configuration
        self.master = master
        self.master.minsize(500,190) #(Height, Width)
        self.master.maxsize(500,190)
        #This CenterWindow method will center our app on the user's screen
        final_drill_func.center_window(self,500,190)

        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: final_drill_func.ask_quit(self))

        self.sourcePath = StringVar()
        self.destinationPath = StringVar()
        

        # Creating a db
        final_drill_func.create_tbl(self)

        # Calling for gui
        final_drill_gui.load_gui(self)
        

        
if __name__ == "__main__":
    root = tk.Tk()
    App = MainWindow(root)
    root.mainloop()

        

        
