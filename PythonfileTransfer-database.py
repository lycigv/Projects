from __future__ import unicode_literals

import wx, sqlite3
import shutil, os, time, sys
import datetime as dt
from datetime import  timedelta

 # Connect to database
conn=sqlite3.connect('CheckFileTime.db')
c=conn.cursor()



##def tableCreate():
##    c.execute("DROP TABLE IF EXISTS FileTransfer")
##    c.execute('CREATE TABLE FileTransfer (ID INTEGER, datestamp TEXT)')
##tableCreate()
 


class windowClass(wx.Frame):
    
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(360, 250))

        self.Center()
        getLastRow()
        
        panel=wx.Panel(self)
        wx.StaticText(panel, -1, 'Copy files modified in last 24hrs', (100,10))

        # Get the last row in table
        last_row1 = getLastRow()
##        print type(last_row1)
        print last_row1
        
        # Display file modification time
        self.LastTransferDate = wx.StaticText(panel, -1, last_row1[1], (285,10))
        
        fileCopy=wx.Button(panel,label='Copy',pos=(100,150))
        self.Bind(wx.EVT_BUTTON, self.copyFile, fileCopy) 
        fileCheck=wx.Button(panel,label='checkFile',pos=(200,150))
        self.Bind(wx.EVT_BUTTON, self.checkFile, fileCheck)   

        # Source folder view
        wx.StaticText(panel, label='Source:', pos=(20,40))
        self.SourceFilePath = wx.TextCtrl(panel, pos=(100,40), size=(140,25), style=wx.TE_READONLY)
        wx.Button(panel, 1, 'Browse', pos=(240, 40))
        self.Bind(wx.EVT_BUTTON, self.sourceBrowse, id=1)

        # Destination folder view
        wx.StaticText(panel, label='Destination:', pos=(20,100))
        self.DestinationFilePath = wx.TextCtrl(panel, pos=(100,100), size=(140,25), style=wx.TE_READONLY)
        wx.Button(panel, 2, 'Browse', pos=(240, 100))
        self.Bind(wx.EVT_BUTTON, self.destinationBrowse, id=2)

        self.Show(True)
                
    def checkFile(self,event):
        source = self.SourceFilePath.GetValue() + "\\"
        print(source)
        destination = self.DestinationFilePath.GetValue() + "\\"
        print(destination)
        
        listfile= os.listdir(source)
        print listfile

        today=dt.datetime.now()
        modtime=today-dt.timedelta(hours=24)
       
        for files in listfile:
            if files.endswith('.txt'):
                mtime=dt.datetime.fromtimestamp(os.stat(source+files).st_mtime)
                print mtime
                if mtime > modtime:
                    print  source+files
                    print destination+files             

    def copyFile(self,event):
        source = self.SourceFilePath.GetValue() + "\\"
        print(source)
        destination = self.DestinationFilePath.GetValue() + "\\"
        print(destination)
         
        listfile= os.listdir(source)
        print listfile
        
        # Get the last row in the database
        last_row2 = getLastRow()
        id = last_row2[0] + 1
        
##        ModDate = datetime.datetime.strptime(last_row2[1], '%m-%d-%Y %H:%M:%S')
##        today = datetime.datetime.today().strftime("%m-%d-%Y %H:%M:%S")
##        modtime=today-dt.timedelta(hours=24).strptime(last_row2[1], '%m-%d-%Y %H:%M:%S')
        
        today=dt.datetime.now()
        modtime=today-dt.timedelta(hours=24)

        for files in listfile:
            if files.endswith('.txt'):
                mtime=dt.datetime.fromtimestamp(os.stat(source+files).st_mtime)      
                if mtime > modtime:
                    shutil.copy2(source+files,destination)
                    print destination+files
                else:
                    print "File is not new to copy"
    
        c.execute('INSERT INTO FileTransfer VALUES(?,?)',(id, today))
        conn.commit()
        

        # Update GUI with new dateTime
        self.LastTransferDate.SetLabel(str(today))

    def sourceBrowse(self, event):
        dlg = wx.DirDialog(self, 'Choose Source Folder:')
        if dlg.ShowModal() == wx.ID_OK:
            self.SourceFilePath.WriteText(dlg.GetPath())
        dlg.Destroy()
        
    def destinationBrowse(self, event):
        dlg = wx.DirDialog(self, 'Choose Destination Folder:')
        if dlg.ShowModal() == wx.ID_OK:
            self.DestinationFilePath.WriteText(dlg.GetPath())
        dlg.Destroy()
        
def getLastRow():
    conn = sqlite3.connect('CheckFileTime.db')
    c = conn.cursor()
    row = c.execute('SELECT * FROM FileTransfer WHERE ID = (SELECT MAX(ID) FROM FileTransfer)').fetchone()
    print row
    conn.close()
    return row
        

if __name__=='__main__': 
    app= wx.App()        
    windowClass(None,title='TO COPY NEW FILES !!')
    app.MainLoop()

conn.close()
