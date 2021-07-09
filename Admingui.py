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

def resetpass():
    email=uservalue.get()
    auth.send_password_reset_email(email)
    print("We have sent an email, check your inbox ")
    text_label = Label(root, text="Password reset mail has been sent to your\nrespective email id", fg="green", font="TimesNewRoman 8 bold",
                       pady=9)
    text_label.grid(row=9, column=7)

def getvals():
    email=uservalue.get()
    password=passvalue.get()
    try:
         user = auth.sign_in_with_email_and_password(email, password)
         os.system('python GUIFbase.py')
         print("successful")

    except:
        text_label = Label(root, text="OOPS INVALID USERNAME OR PASSWORD!!!", fg="red",bg="white", font="TimesNewRoman 8 bold",
                           pady=9)
        text_label.grid(row=9, column=7)

    # if(uservalue.get()=="admin" and passvalue.get()=="admin"):
    #     os.system('python GUIFbase.py')
    # else:
    #     text_label = Label(root, text="OOPS INVALID USERNAME OR PASSWORD", fg="red", font="TimesNewRoman 8 bold",pady=9)
    #     text_label.grid(row=8,column=7)


root=Tk();
root.title("Welcome ADMIN")
root.geometry("590x300")
root.maxsize(590,300)
root.minsize(520,300)

p1 = PhotoImage(file='download.png')
root.iconphoto(False, p1)

text_label = Label(root, text="WELCOME ADMIN", fg="black", font="TimesNewRoman 13 bold",pady=15,padx=20)
text_label.grid(row=0,column=7)

user=Label(root,text="Email",pady=5,padx=30).grid(row=1,column=5)
Password=Label(root,text="Password",pady=5,padx=30).grid(row=3,column=5)


uservalue=StringVar();
passvalue=StringVar();

userentry=Entry(root,textvariable=uservalue).grid(row=1,column=8)
passentry=Entry(root,textvariable=passvalue,show="*").grid(row=3,column=8)

Button(text="LOG IN",command=getvals,padx=20).grid(row=10,column=6)
Button(text="Forgot Password",command=resetpass,padx=20).grid(row=10,column=7)

# b2=Button(root,text="LOG IN",borderwidth=2,font="TimesNewRoman 11 bold")
# b2.pack(side=RIGHT,padx=40,pady=10)


root.mainloop();