# import library
from Tkinter import *
import Tkinter
import sys
# ----------------
def showpackage():
    import dircache
    a = dircache.listdir(input1.get())
    for path in a:
        path = '[~]' + ' ' + path + '\n'
        text.insert(END,path)
# ---------------------------------------------------
# code for tkinter
root = Tk() # Create widget
root.title("Show file") # Title widget
root.minsize(610,280) # minsize widget
root.config(bg = '#e7d5d5') # background-color widget
# ---------------------------------------------------
Label(root, text="Please Enter path :", bg = '#eed78f').place(x = 5, y = 20) # Create label
var = StringVar()
input1 = Entry(root,textvariable=var,width=50)
input1.place(x=110,y=20)
# ---------------------------------------------------
text = Text(root, height=10, width=80)
text.place(x = 21, y = 70)
def deletepackage():
    text.delete(0.0,END)
button = Button(root,text = 'Show', bg = '#f7f7f7')
button.config(command=showpackage)
button.place(x = 200, y = 240)

button = Button(root,text = 'delete', bg = '#f7f7f7')
button.config(command=deletepackage)
button.place(x = 250, y = 240)
# ===================================================
Label(root, text = sys.platform, bg = '#ccc')
# ---------------------------------------------------
root.mainloop() # Run widget
