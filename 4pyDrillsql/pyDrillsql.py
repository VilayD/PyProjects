

# python 3.8.0
# Using python & sqlite3 to create a database

import os
import sqlite3


# Creating table if not exists
def create_tbl():
    conn = sqlite3.connect('Drill2.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fileName TEXT \
            )")
    conn.commit()
    conn.close()  

    # Looking for file/s with .txt and adding name to col
def add_info(): 
    conn = sqlite3.connect('Drill2.db')
    with conn:
        cur = conn.cursor()
        for file in os.listdir('C:\\python_projects\\4pyDrillsql\\'):
            if file.endswith('.txt'):
                cur.execute("INSERT INTO tbl_files(col_fileName) VALUES(?)", [file])
                print("Here is the file name with .txt!")
                print(file)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tbl()
    add_info()
    



