import webbrowser
import tkinter as tk


class TheWindow(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        
        self.wm_geometry("")

        self.filename = "html_for_72drill.html"

        self.grid()
               
        self.var = tk.StringVar()  

        # New content button
        createNewButton = tk.Button(self, text="Content Input", command=self.createNew)
        createNewButton.grid(column=0, row=0, padx=57)

        # Old content button
        ExistingContent = tk.Button(self, text="Existing Content", command=self.oldContent)
        ExistingContent.grid(column=1, row=0, padx=57)
       
        
    def createNew(self):
        self.action = "new"
##        self.var.set()
        # Label for New Content
        self.label = tk.Label(self, anchor="w", text="New Content:")
        self.label.grid(column=0, row=1, sticky='EW', columnspan=2, padx=5)
        
        # New content box
        self.text = tk.Text(self, height=15, width=50)
        self.text.grid(column=0, row=2, sticky='EW', columnspan=2, padx=5)
        self.showButtons()

    def oldContent(self):
        self.action = "old"
##        self.var.set()
        # Previous content label
        self.label = tk.Label(self, anchor="w", text="Old content:")
        self.label.grid(column=0, row=1, columnspan=2, sticky='EW', padx=5)

        f = open('Web page generator project.html','w')
        message = """  
        <html>
        <body>
        Stay tuned for our amazing summer sale!
        </body>
        </html> 
        """
        f.write(message)
        f.close()
        webbrowser.open_new_tab('Web page generator project.html')
        self.showButtons()

    def webContent(self):
        if self.action == "new":
            text = self.text.get("1.0", 'end')
            self.text.delete("1.0", 'end')
        else:
            # keep old webpage
            text = self.var.get()    
##        # Add html to  content
        html = "<html>\n\t<body>\n\t\t<pre>\n" + text + "\n\t\t</pre>\n\t</body>\n</html>"

        # Write html to a file
        f = open(self.filename,'w') 
        f.write(html)
        f.close()
        
    def openPage(self):
       #display page
        webbrowser.open(self.filename)

    def showButtons(self):
        #publish or view buttons
        self.publishButton = tk.Button(self, text="Publish", command=self.webContent)
        self.publishButton.grid(column=2, row=0)

        self.viewButton = tk.Button(self, text="Veiw", command=self.openPage)
        self.viewButton.grid(column=2, row=1)


if __name__ == "__main__":
    app = TheWindow(None)
    app.title("HTML Page Input") 
    app.mainloop()
