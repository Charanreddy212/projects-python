from tkinter import *
from tkinter import messagebox
def ok():
    uname=e1.get()
    password=e2.get()
    
    if (uname=="" or password==""):
        messagebox.showinfo("","blank is not allowed")
    elif (uname=="Admin" and password=="123"):
        messagebox.showinfo("","Login success")
        root.destroy()
    else:
        messagebox.showinfo("","incorrect username or password")
root=Tk()
root.title("Login page")
root.geometry("300x200")
global e1
global e2
Label(root,text="username").place(x=10,y=10)
Label(root,text="password").place(x=10,y=40)
e1=Entry(root)
e1.place(x=140,y=10)
e2=Entry(root)
e2.place(x=140,y=40)
e2.config(show="*")
Button(root,text="login",command=ok,height=1,width=13).place(x=10,y=100)
root.mainloop() 


