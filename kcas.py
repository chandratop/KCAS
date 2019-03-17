# Modules imported

from Tkinter import *   # For GUI
import tkMessageBox     # For GUI Popup message box
import os               # Starting file
import ttk
import datetime

# Variables





# Functions

"""def login():
    def check():
        pwentry = pw.get()
        now = str(datetime.datetime.today())
        passwd = now[11:13]+now[8:10]
        if passwd != pwentry:
            tkMessageBox.showerror('ERROR','INCORRECT PASSWORD')
            login.destroy()
        else:
            EDwindow()
    login = Tk()
    un = StringVar()
    pw = StringVar()
    
    
    login.title("Login")
    login.configure(bg="slategray")
    login.geometry("240x100+530+300")
    username =Label(login,text="Username",bg="slategray",font=('',12),padx=10,pady=5).grid(row=0)
    username_entry = ttk.Entry(login,textvariable=un).grid(row=0,column=2)
    password = Label(login,text="Password",bg="slategray",font=('',12),pady=5).grid(row=1,column=0)
    password_entry = ttk.Entry(login,textvariable=pw,show='*').grid(row=1,column=2)
    
    
    login_button = ttk.Button(login,text="Login",command=check).place(x=90,y=70)    
    login.mainloop()

def EDwindow():
    print "OK"
"""
# -----MAIN GUI-----

root = Tk()     # window object

root.title("START PAGE")
root.configure(bg="slategray")
root.geometry("240x100+530+300") # 'x-axis' x 'y-axis' PIXELS
h1 = Label(root,text="KCAS",fg="white",bg="slategray",font=("Century",24)).place(x=70,y=10) # heading1
lg = ttk.Button(root,text="Login").place(x=20,y=60)
nw = ttk.Button(root,text="Sign up").place(x=140,y=60)
del h1
del lg
del nw
root.mainloop()
