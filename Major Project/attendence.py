from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


import customtkinter as ctk



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognisation System")

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        #use this to choose random rgb color in bg
        mycolor = '#%02x%02x%02x' % (32,32,32) # set your favourite rgb color
        mycolor2 = '#222' # or use hex if you prefe



        # main bg image
        img3 = Image.open(r"images\desktop-wallpaper-dark-and-background-dark-for-pc.jpg")
        img3 = img3.resize((1530, 790), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=790)

        #title
        
        title_lbl = ctk.CTkLabel(master=root,bg_color="transparent",height=25,fg_color="black",text="ATTENDANCE MANAGEMENT SYSTEM", font=("Century Gothic", 35, "bold"))
        title_lbl.place(x=380, y=0)


        # first image
        img = Image.open(r"images\BestFacialRecognition.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=45, width=450, height=130)
        
        # second image
        img1 = Image.open(r"images\Facial-Recognition-–-Shaping-the-future-of-Identity-Verification-Market-825x500.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=450, y=45, width=480, height=130)

        # third image
        img2 = Image.open(r"images\1221sm-iapp-sectec-lively-facial-facial-recognition-law.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=930, y=45, width=430, height=130)

#left lable back frame for round corner
        Left_frame1=ctk.CTkFrame(master=root,width=660,height=536,border_width=2,fg_color="black",corner_radius=20)
        Left_frame1.place(x=14,y=182)

        #left lable frame

        Left_frame=LabelFrame(root,bd=0,bg="black",fg="white",relief=RIDGE,text="Student Attendence Details",font=("Century Gothic",16,"bold"))
        Left_frame.place(x=23,y=187,width=644,height=525)


# left inner border
        class_student=LabelFrame(Left_frame,bd=2,bg="black",fg="white",relief=RIDGE,text="Student Information",font=("Century Gothic",14,"bold"))
        class_student.place(x=10,y=10,width=620,height=370)

#attendanceID
        attendanceID=ctk.CTkLabel(class_student,text="attendanceID :",font=("Century Gothic",16,"bold"))
        attendanceID.grid(row=0,column=0,padx=10,pady=15,sticky=W)

        StudentId_entry=ctk.CTkEntry(master=attendanceID,font=("Century Gothic",14,"bold"))
        StudentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        #rollLabel
        rollLabel=ctk.CTkLabel(class_student,text="Roll :",font=("Century Gothic",16,"bold"))
        rollLabel.grid(row=0,column=2,padx=1,sticky=W)

        Student_name_entry=ctk.CTkEntry(master=rollLabel,font=("Century Gothic",14,"bold"))
        Student_name_entry.grid(row=0,column=3,padx=10,sticky=W)

        #Name
        nameLabel=ctk.CTkLabel(class_student,text="Name :",font=("Century Gothic",16,"bold"))
        nameLabel.grid(row=1,column=0,padx=10,sticky=W)

        Roll_no_entry=ctk.CTkEntry(master=nameLabel,font=("Century Gothic",14,"bold"))
        Roll_no_entry.grid(row=0,column=1,padx=30,sticky=W)

        #depLabel
        depLabel=ctk.CTkLabel(class_student,text="Department :",font=("Century Gothic",16,"bold"))
        depLabel.grid(row=1,column=2,padx=10,sticky=W)

        Div_entry=ctk.CTkEntry(master=depLabel,font=("Century Gothic",14,"bold"))
        Div_entry.grid(row=0,column=3,padx=20,sticky=W)

        #Time
        timeLabel=ctk.CTkLabel(class_student,text="Time :",font=("Century Gothic",16,"bold"))
        timeLabel.grid(row=2,column=0,padx=10,sticky=W)

        dob_entry=ctk.CTkEntry(master=timeLabel,font=("Century Gothic",14,"bold"))
        dob_entry.grid(row=2,column=1,padx=54,pady=15,sticky=W)

        #Date
        dateLabel=ctk.CTkLabel(class_student,text="Date :",font=("Century Gothic",16,"bold"))
        dateLabel.grid(row=2,column=2,padx=10,sticky=W)

        Address_entry=ctk.CTkEntry(master=dateLabel,font=("Century Gothic",14,"bold"))
        Address_entry.grid(row=2,column=3,padx=(60,0),sticky=W)

        #attendance
        attendanceLabel=ctk.CTkLabel(class_student,text="attendance :",font=("Century Gothic",16,"bold"))
        attendanceLabel.grid(row=3,column=0,sticky=W)

        sem_combo=ctk.CTkComboBox(class_student,values=["Present","Absent"],font=("Century Gothic",14,"bold"),state="readonly")
        sem_combo.set("Status")
        sem_combo.grid(row=3,column=1,sticky=W)

        #button frame
        btn_frame=Frame(Left_frame1,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=500,width=715,height=35)

        save_btn=Button(btn_frame,text="Import csv",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)





if __name__=="__main__":
    root=ctk.CTk()
    obj=Student(root)
    root.mainloop()