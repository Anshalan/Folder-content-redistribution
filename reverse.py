import os, shutil
import time

# start_time = time.process_time()
def reverseMove(dirPath, folderNames):
    start_time = time.process_time()
    for x in list(folderNames):
        if os.path.exists(dirPath+"\\"+x):
            for file in os.listdir(dirPath+"\\"+x):
                shutil.move(dirPath+"\\"+x+"\\"+file, dirPath+"\\"+file)
            os.rmdir(dirPath+"\\"+x)
    print("---%s seconds ---" % (time.process_time() -start_time))

# # myDir = GUI.getDirectory()+"/"
# myDir ="C:\\Users\\jedrz\\Downloads\\"
# folderNames = ("Documents", "Images", "Applications", "Disk images", "Archives","Spreadsheets","Code")
#
# reverseMove(myDir,folderNames)
# print("---%s seconds ---" % (time.process_time() -start_time))