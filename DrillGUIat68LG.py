# Python 2.7 GUI   Drill: Lyci

from __future__ import unicode_literals
import wx
import shutil, os, time, sys
import datetime as dt
from datetime import  timedelta

class windowClass(wx.Frame):   
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)       
        self.Center()
        self.basicGUI()
        #self.SetBackgroundColour('yellow')
        
    def basicGUI(self):
        
        panel=wx.Panel(self)
        wx.StaticText(panel, -1, "Copy files modified in last 24hrs", (100,10))
        panel.SetBackgroundColour('green')
        
        fileCopy=wx.Button(panel,label="Copy",pos=(100,150))
        self.Bind(wx.EVT_BUTTON, self.copyFile, fileCopy) 
        fileCheck=wx.Button(panel,label="checkFile",pos=(200,150))
        self.Bind(wx.EVT_BUTTON, self.checkFile, fileCheck)   
        fileCopy.SetBackgroundColour('red')
        fileCheck.SetBackgroundColour('red')
        
        menuBar=wx.MenuBar()
        fileButton=wx.Menu()
        editButton=wx.Menu()
        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'Edit')
        self.SetMenuBar(menuBar)

        editButton.Append(wx.ID_COPY, 'Copy')
        exitItem=fileButton.Append(wx.NewId(), "Exit")
        self.Bind(wx.EVT_MENU,self.exitProgram, exitItem)
        
        # Source folder view
        wx.StaticText(panel, label='Source:', pos=(20,40))
        self.SourceFilePath = wx.TextCtrl(panel, pos=(100,40), size=(340,35), style=wx.TE_READONLY)
        self.button=wx.Button(panel, 1, 'Browse', pos=(450, 40))
        self.Bind(wx.EVT_BUTTON, self.sourceBrowse, id=1)
        self.SourceFilePath.SetBackgroundColour('yellow')                              
        self.button.SetBackgroundColour('blue')
        
        # Destination folder view
        wx.StaticText(panel, label='Destination:', pos=(20,100))
        self.DestinationFilePath = wx.TextCtrl(panel, pos=(100,100), size=(340,35), style=wx.TE_READONLY)
        self.button=wx.Button(panel, 2, 'Browse', pos=(450, 100))
        self.Bind(wx.EVT_BUTTON, self.destinationBrowse, id=2 )
        self.DestinationFilePath.SetBackgroundColour('yellow')
        self.button.SetBackgroundColour('blue')
        self.Show(True)
        
    def exitProgram(self,event):
        self.Destroy()
        
    def checkFile(self,event):
        source = self.SourceFilePath.GetValue() + "\\"
        print(source)
        destination = self.DestinationFilePath.GetValue() + "\\"
        print(destination)     
        listfile= os.listdir(source)     
        today=dt.datetime.now()
        modtime=today-dt.timedelta(hours=24)       
        for files in listfile:
            if files.endswith(".txt"):
                mtime=dt.datetime.fromtimestamp(os.stat(source+files).st_mtime)                
                if mtime > modtime:
                    print  ("Newly Modified: {} ", files)
                else:
                    print ("File is not new to move")

    def copyFile(self,event):     
        source = self.SourceFilePath.GetValue() + "\\"
        print(source)
        destination = self.DestinationFilePath.GetValue() + "\\"
        print(destination)
        listfile= os.listdir(source)      
        today=dt.datetime.now()
        modtime=today-dt.timedelta(hours=24)
        for files in listfile:
            if files.endswith(".txt"):
                mtime=dt.datetime.fromtimestamp(os.stat(source+files).st_mtime)      
                if mtime > modtime:
                    shutil.move(source+files,destination)
                    print ("Moved Files;", files)

    def sourceBrowse(self, event):
        dlg = wx.DirDialog(self, "Choose Source Folder:")
        if dlg.ShowModal() == wx.ID_OK:
            self.SourceFilePath.WriteText(dlg.GetPath())
        dlg.Destroy()       
        
    def destinationBrowse(self, event):
        dlg = wx.DirDialog(self, "Choose Destination Folder:")
        if dlg.ShowModal() == wx.ID_OK:
            self.DestinationFilePath.WriteText(dlg.GetPath())
        dlg.Destroy()
        
def main():
    app= wx.App()   
    windowClass(None,title='TO COPY NEW FILES !!')
    app.MainLoop()
main()

