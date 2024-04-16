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

        ###Treeview Customisation (theme colors are selected)



        # --------variables-----------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_div=StringVar()
        self.var_dob=StringVar()
        self.var_address=StringVar()
        self.var_gender=StringVar()

        # main bg image
        img3 = Image.open(r"images\desktop-wallpaper-dark-and-background-dark-for-pc.jpg")
        img3 = img3.resize((1530, 790), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=790)

        #title
        
        title_lbl = ctk.CTkLabel(master=root,bg_color="transparent",height=25,fg_color="black",text="Student Details", font=("Century Gothic", 35, "bold"))
        title_lbl.place(x=520, y=0)

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

        Left_frame=LabelFrame(root,bd=0,bg="black",fg="white",relief=RIDGE,text="Student Details",font=("Century Gothic",16,"bold"))
        Left_frame.place(x=23,y=187,width=644,height=525)

    # current course
        Current_course=LabelFrame(Left_frame,bd=2,bg="black",fg="white",relief=RIDGE,text="Student Course",font=("Century Gothic",14,"bold"))
        Current_course.place(x=10,y=10,width=620,height=150)

        #department
        dep_lable=ctk.CTkLabel(Current_course,text="Department :",font=("Century Gothic",15,"bold"))
        dep_lable.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ctk.CTkComboBox(Current_course,variable=self.var_dep,values=["Computer","IT","Mechnical","Civil"],font=("Century Gothic",14,"bold"),state="readonly")
        dep_combo.set("Select Department")
        dep_combo.grid(row=0,column=1,padx=0,pady=15,sticky=W)

        #Course
        course_lable=ctk.CTkLabel(Current_course,text="Course :",font=("Century Gothic",16,"bold"),width=17)
        course_lable.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ctk.CTkComboBox(Current_course,variable=self.var_course,values=["TE","SE","FE","BE"],font=("Century Gothic",14,"bold"),state="readonly")
        course_combo.set("Select Course")
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Year
        year_lable=ctk.CTkLabel(Current_course,text="Year :",font=("Century Gothic",16,"bold"),width=17)
        year_lable.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ctk.CTkComboBox(Current_course,variable=self.var_year,values=["2020-21","2021-22","2022-23","2023-24"],font=("Century Gothic",14,"bold"),state="readonly")
        year_combo.set("Select Year")
        year_combo.grid(row=1,column=1,padx=2,pady=15,sticky=W)


        #Semester
        sem_lable=ctk.CTkLabel(Current_course,text="Semester :",font=("Century Gothic",16,"bold"),width=17)
        sem_lable.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ctk.CTkComboBox(Current_course,variable=self.var_sem,values=["1st","2nd","3rd","4th","5th","6th"],font=("Century Gothic",14,"bold"),state="readonly")
        sem_combo.set("Select Semester")
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

    #Class Student information
        class_student=LabelFrame(Left_frame,bd=2,bg="black",fg="white",relief=RIDGE,text="Student Information",font=("Century Gothic",14,"bold"))
        class_student.place(x=10,y=160,width=620,height=240)

        #student id
        StudentId_lable=ctk.CTkLabel(class_student,text="Student Id :",font=("Century Gothic",16,"bold"))
        StudentId_lable.grid(row=0,column=0,padx=10,pady=15,sticky=W)

        StudentId_entry=ctk.CTkEntry(master=StudentId_lable,textvariable=self.var_id,placeholder_text="0823CS201XXX",font=("Century Gothic",14,"bold"))
        StudentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        #student name
        Student_name_lable=ctk.CTkLabel(class_student,text="Student Name :",font=("Century Gothic",16,"bold"))
        Student_name_lable.grid(row=0,column=2,padx=10,sticky=W)

        Student_name_entry=ctk.CTkEntry(master=Student_name_lable,textvariable=self.var_name,placeholder_text="abc",font=("Century Gothic",14,"bold"))
        Student_name_entry.grid(row=0,column=3,padx=10,sticky=W)

        #student rollno
        Roll_no_lable=ctk.CTkLabel(class_student,text="Roll No. :",font=("Century Gothic",16,"bold"))
        Roll_no_lable.grid(row=1,column=0,padx=10,sticky=W)

        Roll_no_entry=ctk.CTkEntry(master=Roll_no_lable,textvariable=self.var_roll,placeholder_text="XX",font=("Century Gothic",14,"bold"))
        Roll_no_entry.grid(row=0,column=1,padx=30,sticky=W)

        #student Division
        Div_lable=ctk.CTkLabel(class_student,text="Class Division :",font=("Century Gothic",16,"bold"))
        Div_lable.grid(row=1,column=2,padx=10,sticky=W)

        Div_entry=ctk.CTkEntry(master=Div_lable,textvariable=self.var_div,placeholder_text="A/B/C",font=("Century Gothic",14,"bold"))
        Div_entry.grid(row=0,column=3,padx=20,sticky=W)

        #student DOB
        dob_lable=ctk.CTkLabel(class_student,text="DOB :",font=("Century Gothic",16,"bold"))
        dob_lable.grid(row=2,column=0,padx=10,sticky=W)

        dob_entry=ctk.CTkEntry(master=dob_lable,textvariable=self.var_dob,placeholder_text="DD/MM/YYYY",font=("Century Gothic",14,"bold"))
        dob_entry.grid(row=0,column=1,padx=54,pady=15,sticky=W)

        #Address
        Address_lable=ctk.CTkLabel(class_student,text="Address :",font=("Century Gothic",16,"bold"))
        Address_lable.grid(row=2,column=2,padx=10,sticky=W)

        Address_entry=ctk.CTkEntry(master=Address_lable,textvariable=self.var_address,placeholder_text="Home Address",font=("Century Gothic",14,"bold"))
        Address_entry.grid(row=0,column=3,padx=(60,0),sticky=W)

        #Gender
        Gender_lable=ctk.CTkLabel(class_student,text="Gender :",font=("Century Gothic",16,"bold"))
        Gender_lable.grid(row=3,column=2,padx=10,sticky=W)

        Gender_entry=ctk.CTkEntry(master=Gender_lable,textvariable=self.var_gender,placeholder_text="Gender",font=("Century Gothic",14,"bold"))
        Gender_entry.grid(row=0,column=3,padx=(60,0),sticky=W)


