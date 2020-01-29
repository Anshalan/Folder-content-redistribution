#imports
import os, sys

####functions#####################################################

####check and create forders you want to use for redistribution############################
def folderCheckCreate(*therest):
    for x in list(therest):
        if os.path.exists(myDir+x):
            print("folder", x, "already exist")
        else:
            try:
                os.mkdir(myDir+x)
                print(x, "folder was created")
            except os.error as e:
                print(e)


myDir = "C:\\Users\\jedrz\\Downloads\\Folder testowy\\" ##drectory you want to redistribute files from as "C:\\aaa\\sss\\ddd\\"
dirlist = os.listdir(myDir)
#print (dirlist)

#### listing directory content########################################
# for x in os.listdir("."):
# for x in dirlist :
#     #print (myDir + x)
#     if os.path.isfile(myDir+x):
#         print ('f- ', x)
#     elif os.path.isdir(myDir+x):
#         print ("d- ", x)
#     else:
#         print("nothing?")



folderCheckCreate("test2", "test3")