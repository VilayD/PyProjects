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
import sqlite3
import time
import shutil

import final_drill
import final_drill_gui


def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo
    
    
def ask_quit(self):# Catches if use wants to really close app.
    messagebox.askokcancel("Quit", "Do you want to leave the program?")
    # This closes app
    self.master.destroy()
    os._exit(0)

def Sel_Source(self):# Browse for the source folder
    self.sourcePath.set(filedialog.askdirectory())

def Sel_Destination(self):# Browse for destination folder
    self.destinationPath.set(filedialog.askdirectory())

def moveTextfiles(self):# Finds .txt files from source and move them to destination
    # Assigning variables for source and destination paths
    self.sourceDir = self.sourcePath.get()
    self.destinationDir = self.destinationPath.get()

    numOf_txtFiles = 0
    numOf_txtFiles_Moved = 0

    if os.path.exists(self.sourceDir)and os.path.exists(self.destinationDir):


        movedFiles = [] # Record what files were moved
        
        for f in os.listdir(self.sourceDir):
            abPath = os.path.join(self.sourceDir, f)

            # Print text files
            if f.endswith('.txt'):
                numOf_txtFiles += 1
                epochTime = os.path.getmtime(abPath)# os.path.getmtime() gets the seconds since January 1, 1970
                modTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epochTime))# time.strftime() converts epoch time to readable time

                # Move files and add to db
                shutil.move(abPath, self.destinationDir)
                addTo_db(self,f,modTime)
                numOf_txtFiles_Moved += 1 
                movedFiles.append(f)

        # Show files
        if numOf_txtFiles_Moved > 0:
            showDB_Files(self,movedFiles)
            movedFiles.clear()

        # Prints string text that shows source and destination folders if number of text files is more then 0.
        if (numOf_txtFiles > 0):
            print("There are {} files moved from {}\nto {}.".format(numOf_txtFiles_Moved, self.sourceDir, self.destinationDir))
        else:
            print("There are no .txt files in {}.".format(self.sourceDir))
    else:
        print("Please Enter valid source path and destination path!")
    


# Create the database table
def create_tbl(self):
    conn = sqlite3.connect('TextFiles.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS TextFiles ( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            fileName VARCHAR, \
            dateModified VARCHAR \
            )")
        conn.commit()
    conn.close()

# Add if it's a new file
def addTo_db(self,fileName,modTime):
    conn = sqlite3.connect('TextFiles.db')
    with conn:
        cur = conn.cursor()
        cur.execute("\
            SELECT COUNT(fileName) FROM TextFiles\
            WHERE fileName = '{}'".format(fileName))
        count = cur.fetchall()[0][0]
        if(count > 0):
            print("{} already exists!".format(fileName))
        else:
            cur.execute("\
                INSERT INTO TextFiles\
                (fileName, dateModified)\
                VALUES\
                (?,?)", (fileName, modTime))
            print("{} has been added to database.".format(fileName))
        conn.commit()
    conn.close()
            
# Shows files that was moved in database
def showDB_Files(self,movedFiles):
    print("Files that was moved")

    conn = sqlite3.connect('TextFiles.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT fileName, dateModified FROM TextFiles")

        # Display data
        for i in cur.fetchall():
            string = ""
            if i[0] in movedFiles:
                for n in i:
                    string += "{} \t".format(n)
                print("{}".format(string))
        conn.commit()
    conn.close()
            

if __name__ == "__main__":
    pass
