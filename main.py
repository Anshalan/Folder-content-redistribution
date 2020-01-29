import os, shutil
import time

def folderCheckCreate(*therest):
    for x in list(therest):
        if os.path.exists(myDir+x):
            continue
            #print("folder", x, "already exist")
        else:
            try:
                os.mkdir(myDir+x)
                print(x, "folder was created")
            except os.error as e:
                print(e)

def moveIfDocument(fileDir, fileName):
    destFolder = "Documents"
    if fileName.lower().endswith((".pdf", ".doc",".docx", ".odt", ".txt")):
        # print(x, 'is a PDF file')
        folderCheckCreate(destFolder)
        shutil.move(fileDir + x, fileDir + destFolder +'\\'+ x)
def moveIfPicture(fileDir, fileName):
    destFolder = "Pictures"
    if fileName.lower().endswith((".jpg", ".jpeg",".bmp", ".png")):
        folderCheckCreate(destFolder)
        shutil.move(fileDir + x, fileDir + destFolder +'\\'+ x)
def moveIfExecutable(fileDir, fileName):
    destFolder = "Applications"
    if fileName.lower().endswith(".exe"):
        folderCheckCreate(destFolder)
        shutil.move(fileDir + x, fileDir + destFolder +'\\'+ x)
def moveIfISO(fileDir, fileName):
    destFolder = "Disk images"
    if fileName.lower().endswith(".iso"):
        folderCheckCreate(destFolder)
        shutil.move(fileDir + x, fileDir + destFolder +'\\'+ x)
def moveIfArchive(fileDir, fileName):
    destFolder = "Archives"
    if fileName.lower().endswith((".zip", "rar", ".7z")):
        folderCheckCreate(destFolder)
        shutil.move(fileDir + x, fileDir + destFolder + '\\' + x)
def moveIfSpreadsheet(fileDir, fileName):
    destFolder = "Spreadsheets"
    if fileName.lower().endswith((".xml", "xls", "xlsm", "xlsx")):
        folderCheckCreate(destFolder)
        shutil.move(fileDir + x, fileDir + destFolder + '\\' + x)
def moveIfCode(fileDir, fileName):
    destFolder = "Code"
    if fileName.lower().endswith((".py", ".c", ".cpp", ".h", ".hpp")):
        folderCheckCreate(destFolder)
        shutil.move(fileDir + x, fileDir + destFolder + '\\' + x)

start_time = time.process_time()

myDir = "C:\\Users\\jedrz\\Downloads\\" ##directory you want to redistribute files from as "C:\\aaa\\sss\\ddd\\"
dirlist = os.listdir(myDir)

for x in dirlist :
    if os.path.isfile(myDir+x):
        moveIfDocument(myDir, x)
        moveIfArchive(myDir, x)
        moveIfCode(myDir, x)
        moveIfExecutable(myDir, x)
        moveIfISO(myDir, x)
        moveIfPicture(myDir, x)
        moveIfSpreadsheet(myDir, x)

    else:
        print(x, "is not a file but and didnt tell me what to do with it")
print("---%s seconds ---" % (time.process_time() -start_time))