#Note: May no longer need HakuNekoFileRenaming.py. Probably delete that then rename GUI.py as HakuNekoFileRenaming.py!
#https://youtu.be/ibf5cx221hk 
from cgitb import text
import os
from this import d
import tkinter as tk
from tkinter import *
from tkinter import font as tkFont  
from tkinter import messagebox
from tkinter import filedialog
from natsort import natsorted, ns
import shutil

#===============CONNECTING TWO FILES TEST==================
#For code below, Refer to: https://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-script-from-another-script
#===============CONNECTING TWO FILES TEST==================
def fnFindFile(desiredDirectoryPath):
    fileExistence = os.path.exists(desiredDirectoryPath)
    if fileExistence == True:
        return True
    else:
        return False

chosenPath = None

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("HakuNeko File Sortation Program")
        self.root.configure(width=500, height=300)
        self.root.configure(bg='lightgray')
        self.root.geometry("2560x1440")

        self.label = tk.Label(self.root, text="HakuNeko File Sortation Program\nPlease Select a directory path then click \"Process Files\".\nOnce you are done, feel free to select another directory path and repeat the process.", font=('Arial', 18))
        self.label.pack(padx = 10, pady = 10)
       
        #self.checkState = tk.IntVar()

        #================BUTTON=================

        self.button = tk.Button(self.root, text="Choose Directory", font=('Arial', 18), command = self.fnChooseDirectoryPath)
        #self.button = tk.Button(self.root, text="Process Files", font=('Arial', 18), command = HakuNekoFileRenaming.fnSortThroughFiles)
        self.button.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Process Files", font=('Arial', 18), command = self.fnSortThroughFiles)
        #self.button = tk.Button(self.root, text="Process Files", font=('Arial', 18), command = HakuNekoFileRenaming.fnSortThroughFiles)
        self.button.pack(padx=10, pady=10)


        #================BUTTON=================

        #==================TEXT BOX============

        #=========IDEA=========== ----> Try to output text into the textox.
        #This might help? https://stackoverflow.com/questions/68198575/how-can-i-displaymy-console-output-in-tkinter
    
        #==================TEXT BOX============

        self.root.protocol("WM_DELETE_WINDOW",self.fnOnClosing)


        self.root.mainloop()
        

    def fnOnClosing(self):
        if messagebox.askyesno(title ="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    def fnPrint(self):
        if self.checkState.get() == 0:
            print("True")
        else:
            print("False")

    def fnChooseDirectoryPath(self):
        global chosenPath
        chosenPath = filedialog.askdirectory()
        print("\nChosen Directory Path: " + chosenPath + "\n")

    def fnSortThroughFiles(self):
        global chosenPath
        if chosenPath == None:
            print("\nNo directory path selected. Try again.\n")
        else:
            #Chosen directory path user will select
            print("Your chosen directory path is: " + chosenPath)

            #===============Merged Folder Creation=====================
            #chosenPath's parent directory
            chosenPathParentDirectory = os.path.dirname(chosenPath)
            #Adds a backslash if one doesn't already exist. 
            if chosenPathParentDirectory[-1] != "\\":
                chosenPathParentDirectory = "".join([chosenPathParentDirectory, "\\"])
            #Creates a new variable set to a variable upADirectory's pathway with \Merged as its last component.
            mergedFilePath = "".join([chosenPathParentDirectory, "\\Merged"])

            #Checks to see if the merged folder exists yet. If not, then create it. 
            if fnFindFile(mergedFilePath) == False:
                #os.makedirs(mergedFilePath)
                #Up a hierarchy
                os.makedirs(mergedFilePath)
            #===============Merged Folder Creation=====================

            #===================================FILE LISTING===================================
            #label = Label(self.root, text=("List of files in your folder"), font=('Arial', 18))
            #label.pack()
            i = 0
            #Used to rename the files
            x = 0
            y=0
            #==========IMPORTANT===========
            #Key = len kind of works. But not for chapters with a .5 as they
            #are put at the end of the list.
            #for x in sorted(os.listdir(chosenPath), key=len):
            for file in natsorted(os.listdir(chosenPath), key=lambda y: y.lower()):
                i = i+1
                print("\n" + str(i) + ". " + file)
                #The code below is used if I want labels only.
                #label = Label(self.root, text=(str(i) + ". " + x), font=('Arial', 18))
                #label.pack(padx=10,pady=10)
            
                #Make a for loop that iterates through a concatenation of chosenPath and file to rename .jpgs and move them all into one single folder rather than being in separate folders.
                childPath = "".join([chosenPath, "\\"+file])

                for file in  natsorted(os.listdir(childPath)):
                    x = x+1
                    print(file)
                    #==============FILE RENAMING=================
                    try:
                        os.rename(os.path.join(childPath,file), os.path.join(childPath,str(x)+"A.jpg"))
                        #shutil.copyfile((childPath+"\\"+str(x)+".jpg"),mergedFilePath)
                    except WindowsError:
                        os.remove(os.path.join(childPath,str(x)+".jpg"))
                        os.rename(os.path.join(childPath,file), os.path.join(childPath,str(x)+"A.jpg"))
                        shutil.copyfile((childPath+"\\"+str(x)+".jpg"),mergedFilePath)
                for file in  natsorted(os.listdir(childPath)):
                    y=y+1
                    shutil.copy(os.path.join(childPath,file),mergedFilePath)
                    #==============FILE RENAMING=================
                    #shutil.copyfile(mergedFilePath)
            #Outputs the total amount of files (in this case folder) founded inside of chosenPath (not the files inside of chosenPath's files)
            #print("\nA total of " + str(i) + " items are in the directory " + chosenPath)

            #===================================FILE LISTING===================================
        print("\n========\nFinished\n========\n")
MyGUI()
