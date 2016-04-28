import tkinter as tk
import webModule as wM

import sqlite3

conn = sqlite3.connect('ExistingContents.db')
c = conn.cursor()


class TheWindow(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.wm_geometry("")

        self.filename = "html_for_72drill.html"

        self.grid()
        self.radio=[]
        self.var = tk.StringVar()  

        # New content button
        createNewButton = tk.Button(self, text="Content Input", command=self.createNew)
        createNewButton.grid(column=0, row=0, padx=20)

        # Old content button
        ExistingContent = tk.Button(self, text="Existing Content", command=self.oldContent)
        ExistingContent.grid(column=1, row=0, padx=20)
      

        
    def createNew(self):
        self.action = "new"
        if getattr(self, 'radioButtons', None):
            for button in self.radio:
                button.grid_remove()
            self.removeButtons()
            

        # Label for New Content
        self.label = tk.Label(self, anchor="w", text="New Content:")
        self.label.grid(column=0, row=1, sticky='EW', columnspan=2, padx=5)
        
        # New content box
        self.text = tk.Text(self, height=15, width=50)
        self.text.grid(column=0, row=2, sticky='EW', columnspan=2, padx=5)

        self.showButtons()
        
    def webContent(self):
        #add new content input
        wM.webContent(self)

    def oldContent(self):
        self.action = "old"

        if getattr(self, 'text', None):
            self.text.grid_remove()
            self.removeButtons()
            
##        self.var.set()
        # Previous content label
        self.label = tk.Label(self, anchor="w", text="Old content:")
        self.label.grid(column=0, row=1, columnspan=2, sticky='EW', padx=5)       
        
        # Selecting contents
        c.execute("SELECT * FROM WebContent")
        row = c.fetchall()
        
        # count of rows
        c.execute("SELECT COUNT(*) FROM WebContent")
        count = c.fetchone()[0]
        
          # Dynamic radio button list of existing contents
        for id, Contents in row:
            self.radioButtons = tk.Radiobutton(self,
                                               bg="light gray",
                                               fg="blue",
                                               indicatoron=0,
                                               relief="sunken",
                                               width=55,
                                               text=Contents,
                                               padx=5,
                                               justify="left",
                                               anchor="w",
                                               variable=self.var,
                                               val=Contents)
            self.radioButtons.deselect()

            self.radioButtons.grid(column=0, row=id+1, columnspan=2, sticky="EW")

            # Save list of button preferences to remove later
            self.radio.append(self.radioButtons)
            buttonPos = id + 2
        
        self.showButtons()
        
    def openPage(self):
       #display page
        wM.openPage(self)

    def showButtons(self):
        #publish or view buttons
        self.publishButton = tk.Button(self, text="Publish", command=self.webContent)
        self.publishButton.grid(column=2, row=0)

        self.viewButton = tk.Button(self, text="Veiw", command=self.openPage)
        self.viewButton.grid(column=2, row=1)
        
    def removeButtons(self):
       #to remove view or publish
        self.publishButton.grid_remove()
        self.viewButton.grid_remove()

if __name__ == "__main__":
    app = TheWindow(None)
    app.title("HTML Page Input") 
    app.mainloop()

