

# Python 3.8.0


import os
import time
import datetime



target_file = "drill_python.py"
start_folder = "C:\\pyDrill\\"
for root, dirs, files in os.walk(start_folder):
    if target_file in files:
        print(root + '\\' + target_file)




print('\n\nHere is the list!\n')
for x in os.listdir('\\pyDrill'):
    print (x)




fName = 'drill_python.py'
fPath = 'C:\\pyDrill\\'
abPath = os.path.join(fPath, fName)
print('Path:\n')
print(abPath)




for file in os.listdir('C:\\pyDrill\\'):
    if file.endswith('.txt'):
        print(file, "last modified: %s" % time.ctime(os.path.getmtime(file)))
        



