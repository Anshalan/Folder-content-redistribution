import tkinter as tk
from tkinter import filedialog, Text
import move
from reverse import reverseMove

folderName = ""

def addFolder():
    global folderName
    folderName = filedialog.askdirectory()
    # folder.append(folderName)
    print(folderName)
    # print(folder)
def execute():
    move.tempFunctionName(folderName)
    print("moved")
def rev():
    reverseMove(folderName,("Documents", "Images", "Applications", "Disk images", "Archives","Spreadsheets","Code"))
    print("reversed")

# def getDirectory():
window = tk.Tk()
window.title("Files redistributon")


canvas = tk.Canvas(window, height=250, width=250, bg="#c1c1c1")
canvas.pack()
frame = tk.Frame(window, bg= "#B1B1B1", bd=1, highlightbackground="black")

frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

openFile =tk.Button(frame, text="Select folder", bg="#C6C6C6", fg = "black", activebackground="#32FF75", command = addFolder)
openFile.pack()
runApp =tk.Button(frame, text="Run App", bg="#C6C6C6", fg = "black", activebackground="#32FF75", command = execute)
runApp.pack()
Reverse =tk.Button(frame, text="Reverse", bg="#C6C6C6", fg = "black", activebackground="#32FF75", command = rev)
Reverse.pack()

window.mainloop()
    # return folderName

