
import wx
import os, time, sys
import datetime as dt
from datetime import  timedelta


app = wx.App()

class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)
        self.Center()
        self.basicGUI()
       
    def basicGUI(self):
        
        panel=wx.Panel(self)
        wx.StaticText(panel, -1, 'Check for new pictures', (100,10))

        fileCheck=wx.Button(panel,label='checkFile',pos=(200,150))
        self.Bind(wx.EVT_BUTTON, self.checkFile, fileCheck)   

        # Source folder view
        wx.StaticText(panel, label='Source:', pos=(20,40))
        self.SourceFilePath = wx.TextCtrl(panel, pos=(100,40), size=(140,25), style=wx.TE_READONLY)
        wx.Button(panel, 1, 'Browse', pos=(240, 40))
        self.Bind(wx.EVT_BUTTON, self.sourceBrowse, id=1)

        self.Show(True)
        
    def exitProgram(self,event):
        self.Destroy()


    def checkFile(self,event):
        source = self.SourceFilePath.GetValue() + '\\'
##        print(source)
   
        listfile= os.listdir(source)
##        print listfile

        today=dt.datetime.now()
        modtime=today-dt.timedelta(hours=24)
       
        for files in listfile:
            if files.endswith('.JPG'):
                mtime=dt.datetime.fromtimestamp(os.stat(source+files).st_mtime)
##                print mtime
                if mtime > modtime:
                    print  source+files
                    wx.MessageBox('New Picture is Added!', 'Alert!!', wx.OK)
                else:
                    print 'Not a New Picture'
            
  

    def sourceBrowse(self, event):
        dlg = wx.DirDialog(self, 'Choose Source Folder:')
        if dlg.ShowModal() == wx.ID_OK:
            self.SourceFilePath.WriteText(dlg.GetPath())
        dlg.Destroy()
        

 
def main():
    app= wx.App()        
    windowClass(None,title='TO ALERT NEW PICTURES !!')
    app.MainLoop()
main()

