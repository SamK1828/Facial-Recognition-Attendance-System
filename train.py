from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql as mysql
import cv2 #Computer Vision Library
import os
import numpy as np
import customtkinter

ft=("verdana",11,"bold")
ft1=("verdana",13,"bold")

class Train:
    def __init__(self,root):
        self.root=root
        #self.root.geometry("1366x900+0+0")
        #screen_width = self.root.winfo_screenwidth()-100
        #screen_height = self.root.winfo_screenheight()-100
        screen_width = 1530
        screen_height = 780
        #Set the size of the window based on the screen resolution
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.title("__Train Data Section__")
        
        # This part is image labels setting start 
        #First Image
        img=Image.open("Images_GUI/banner.jpg")
        img=img.resize((screen_width//2,135),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        
        
        f_lb1 = Label(self.root,image=self.photoimage)
        f_lb1.place(x=0,y=0,width=screen_width//2,height=135)
        
        #Second Image
        img1=Image.open("Images_GUI/banner1.jpg")
        img1=img1.resize((screen_width//2,135),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        
        
        f_lb1 = Label(self.root,image=self.photoimage1)
        f_lb1.place(x=screen_width//2,y=0,width=screen_width//2,height=135)
        
        # backgorund image 
        bg1=Image.open("Images_GUI/bg2.jpg")
        bg1=bg1.resize((screen_width,screen_height-130),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)
        
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=135,width=screen_width,height=screen_height-130)
        
        #Title 
        title_lbl=Label(self.root,text="DATA SET TRAINING SECTION",font=("VERDENA",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=136,width=screen_width,height=50)
        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open("Images_GUI/tt_button.png")
        std_img_btn=std_img_btn.resize((200,200),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)
        std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(x=650,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("verdena",16,"bold"),bg="white",fg="green")
        std_b1_1.place(x=650,y=380,width=180,height=45)
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #Gray Scale Image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1]) 
            #id=int(os.path.split(image)[1].split('.')[0])
            #C:\Users\HP\Music\Documents\Programming\Saved of Python\MP\data\user.1.1.jpg
            #0                                                               1
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        #========================== Train the Classifier and Save===============================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed ...")
        self.root.destroy()
        
if __name__ == "__main__":  
    root=Tk()
    obj=Train(root)
    root.resizable(False,False)
    root.mainloop()
              