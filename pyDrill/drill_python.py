

# Python 3.8.0


import os
import time
import datetime



def file_info():
    # Print file path
    target_file = "drill_python.py"
    start_folder = "C:\\pyDrill\\"
    for root, dirs, files in os.walk(start_folder):
        if target_file in files:
            print(root + '\\' + target_file)



    # Iterate through start folder to check for .txt files and print it
    print("\nLast Modified time for text files in this directory!\n")
    for file in os.listdir(start_folder):
        if file.endswith('.txt'):
            abPath = os.path.join(start_folder, file)   
            print(file, time.ctime(os.path.getmtime(file)))
        
        

if __name__ == "__main__":
    file_info()
        



