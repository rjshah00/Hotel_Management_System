from tkinter import *
import tkinter.font as font
from main import back

def main_page():
    username=username_entry.get()
    password=password_entry.get()
    temp=back.login_search(username,password)
    if(temp==1):
        popup=Tk()
        popup.title("MessageBox")
        popup.geometry("100x50")
        valid_label=Label(popup,text="Logged in successfull.",bg='white',fg='green')
        valid_label.pack()
        valid_btn=Button(popup,text="Okay",command=popup.destroy)
        valid_btn.pack()
        root.destroy()
    else:
        popup=Tk()
        popup.title("MessageBox")
        popup.geometry("100x50")
        invalid_label=Label(popup,text="invalid input please check username and password entered.",bg='white',fg='red')
        invalid_label.pack()
        invalid_btn=Button(popup,text="Log in Again",command=popup.destroy)
        invalid_btn.pack()
        username_entry.delete(0,END)
        password_entry.delete(0,END)

root=Tk()
root.title("Hotel Management")
root.configure(bg='#1D085F')
root.geometry("900x900")
myFont = font.Font(family='Helvetica')
myFont2= font.Font(size='50')
myFont1= font.Font(weight='bold')
Lab=Label(root,text="Hotel Management System",bg='#D4D7DD')
Lab['font']=myFont
Lab['font']=myFont1
Lab['font']=myFont2
Lab.pack()
myFont3= font.Font(size='20')

frame=LabelFrame(root,text="Login Page",padx=60,pady=50,bg='#1D085F')
frame.configure(bg='#C1E8ED')
frame.pack(padx=100,pady=180)

admin_label=Label(frame,text="Username :  ",textvariable="username",bg='#C1E8ED')
admin_label['font']=myFont
admin_label['font']=myFont1
admin_label['font']=myFont3
admin_label.grid(row=5,column=7)

password_label=Label(frame,text="Password :  ",textvariable="password",bg='#C1E8ED')
password_label['font']=myFont
password_label['font']=myFont1
password_label['font']=myFont3
password_label.grid(row=6,column=7)

username_entry=Entry(frame,width="30")
username_entry.grid(row=5,column=8)

password_entry=Entry(frame,width="30",show="*")
password_entry.grid(row=6,column=8)

submit_button=Button(frame,text="Log In",padx=10,bg='#1D085F',fg='white',command=main_page)
submit_button.grid(row=10,column=8,columnspan=2,padx=2,ipadx=2)

root.mainloop()















