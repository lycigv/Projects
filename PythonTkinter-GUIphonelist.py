from tkinter import *

win=Tk()

##b1=Button(win,text="One")
##b2=Button(win,text="Two")
##
##b1.pack(side=LEFT, padx=10)
##b2.pack(side=LEFT, padx=10)

##b1 = Button(win,text="One")
##b2 = Button(win,text="Two")
##b1.grid(row=0, column=0)
##b2.grid(row=1, column=1)
##l = Label(win, text="This is a label")
##l.grid(row=1,column=0)


f = Frame(win)
b1 = Button(f, text="One")
b2 = Button(f, text="Two")
b3 = Button(f, text="Three")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)

##v=StringVar()
##l= Label(win,textvariable=v)
##v.set("This label is over all buttons")

l=Label(win,text="This is over buttons")
l.pack()
f.pack()

b1.configure(text="Uno")
def but1():
    print ("Button was pushed")
b1.configure(command=but1)

v=StringVar()
e=Entry(win,textvariable=v)
e.pack()
v.set("This is a Program")
##v.get()

lb=Listbox(win, height=3)
lb.pack(side=LEFT)
lb.insert(END,"first entry")
lb.insert(END, "second entry")
lb.insert(END,"third entry")
lb.insert(END, "fourth entry")
sb=Scrollbar(win,orient=VERTICAL)
sb.pack(side=LEFT, fill=Y)
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)
lb.curselection()

