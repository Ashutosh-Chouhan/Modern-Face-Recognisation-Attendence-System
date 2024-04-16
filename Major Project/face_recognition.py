from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np #NumPy daal lena 

import customtkinter as ctk

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        mycolor2 = '#00001c'

        
        # main bg image
        img3 = Image.open(r"images\Facial-Recognition-–-Shaping-the-future-of-Identity-Verification-Market-825x500.jpg")
        img3 = img3.resize((1530, 790), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=790)
        
        #title
        title_lbl = ctk.CTkLabel(master=root,bg_color="transparent",height=25,fg_color="black",text="FACE RECOGNITION", font=("Century Gothic", 35, "bold"))
        title_lbl.place(x=520, y=0)

        #button
        b1_1=ctk.CTkButton(self.root,text="Face Recognition",corner_radius=50,cursor="hand2",font=("times new roman",18,"bold"),bg_color=mycolor2,width=50,height=150)
        b1_1.place(x=125,y=330)

        #button
        b1_1=ctk.CTkButton(self.root,text="Face Recognition",command=self.face_recog,corner_radius=50,cursor="hand2",font=("times new roman",18,"bold"),bg_color=mycolor2,width=50,height=150)
        b1_1.place(x=125,y=330)


     # ============================= Attendance =============================

    def mark_attendance(self,i,r,n,d):
        with open("stud_attendence.csv","r+",newline="\n")as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((",")) 
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")


    # ========================== Face Recognition ==========================

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))


                #ye mysql connection wala code sahi se poora kardena student.py se leke
                conn= mysql.connector.connect(host="localhost",user="root",password="mydb123",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Student_Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()

                my_cursor.execute("select Roll_No from student where Student_id="+str(id))
                r = my_cursor.fetchone()

                my_cursor.execute("select Department from student where Student_id="+str(id))
                d = my_cursor.fetchone()

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()

                if n and r and d and i:  # Check if any result is fetched
                    n = n[0]  # Assuming fetchone() returns a single value
                    r = r[0]
                    d = d[0]
                    i = i[0]

                if confidence > 77:
                    cv2.putText(img, f"Student_id: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll_No: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Student_Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)


                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        #haarcascade file ka path h
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")     

        cap=cv2.VideoCapture(0)


        while True:
            ret, img = cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome TO face Recognition", img)
    
            key = cv2.waitKey(1)
            if key == ord('q'):  # Press 'q' to exit
                break
            
            # Check if the window is open or closed
            if cv2.getWindowProperty("Welcome TO face Recognition", cv2.WND_PROP_VISIBLE) < 1:
                break  # Break the loop when window is closed
            
        cap.release()
        cv2.destroyAllWindows()
   





        
if __name__ == "__main__":
    root=ctk.CTk()
    obj=Face_Recognition(root)
    root.mainloop()