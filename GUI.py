import tkinter as tk
from tkinter import filedialog, Text
import move

folderName = ""

def addFolder():
    global folderName
    folderName = filedialog.askdirectory()
    # folder.append(folderName)
    print(folderName)
    # print(folder)
def execute():
    move.tempFunctionName(folderName)

# def getDirectory():
window = tk.Tk()
window.title("Files redistributon")
canvas = tk.Canvas(window, height=500, width=800, bg="#320775")
canvas.pack()

frame = tk.Frame(window, bg= "#D8A5F3")
frame.place(relheight=0.7, relwidth=0.7, relx=0.15, rely=0.15)

openFile =tk.Button(frame, text="Select folder", bg="#320775", fg = "white", activebackground="#32FF75", command = addFolder)
openFile.pack()
runApp =tk.Button(frame, text="Run App", bg="#320775", fg = "white", activebackground="#32FF75", command = execute)
runApp.pack()

window.mainloop()
    # return folderName

