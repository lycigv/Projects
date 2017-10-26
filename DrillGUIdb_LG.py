# LG's Simple python GUI to transfer recently modified files 

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
import datetime
import time
import shutil
import os
from os import path
import sqlite3


class CopyFileApp:
    
    def __init__(self, master):
        
        self.LastRun= StringVar()
        label = ttk.Entry(master, textvariable = self.LastRun).pack()
        button = ttk.Button(master, text = "Click For Last Run Time:", command = self.get_last_time).pack()

        self.source= StringVar()
        label = ttk.Entry(master, textvariable = self.source).pack()
        button = ttk.Button(master, text = "Select Source Folder", command=self.load_src ).pack()

        self.destination = StringVar()
        label = ttk.Entry(master, textvariable= self.destination).pack()
        button = ttk.Button(master, text = "Select Destination Folder",command=self.load_dst ).pack()
     
        self.FilesMoved=StringVar()        
        label = ttk.Entry(master, textvariable = self.FilesMoved).pack()
        button = ttk.Button(master, text = "Copy New Files Now", command = self.check_file_contents).pack()
        self.createDb()
        
    def load_src(self):
        self.src = askdirectory()
        self.source.set(self.src)
           
    def load_dst(self):
        self.dst = askdirectory()
        self.destination.set(self.dst)

    def get_last_time(self):
        conn = sqlite3.connect('click_time_stamp.db')
        c = conn.cursor()
        c.execute('SELECT * FROM time_stamp ORDER BY Time DESC Limit 1')
        last_time = c.fetchone() 
        self.LastRun.set(last_time) 
                
    def check_file_contents(self):
        self.unix = time.time()       
        for file in os.listdir(self.src):
            if file.endswith('.txt'):
                src_name = os.path.join(self.src,file)
                modified_time = os.path.getmtime(src_name)
                elapsed_time = self.unix - modified_time
                if elapsed_time < 86400:   
                    shutil.copy(src_name,self.dst)
                    self.insertDb()
                    self.FilesMoved.set(file)
   
    def createDb(self):
        conn = sqlite3.connect('click_time_stamp.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS time_stamp (Time TEXT)')  
               
    def insertDb(self):
        conn = sqlite3.connect('click_time_stamp.db')
        c = conn.cursor()
        last_stamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.unix))
        print(last_stamp)
        c.execute('INSERT INTO time_stamp (Time) VALUES(?)',(last_stamp,))
        conn.commit()                        
        c.close
        conn.close
              
def main():  
    root = Tk() 
    app = CopyFileApp(root)
    root.mainloop()
    
if __name__ == "__main__": 
	main()
