import os
from tkinter import *
import tkinter as tk

import check_file_main

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
            messagebox.askokcancel("Quit", "Do you want to leave the program?")
            # This closes app
            self.master.destroy()
            os._exit(0)

if __name__ == "__main__":
    pass



