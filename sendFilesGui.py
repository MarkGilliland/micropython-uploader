import tkinter as tk
from tkinter import filedialog
import os
from pathlib import Path

app = tk.Tk()

def askForFile():
    systemDirectory =  filedialog.askdirectory(initialdir = "C:\\Users\\markg\\Desktop\\All Projects\\KTANE Box\\Code\\ktaneBoxCode\\manager-module", title = "Select dir")
    createFileList(systemDirectory)
    systemDirLabel.config(text=systemDirectory)

    

def createFileList(directory):
    global fileCheckboxes
    files = os.listdir(directory)
    fileCheckboxes = []#list of dicts {"filepathObj":filepathObj, "checkboxObj":checkboxObj, "stateVar":stateVariableObj}
    gridCounter = 0
    for file in files:
        stateVar = tk.IntVar(value=0)
        fileCheckboxes.append({"filepathObj":Path(f'{directory}\\{file}'), 
                              "stateVar":stateVar,
                              "checkboxObj":tk.Checkbutton(fileListFrame, text=file, justify="left", anchor="w", variable=stateVar)})
        fileCheckboxes[-1]["checkboxObj"].grid(row=gridCounter, column=0,sticky='w')
        gridCounter += 1   
    print(files)

def selectAll():
    for fileCheckboxDict in fileCheckboxes:
        fileCheckboxDict['checkboxObj'].select()
    
def selectNone():
    for fileCheckboxDict in fileCheckboxes:
        fileCheckboxDict['checkboxObj'].deselect()

def uploadToDevice():
    pass

fileCheckboxes = []
browseButton = tk.Button(app, text = "Browse", command=askForFile)
systemDirLabel = tk.Label(app, text="No ESP32 system directory selected")
fileListFrame = tk.Frame(app)
selectAllButton = tk.Button(app, text="Select All", command=selectAll)
selectNoneButton = tk.Button(app, text="Select None", command=selectNone)
uploadButton = tk.Button(app, text="Upload to ESP32", command=uploadToDevice)

gridOptions = {'sticky':'w'}
browseButton.grid(row=0, column=0, columnspan=2, **gridOptions)
systemDirLabel.grid(row=1, column=0, columnspan=2, **gridOptions)
selectAllButton.grid(row=2, column=0, **gridOptions)
selectNoneButton.grid(row=2, column=1, **gridOptions)
fileListFrame.grid(row=3, column=0, columnspan=2, **gridOptions)
uploadButton.grid(row=4, column=0, columnspan=2, **gridOptions)


app.mainloop()