#radio button

        self.var_radio1=StringVar()
        Radiobutton1=ctk.CTkRadioButton(master=class_student,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        Radiobutton1.place(x=10,y=150)

        
        Radiobutton2=ctk.CTkRadioButton(master=class_student,variable=self.var_radio1,text="No Photo Sample",value="No")
        Radiobutton2.place(x=10,y=180)

    #buttons
        Save=ctk.CTkButton(Left_frame,text="Save",command= self.add_data)
        Save.place(x=10,y=410)

        Delete=ctk.CTkButton(Left_frame,text="Delete",command= self.delete_data)
        Delete.place(x=164,y=410)

        Update=ctk.CTkButton(Left_frame,text="Update",command= self.update_data)
        Update.place(x=322,y=410)

        Reset=ctk.CTkButton(Left_frame,text="Reset",command= self.reset_data)
        Reset.place(x=478,y=410)

        #Photo sample btn
        Take=ctk.CTkButton(Left_frame,text="Take Photo Sample",width=296,command=self.generate_dataset)
        Take.place(x=10,y=450)

        Update_sample=ctk.CTkButton(Left_frame,text="Update Photo Sample",width=296)
        Update_sample.place(x=322,y=450)

#Right lable back frame for round corner
        Right_frame=ctk.CTkFrame(master=root,width=665,height=536,border_width=2,fg_color="black",corner_radius=20)
        Right_frame.place(x=685,y=182)

#Right lable frame

        Right_frame=LabelFrame(root,bd=0,bg="black",fg="white",relief=RIDGE,text="Student Details",font=("Century Gothic",16,"bold"))
        Right_frame.place(x=698,y=187,width=644,height=525)
        
        
    #----Searching System frame
        Search_frame=LabelFrame(Right_frame,bd=2,bg="black",fg="white",relief=RIDGE,text="Search System",font=("Century Gothic",14,"bold"))
        Search_frame.place(x=10,y=10,width=620,height=150)


        #Search Entry
        Entry_entry=ctk.CTkEntry(Search_frame,placeholder_text="Search here",font=("Century Gothic",14,"bold"),width=580)
        Entry_entry.place(x=10,y=15)

        Search=ctk.CTkButton(Search_frame,text="Search",width=110,height=28,border_color="gray",border_width=2)
        Search.place(x=478,y=15)


        #Search By combobox
        search_label=ctk.CTkLabel(Search_frame,text="Search By :",font=("Century Gothic",15,"bold"))
        search_label.place(x=10,y=70)

        course_combo=ctk.CTkComboBox(Search_frame,values=["Student Id","Roll No","Division"],font=("Century Gothic",14,"bold"),state="readonly",width=200)
        course_combo.set("Select")
        course_combo.place(x=100,y=70)

        #search btn
        Search=ctk.CTkButton(Search_frame,text="Search",width=130)
        Search.place(x=310,y=70)

        ShowAll=ctk.CTkButton(Search_frame,text="Show All",width=130)
        ShowAll.place(x=460,y=70)

    #----table frame

        Table_frame=LabelFrame(Right_frame,bd=2,bg="white",fg="white",relief=RIDGE,font=("Century Gothic",14,"bold"))
        Table_frame.place(x=10,y=170,width=620,height=320)

        #Scroll bar
        scroll_x=ctk.CTkScrollbar(Table_frame,orientation=HORIZONTAL)
        scroll_y=ctk.CTkScrollbar(Table_frame,orientation=VERTICAL)

        #Treeview colorchange(customise Treeview)
        style = ttk.Style()  

        #pick background theam for treeview
        style.theme_use("default")
        style.configure("Treeview", background="black", foreground="white", fieldbackground=mycolor, borderwidth=0)
        style.map('Treeview', background=[('selected', "black")], foreground=[('selected', "blue")])
        root.bind("<<TreeviewSelect>>", lambda event: root.focus_set())
        



        #craeating Treeview table
        self.student_table=ttk.Treeview(Table_frame,columns=("dep","course","year","sem","id","name","roll","div","dob","address","gender","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.configure(command=self.student_table.xview)
        scroll_y.configure(command=self.student_table.yview)



        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student id")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        #Set heading width in table
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.column("dep",width=100)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        



# --------------function declaration-----------------------

    def add_data(self):
        if self.var_dep.get=="Select Department" or self.var_name.get()=="" or self.var_id.get()==""or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent= self.root)
        else:
            try:
                conn= mysql.connector.connect(host="localhost",user="root",password="mydb123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_roll.get(),
                    self.var_div.get(),
                    self.var_dob.get(),
                    self.var_address.get(),
                    self.var_gender.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Sucessfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # -------------fetch data ---------------
    def fetch_data(self):
        conn= mysql.connector.connect(host="localhost",user="root",password="mydb123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ---------------get cursor------------- take entry from table and put into student details entry
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_roll.set(data[6])
        self.var_div.set(data[7])
        self.var_dob.set(data[8])
        self.var_address.set(data[9])
        self.var_gender.set(data[10])
        self.var_radio1.set(data[11])

    # ---------update function ------------------
    def update_data(self):
        if self.var_dep.get=="Select Department" or self.var_name.get()=="" or self.var_id.get()==""or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn= mysql.connector.connect(host="localhost",user="root",password="mydb123",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Student_Name=%s,Roll_No=%s,Division=%s,DOB=%s,Address=%s,Gender=%s,PhotoSampleStatus=%s where Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_roll.get(),
                        self.var_div.get(),                    
                        self.var_dob.get(),
                        self.var_address.get(),
                        self.var_gender.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    ))
                else:
                    if not Update:
                        return   
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root) 
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



    #---------------delete function-------------

    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student details", parent=self.root)
                if delete>0:
                    conn= mysql.connector.connect(host="localhost",user="root",password="mydb123",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student Where Student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Delete Student Details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #-------------reset data------------
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_roll.set(""),
        self.var_div.set("Select Devision"),
        self.var_dob.set(""),
        self.var_address.set(""),
        self.var_gender.set("Male"),
        self.var_radio1.set("")


    # ____________Generate Dataset or take an photo sample______________
    def generate_dataset(self):
        if self.var_dep.get=="Select Department" or self.var_name.get()=="" or self.var_id.get()==""or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn= mysql.connector.connect(host="localhost",user="root",password="mydb123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Student_Name=%s,Roll_No=%s,Division=%s,DOB=%s,Address=%s,Gender=%s,PhotoSampleStatus=%s where Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_roll.get(),
                        self.var_div.get(),                    
                        self.var_dob.get(),
                        self.var_address.get(),
                        self.var_gender.get(),
                        self.var_radio1.get(),
                        self.var_id.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()

                # =============Load face frontal from opencv==============

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5) #scaling factor=1.3, minimum neigbor=5

                    for(x,y,w,h)in faces:
                        face_cropped=img[y:y+h,x:x+w] # y:cropping hight, x:croppingwidth
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                    
                        face=cv2.resize(face_cropped(my_frame),(450,450)) #450 is width and hight for cropped image
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Sample Images/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Image",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets is completed")
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


                

if __name__=="__main__":
    root=ctk.CTk()
    obj=Student(root)
    root.mainloop()
