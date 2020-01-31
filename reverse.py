import os, shutil
import time
import GUI

start_time = time.process_time()
def reverse(dirPath, folderNames):
    for x in list(folderNames):
        if os.path.exists(dirPath+"\\"+x):
            for file in os.listdir(dirPath+"\\"+x):
                shutil.move(dirPath+"\\"+x+"\\"+file, dirPath+"\\"+file)
            os.rmdir(dirPath+"\\"+x)

# myDir = GUI.getDirectory()+"/"
myDir ="C:\\Users\\jedrz\\Downloads\\"
folderNames = ("Documents", "Images", "Applications", "Disk images", "Archives","Spreadsheets","Code")

reverse(myDir,folderNames)
print("---%s seconds ---" % (time.process_time() -start_time))