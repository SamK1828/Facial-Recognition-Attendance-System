from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os
import customtkinter as ctk
ft=("VERDENA",18,"bold")
class Developer:
    def __init__(self,root):
        self.root=root
        screen_width = 1530
        screen_height = 780
        #Set the size of the window based on the screen resolution
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # backgorund image 
        bg1=Image.open("Images_GUI/bg5.jpg")
        bg1=bg1.resize((screen_width,screen_height),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=screen_width,height=screen_height)
        
        #Back Button
        bk_img=Image.open("Images_GUI/bb1.jpg")
        bk_img=bk_img.resize((120,40),Image.LANCZOS)
        self.pback=ImageTk.PhotoImage(bk_img)

        bk_button=Button(bg_img,command=self.root.destroy,image=self.pback,cursor="hand2")
        bk_button.place(x=50,y=100,width=120,height=40)
        #title section
        title_lb1 = Label(bg_img,text="Developer Section",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=screen_width,height=45)

        # # Create buttons below the section 
        # # ------------------------------------------------------------------------------------------------------------------- 
        # Developer 1 Frame
        dev1_frame=Frame(bg_img,bd=2,bg="#002B53")
        dev1_frame.place(x=50,y=200,width=600,height=180)

        dev1_btn=Image.open("Images_GUI/me.jpg")
        dev1_btn=dev1_btn.resize((180,180),Image.LANCZOS)
        self.dev11=ImageTk.PhotoImage(dev1_btn)

        std_b1 = Button(dev1_frame,image=self.dev11,cursor="hand2")
        std_b1.place(x=0,y=0,width=180,height=180)
        
        dev1_label_name=Label(dev1_frame,text="Name: Samarth D Kalegaonkar",font=ft,fg="white",bg="#002B53")
        dev1_label_name.place(x=200,y=5)
        dev1_label_name=Label(dev1_frame,text="Project Role: OpenCV Image \nCapturing & Detection",font=ft,fg="white",bg="#002B53")
        dev1_label_name.place(x=200,y=60)

        # Developer 2 Frame
        dev2_frame=Frame(bg_img,bd=2,bg="#002B53")
        dev2_frame.place(x=500,y=500,width=600,height=180)

        dev2_btn=Image.open("Images_GUI/ranjay.jpg")
        dev2_btn=dev2_btn.resize((180,180),Image.LANCZOS)
        self.dev22=ImageTk.PhotoImage(dev2_btn)

        std_b2 = Button(dev2_frame,image=self.dev22,cursor="hand2")
        std_b2.place(x=0,y=0,width=180,height=180)
        
        dev2_label_name=Label(dev2_frame,text="Name: Ranjay D Singh ",font=ft,fg="white",bg="#002B53")
        dev2_label_name.place(x=200,y=5)
        dev2_label_name=Label(dev2_frame,text="Project Role: UI Designer \n",font=ft,fg="white",bg="#002B53")
        dev2_label_name.place(x=200,y=60)

        # Developer 3 Frame
        dev3_frame=Frame(bg_img,bd=2,bg="#002B53")
        dev3_frame.place(x=900,y=200,width=600,height=180)

        dev3_btn=Image.open("Images_GUI/shubhangi.png")
        dev3_btn=dev3_btn.resize((180,180),Image.LANCZOS)
        self.dev33=ImageTk.PhotoImage(dev3_btn)

        std_b3 = Button(dev3_frame,image=self.dev33,cursor="hand2")
        std_b3.place(x=0,y=0,width=180,height=180)
        
        dev3_label_name=Label(dev3_frame,text="Name: Shubhangi B Manal ",font=ft,fg="white",bg="#002B53")
        dev3_label_name.place(x=200,y=5)
        dev3_label_name=Label(dev3_frame,text="Project Role: Database Connector\n",font=ft,fg="white",bg="#002B53")
        dev3_label_name.place(x=200,y=60)

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()