import tkinter as tk
from tkinter import filedialog
import os
from pathlib import Path
import webrepl_lib

app = tk.Tk()

def askForFile():
    systemDirectory =  filedialog.askdirectory(initialdir = "C:\\Users\\markg\\Desktop\\All Projects\\KTANE Box\\Code\\ktaneBoxCode\\manager-module", title = "Select dir")
    createFileList(systemDirectory)
    systemDirLabel.config(text=systemDirectory)

    

def createFileList(directory):
    global fileCheckboxes
    for fileCheckbox in fileCheckboxes:
        fileCheckbox['checkboxObj'].destroy()
        
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

def openConnection():
    global webreplObj
    webreplObj = webrepl_lib.webrepl(host=ipAddrVar.get())
    uploadButton.config(state='normal')

def closeConnection():
    webreplObj.closeConnection()
    uploadButton.config(state='disabled')

def uploadToDevice():
    for fileCheckboxDict in fileCheckboxes:
        if int(fileCheckboxDict['stateVar'].get()) == 1:
            webreplObj.sendFile(fileCheckboxDict["filepathObj"])
    

fileCheckboxes = []
webreplObj = None
#File stuff
browseButton = tk.Button(app, text = "Browse", command=askForFile)
systemDirLabel = tk.Label(app, text="No ESP32 system directory selected")
fileListFrame = tk.Frame(app)
selectAllButton = tk.Button(app, text="Select All", command=selectAll)
selectNoneButton = tk.Button(app, text="Select None", command=selectNone)
#Connection Stuff
ipAddrVar = tk.StringVar(app, '192.168.1.25')
ipAddrBox = tk.Entry(app, textvariable=ipAddrVar)
openButton = tk.Button(app, text="Open\nConnection", command=openConnection)
closeButton = tk.Button(app, text="Close\nConnection", command=closeConnection)
uploadButton = tk.Button(app, text="Upload to ESP32", command=uploadToDevice)
uploadButton.config(state='disabled')

gridOptions = {'sticky':'w'}
browseButton.grid(row=0, column=0, columnspan=3, **gridOptions)
systemDirLabel.grid(row=1, column=0, columnspan=3, **gridOptions)
selectAllButton.grid(row=2, column=0, **gridOptions)
selectNoneButton.grid(row=2, column=1, **gridOptions)
fileListFrame.grid(row=3, column=0, columnspan=3, **gridOptions)

ipAddrBox.grid(row=4,  column=0, columnspan=3, **gridOptions)
openButton.grid(row=5, column=0, **gridOptions)
closeButton.grid(row=5, column=2, **gridOptions)
uploadButton.grid(row=5, column=1, **gridOptions)


app.mainloop()