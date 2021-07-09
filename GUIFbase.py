from tkinter import *
import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime,date



root=Tk();

root.title("Welcome To F-BASE")
root.geometry("670x300")
root.minsize(670,300)
root.maxsize(700,300)

p1 = PhotoImage(file='download.png')
root.iconphoto(False, p1)


f1=Frame(root)
f1.pack(side=RIGHT,anchor="ne",pady=53,padx=45)

text_label=Label(f1,text="WELCOME TO FBASE",fg="green",bg="white",font="TimesNewRoman 15 bold")
text_label.pack()


text_label2=Label(f1,text="This software is developed and tested by team F-BASE\n All Rights Reserved",font="TimesNewRoman 9")
text_label2.pack(pady=30)

text_label=Label(f1,text="For any Query contact us on : f-base23@gmail.com",fg="green",font="TimesNewRoman 9 italic")
text_label.pack()

b2=Button(f1,text="Exit",borderwidth=2,font="TimesNewRoman 11 bold")
b2.pack(side=RIGHT,padx=20,pady=10)
b2.bind('<Button-1>',quit)

def createnewadmin():
    os.system('python newadmingui.py')

b3=Button(f1,text="Create New Admin",borderwidth=2,font="TimesNewRoman 11 bold",command=createnewadmin).pack(side=RIGHT,padx=(30,10))

photo=PhotoImage(file="imageBasic/logo1.png")
photo_label=Label(image=photo,borderwidth=7,relief=SUNKEN)
photo_label.pack(anchor="nw",pady=47)

def func():
            path = 'imageAttendance'
            images = []
            classNames = []
            myList = os.listdir(path)
            print(myList)


            for cl in myList:
                curImg = cv2.imread(f'{path}/{cl}')
                images.append(curImg)
                classNames.append(os.path.splitext(cl)[0])
            print(classNames)

            def findEncodings(images):
                encodeList = []
                for img in images:
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    encode = face_recognition.face_encodings(img)[0]
                    encodeList.append(encode)
                return encodeList

            def markAttendance(name):
                with open("Attendance.csv", "r+") as f,open("Exit.csv", "r+") as g:
                    myDataList = f.readlines()
                    nameList = []
                    now = datetime.now()
                    dtString = now.strftime('%H:%M:%S')
                    dt = int(dtString[0:2])

                    for line in myDataList:
                        entry = line.split(',')
                        nameList.append(entry[0])

                    if name not in nameList:
                        now = datetime.now()
                        dtString = now.strftime('%H:%M:%S')
                        dt=int(dtString[0:2])
                        dtm=int(dtString[3:5])
                        print(dt,dtm)

                        if (dt>12 and dtm>30):
                            entry="LATE"
                        else :
                            entry="ON TIME"
                        dt2=date.today()
                        f.writelines(f'\n{name},{dtString},{dt2},{entry}')

                    elif name in nameList :
                        if dt>15 and dt<16:
                            now = datetime.now()
                            dtString = now.strftime('%H:%M:%S')
                            dt2=date.today()
                            exit="HALF DAY"
                            g.writelines(f'\n{name},{dtString},{dt2}.{exit}')
                        elif dt>17:
                            now = datetime.now()
                            dtString = now.strftime('%H:%M:%S')
                            dt2 = date.today()
                            exit = "FULL DAY"
                            g.writelines(f'\n{name},{dtString},{dt2}.{exit}')

            encodeListKnown = findEncodings(images)
            print('ENCODING COMPLETE')

            cap = cv2.VideoCapture(0)

            while True:
                success, img = cap.read()
                imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
                imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

                facesCurFrame = face_recognition.face_locations(imgS)
                encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

                for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                    matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                    faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                    # print(faceDis)
                    matchIndex = np.argmin(faceDis)

                    # if matches[matchIndex]:
                    #     name = classNames[matchIndex].upper()
                    #     # print(name)
                    #     y1, x2, y2, x1 = faceLoc
                    #     y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    #     cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 1)
                    #     cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    #     cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                    #     markAttendance(name)
                    if faceDis[matchIndex] < 0.50:
                        name = classNames[matchIndex].upper()
                        markAttendance(name)
                    else:
                        name = 'Unknown'

                    # print(name)
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)


                cv2.imshow('webcam', img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

b1=Button(f1,text="Let's Start",command=func,borderwidth=2,font="TimesNewRoman 11 bold")
b1.pack(side=BOTTOM,pady=10)

root.mainloop()


