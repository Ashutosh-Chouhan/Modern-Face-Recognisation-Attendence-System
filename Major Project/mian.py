from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition


import customtkinter as ctk

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x780+0+0")
        self.root.title("Face Recognition System")
        self.root.state("withdrawn")


        #use this to choose random rgb color in bg
        mycolor = '#%02x%02x%02x' % (32,32,32) # set your favourite rgb color
        mycolor2 = '#222' # or use hex if you prefe
        

        # main bg image
        img3 = Image.open(r"Main Page images\desktop-wallpaper-dark-and-background-dark-for-pc.jpg")
        img3 = img3.resize((1530, 790), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=790)
        
        #title
        title_lbl = Label(bg="black",fg="White",text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("Century Gothic", 30, "bold"))
        title_lbl.place(x=180, y=0, height=45)

        # first image
        img = Image.open(r"Main Page images\facial-recognition-connected-real-estate.png")
        img = img.resize((1530, 790), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=-20, y=45, width=1530, height=130)
        

# black frame middle
        mid_frame1=ctk.CTkFrame(master=root,width=1320,height=550,border_width=2,fg_color="black",corner_radius=20)
        mid_frame1.place(x=14,y=182)
        
    # student button
        img4 = Image.open(r"Main Page images\Untitled-1-01-e1593183927231.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1 = Button(mid_frame1, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150, y=20, width=220, height=220)
        
        b1_1 = ctk.CTkButton(mid_frame1, text="Student Details",command=self.student_details,cursor="hand2", font=("times new roman", 15, "bold"), bg_color="black", fg_color= mycolor2,width=220)
        b1_1.place(x=150, y=240)

    # detect_face button
        img5 = Image.open(r"Main Page images\BiometricResize.webp")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b2 = Button(mid_frame1, image=self.photoimg5,command=self.face_data, cursor="hand2")
        b2.place(x=550, y=20, width=220, height=220)
        
        b2_1 =ctk.CTkButton(mid_frame1, text="Face Detector",command=self.face_data, cursor="hand2", font=("times new roman", 15, "bold"), bg_color="black", fg_color= mycolor2,width=220)
        b2_1.place(x=550, y=240)
        
        
        
    # Attendence_face button
        img6 = Image.open(r"Main Page images\360_F_308919862_hgbRZeYvO348NYDH7AsQcQ7AHSDbNZ7u.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b2 = Button(mid_frame1, image=self.photoimg6, cursor="hand2")
        b2.place(x=950, y=20, width=220, height=220)
        
        b2_1 = ctk.CTkButton(mid_frame1, text="Attendence", cursor="hand2", font=("times new roman", 15, "bold"), bg_color="black", fg_color= mycolor2,width=220)
        b2_1.place(x=950, y=240)


# Train Face button
        img8 = Image.open(r"Main Page images\1 What is Training Data_.webp")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1 = Button(mid_frame1, image=self.photoimg8,command=self.train_data,cursor="hand2", width=220, height=220)
        b1.place(x=100, y=280)
        
        b1_1 = ctk.CTkButton(mid_frame1, text="Train Data",command=self.train_data,cursor="hand2", font=("times new roman", 15, "bold"), bg_color="black", fg_color= mycolor2,width=227)
        b1_1.place(x=100, y=506)



 # photos button
        img9 = Image.open(r"Main Page images\Data-Collection.png")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b2 = Button(mid_frame1, image=self.photoimg9,command=self.open_img, cursor="hand2",width=220, height=220)
        b2.place(x=400, y=280)
        
        b2_1 = ctk.CTkButton(mid_frame1, text="Photos",command=self.open_img, cursor="hand2", font=("times new roman", 15, "bold"), bg_color="black", fg_color= mycolor2,width=227)
        b2_1.place(x=400, y=506)
        
        
    
        
    # Developer_face button
        img10 = Image.open(r"Main Page images\Developer.webp")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b2 = Button(mid_frame1, image=self.photoimg10, cursor="hand2", width=220, height=220)
        b2.place(x=700, y=280)
        
        b2_1 = ctk.CTkButton(mid_frame1, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg_color="black", fg_color= mycolor2,width=227)
        b2_1.place(x=700, y=506)
        
    # Exit button
        img11 = Image.open(r"Main Page images\360_F_36866398_9WNUQeGthhA2RcwjPYnyh0L0dtHCyLyx.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b2 = Button(mid_frame1, image=self.photoimg11, cursor="hand2", width=220, height=220)
        b2.place(x=1000, y=280)
        
        b2_1 = ctk.CTkButton(mid_frame1, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg_color="black", fg_color= mycolor2,width=227)
        b2_1.place(x=1000, y=506)





# -----------------Function Buttons ------------------------

    # Student details new window
    def student_details(self):
        self.new_window= Toplevel(self.root)
        self.app = Student(self.new_window)  # create window if its None or destroyed
        

    # for photo directry new window
    
    def open_img(self):
        os.startfile("Sample Images")
    
    # train data new window

    def train_data(self):
        self.new_window= Toplevel(self.root)
        self.app = Train(self.new_window)

    #recognisation data new window

    def face_data(self):
        self.new_window= Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)










if __name__=="__main__":
    root=ctk.CTk()
    obj=Face_Recognition_System(root)
    root.mainloop()
