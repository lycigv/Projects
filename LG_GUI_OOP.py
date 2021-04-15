#Python3 & SQLite3 End of WorkDay FileTransfer Program
from contextlib import closing
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import shutil
import datetime as dt
import time
import sqlite3
# USing Inheritance 
class GUIframe (ttk.Frame):
    def __init__(self, parent):      
        ttk.Frame.__init__(self, parent, padding="20 20 20 20")
        self.parent=parent
        self.sourceDir = StringVar()
        self.destinationDir = StringVar()
        self.lastTime=StringVar()
                
        self.widgetThings(parent)
        
        self.conn = sqlite3.connect('fileTransferOOP.db')
        self.c = self.conn.cursor()
        self.createDb()
        #self.fetchData()
    def widgetThings(self,parent):
        #Buttons & Labels
        browseButton = ttk.Button(parent, text = 'SourceFile  Folder', command = self.askSource).grid(row = 1, column = 2, padx = 5, pady = 5)
        browseButton = ttk.Button(parent,text = 'Destination Folder', command = self.askDestination).grid(row = 2, column = 2, padx = 5, pady = 5)
        copyButton = ttk.Button(parent,text = 'Copy The Files', command = self.fileCopy).grid(row = 3, column = 1, padx = 5, pady = 5)
        timeButton=ttk.Button(parent,text = 'Last backup time', command = self.fetchData).grid(row = 3, column = 2, padx = 5, pady = 5)
        pathLabel = ttk.Entry(parent, text = self.sourceDir).grid(row = 1, column = 1, padx = 1, pady = 1)
        pathLabel = ttk.Entry(parent,text = self.destinationDir).grid(row = 2, column = 1, padx = 1, pady = 1)
        timeLabel = ttk.Entry(parent, text = "Last File Check:  " , textvariable=self.lastTime).grid(row = 4, column = 1,padx = 5, pady = 5)   
    #
    def createDb(self):
        #create database and table
        self.c.execute('CREATE TABLE IF NOT EXISTS timeElapsed(time TIMESTAMP)')
        self.c.execute('INSERT INTO timeElapsed VALUES (2021)')
        self.conn.commit()# dummy value for the table/ first entry
    def fetchData(self):
        # select time of last file move from db
        with closing (self.c):
            self.c.execute('SELECT time FROM timeElapsed ORDER by time DESC')
            theTime = self.c.fetchone()[0]
            self.lastTime.set(theTime)
            print()
            print("X"*20)
            print("Last modified time: ",theTime)
            print("X"*20)
        
   
    #functions to attach in buttons 
    def askSource(self):
        self.sourceName = filedialog.askdirectory()
        if self.sourceName:
            self.sourceDir.set(self.sourceName)
    def askDestination(self):
        self.destinationName = filedialog.askdirectory()
        if self.destinationName:
            self.destinationDir.set(self.destinationName)
    def fileCopy(self):
        # inserts time to db whenever copy button is pressed 
        now = dt.datetime.now()
        self.c.execute('INSERT INTO timeElapsed VALUES(?)',(now.strftime('%Y-%m-%d %H:%M'),))                                
        self.conn.commit()
        dayAgo = now - dt.timedelta(hours = 8) #Assume you work 8hrs a day
        #get the paths for sending and recieving folders
        sender = self.sourceDir.get()
        receiver = self.destinationDir.get()    
        for fileName in os.listdir(sender):
            path = os.path.join(sender, fileName)
            stat = os.stat(path)
            modTime = dt.datetime.fromtimestamp(stat.st_mtime)
            if modTime > dayAgo:
                shutil.copy2(path, receiver)
                print()
                print("X"*20)
                print ("The modified files:",fileName, " moved to backup folder.")
                print("X"*20)  

if __name__=="__main__":    
    root=Tk()
    root.title("File Transfer GUI")
    GUIframe(root)
    root.mainloop()

# The END
