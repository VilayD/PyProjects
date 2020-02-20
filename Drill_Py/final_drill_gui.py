#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.8.0
#
# Author:       Phanvilay Davis
#
# Purpose:      Function for GUI module using Tkinter Parent and Child relationships.


import os
from tkinter import *
import tkinter as tk

# Importing other modules that relates to this GUI
import final_drill
import final_drill_func

def load_gui(self):
        
    """
    Define the default tkinter widgets and their initial
    configuration and place them using the grid geometry.
    Use grid as it offers the best control
    for pacing the widgets.
    """

    # ========= Buttons =========
    self.btn_browse1 = tk.Button(self.master,width=18,height=1,text='Browse Source...',command= lambda: final_drill_func.Sel_Source(self))
    self.btn_browse1.grid(row=0,column=0,columnspan=1,padx=(15,0),pady=(35,10),sticky=N+W)      
    self.btn_browse2 = tk.Button(self.master,width=18,height=1,text='Browse Destination...',command= lambda: final_drill_func.Sel_Destination(self))
    self.btn_browse2.grid(row=1,column=0,columnspan=1,padx=(15,0),pady=(5,10),sticky=N+W)
    self.btn_ckFiles = tk.Button(self.master,width=18,height=2,text='Check for file...',command= lambda: final_drill_func.moveTextfiles(self))
    self.btn_ckFiles.grid(row=4,column=0,columnspan=1,padx=(15,0),pady=(10,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=18,height=2,text='Close Program',command= lambda: final_drill_func.ask_quit(self))
    self.btn_close.grid(row=4,column=1,columnspan=1,padx=(15,0),pady=(0,0),sticky=E)
       
    # ========= Text Boxes =========
    # Assigning var to StringVar for source path.
    self.sourcePath = StringVar()
    self.txt_browse1 = tk.Entry(self.master,textvariable=self.sourcePath,width=52)
    self.txt_browse1.grid(row=0,column=1,rowspan=1,columnspan=1,padx=(15,5),pady=(35,10),sticky=N+E+W)
    # Assigning var to StringVar for destination path.
    self.destinationPath = StringVar()
    self.txt_browse2 = tk.Entry(self.master,textvariable=self.destinationPath,width=52)
    self.txt_browse2.grid(row=1,column=1,rowspan=1,columnspan=1,padx=(15,5),pady=(5,10),sticky=N+E+W)

      


if __name__ == "__main__":
    pass
