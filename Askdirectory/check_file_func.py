#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.8.0
#
# Author:       Phanvilay Davis
#
# Purpose:      Tkinter GUI module and functions to create gui with filedialog.askdirectory 
#               
#
# Tested OS:    This code was written and tested to work with Windows 10.


import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog

import file_dialog

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo    
    
        
def ask_quit(self): # Catches if use wants to really close app.
    messagebox.askokcancel("Quit", "Do you want to leave the program?")
    # This closes app
    self.master.destroy()
    os._exit(0)

if __name__ == "__main__":
    pass



