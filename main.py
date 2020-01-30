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

def moveFile(fileDir, fileName, destFolder):
    folderCheckCreate(destFolder)
    shutil.move(fileDir + fileName, fileDir + destFolder + '\\' + fileName)

start_time = time.process_time()

myDir = "C:\\Users\\jedrz\\Downloads\\" ##directory you want to redistribute files from as "C:\\aaa\\sss\\ddd\\"
dirlist = os.listdir(myDir)

for x in dirlist :
    if os.path.isfile(myDir+x):
        fileExtension = x.rpartition('.')
       # print(fileExtension[2])
        if fileExtension[2].lower() in ("pdf", "doc","docx", "odt", "txt"):
            moveFile(myDir, x, "Documents")
        elif fileExtension[2].lower() in ("jpg", "jpeg","bmp", "png"):
            moveFile(myDir, x, "Images")
        elif fileExtension[2].lower() in ("exe"):
            moveFile(myDir, x, "Applications")
        elif fileExtension[2].lower() in ("iso"):
            moveFile(myDir, x, "Disk Images")
        elif fileExtension[2].lower() in ("zip","rar","7z"):
            moveFile(myDir, x, "Archives")
        elif fileExtension[2].lower() in ("xml","xls","xlsm","xlsx"):
            moveFile(myDir, x,"Spreadsheets")
        elif fileExtension[2].lower() in ("py", "c", "cpp", "h","hpp"):
            moveFile(myDir, x, "Code")
        else:
            print("no defined action for",fileExtension[2].upper(), "file")
    else:
        print(x, "is not a file but and didnt tell me what to do with it")
print("---%s seconds ---" % (time.process_time() - start_time))