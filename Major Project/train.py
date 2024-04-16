from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import os
import numpy as np 
import cv2

import customtkinter as ctk

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        mycolor2 = '#00001c'

        img3 = Image.open(r"images\image.webp")
        img3 = img3.resize((1530, 790), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=790)

        title_lbl = ctk.CTkLabel(master=root, bg_color="black", width=1500, height=35, fg_color="black",
                                 text="Train Data", font=("Century Gothic", 35, "bold"))
        title_lbl.place(x=-10, y=0)

        b1_1 = ctk.CTkButton(self.root, text="Click To Train", corner_radius=100, command=self.train_classifier,
                             bg_color=mycolor2, cursor="hand2", width=50, height=325, font=("times new roman", 30, "bold"))
        b1_1.place(x=125, y=296)

    def train_classifier(self):
        data_dir = "Sample Images"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        if len(path) <= 1:  # If less than or equal to 1 sample, show an error
            messagebox.showerror("Error", "Empty training data was given. You'll need more than one sample to learn a model.")
            return

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')   # Gray scale image 
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        
        ids = np.array(ids)

        # Train the classifier and save the model
        clf = cv2.face.LBPHFaceRecognizer_create()    
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
