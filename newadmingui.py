from tkinter import *
import os
import pyrebase


firebaseConfig = {
    "apiKey": "AIzaSyDj1qEFM2HY_brmAR-czKu3IT1gqWYSoWU",
    "authDomain": "fbase-2452d.firebaseapp.com",
    "projectId": "fbase-2452d",
    "storageBucket": "fbase-2452d.appspot.com",
    "messagingSenderId": "416946115553",
    "appId": "1:416946115553:web:8b93bb2bf8c250ef3178a0",
    "measurementId": "G-0DDN2V48KW",
    'databaseURL' : "https://fbase-2452d-default-rtdb.firebaseio.com/"
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

root=Tk();
root.title("Create New Admin")
root.geometry("600x300")
root.maxsize(600,300)
root.minsize(600,300)

def func1():
    email = uservalue.get()
    password = passvalue.get()
    password2=passvalue2.get()
    if(password==password2 and password!=""):
        text_label = Label(root, text="New Admin Created", fg="green",
                           font="TimesNewRoman 12 bold",
                           pady=9)
        text_label.grid(row=11, column=7)
        auth.create_user_with_email_and_password(email,password)
        os.system('python Admingui.py')
    else:
        text_label = Label(root, text="Please check the details", fg="red",
                           font="TimesNewRoman 10 bold",
                           pady=9)
        text_label.grid(row=11, column=7)

p1 = PhotoImage(file='download.png')
root.iconphoto(False, p1)

text_label = Label(root, text="Create New ADMIN-Its Good to work as a team", fg="black", font="TimesNewRoman 13 bold",pady=15,padx=20)
text_label.grid(row=0,column=7)

user=Label(root,text="Email",pady=5,padx=30).grid(row=1,column=6)
Password=Label(root,text="Password",pady=5,padx=30).grid(row=3,column=6)
ReEnterPassword=Label(root,text="ReEnterPassword",pady=5,padx=30).grid(row=5,column=6)

uservalue=StringVar();
passvalue=StringVar();
passvalue2=StringVar();

userentry=Entry(root,textvariable=uservalue).grid(row=1,column=7)
passentry=Entry(root,textvariable=passvalue,show="*").grid(row=3,column=7)
passentry=Entry(root,textvariable=passvalue2,show="*").grid(row=5,column=7)

Button(text="Create Admin",command=func1,padx=20).grid(row=10,column=7)
# Button(text="Forgot Password",command=resetpass,padx=20).grid(row=10,column=7)
# Button(text="Create another admin",command=resetpass,padx=20).grid(row=10,column=8)
# b2=Button(root,text="LOG IN",borderwidth=2,font="TimesNewRoman 11 bold")
# b2.pack(side=RIGHT,padx=40,pady=10)


root.mainloop();