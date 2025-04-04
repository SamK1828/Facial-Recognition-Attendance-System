import customtkinter as ctk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
import os
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpsupport import Helpsupport
ft=("times new roman",20,"bold")
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        #self.root.geometry("1366x900+0+0")
        #screen_width = self.root.winfo_screenwidth()
        screen_width=1400
        #screen_height = self.root.winfo_screenheight()
        screen_height=780
        #Set the size of the window based on the screen resolution
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        
        self.root.title("Face Recognition System")
        
        #First Image
        img=Image.open("Images_GUI/banner.jpg")
        img=img.resize((screen_width//2,135),Image.LANCZOS) # type: ignore
        self.photoimage=ImageTk.PhotoImage(img)
        
        
        f_lb1 = Label(self.root,image=self.photoimage) # type: ignore
        f_lb1.place(x=0,y=0,width=screen_width//2,height=135)
        
        #Second Image
        img1=Image.open("Images_GUI/banner1.jpg")
        img1=img1.resize((screen_width//2,135),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        
        
        f_lb1 = Label(self.root,image=self.photoimage1)
        f_lb1.place(x=screen_width//2,y=0,width=screen_width//2,height=135)
        
        #Background Image
        img2=Image.open("Images_GUI/bg3.jpg")
        img2=img2.resize((screen_width,screen_height),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        
        
        bg_img= Label(self.root,image=self.photoimage2)
        bg_img.place(x=0,y=135,width=screen_width,height=screen_height)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="Black")
        title_lbl.place(x=0,y=0,width=screen_width,height=50)
        
        #Student Button
        img4=Image.open("Images_GUI/std1.jpg")
        img4=img4.resize((210,210),Image.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,command=self.student_details,image=self.photoimage4,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,command=self.student_details,text="Student Details",cursor="hand2",font=ft,bg="lightblue",)
        b1_1.place(x=100,y=300,width=220,height=40)
        
        #Face Detect Button
        img5=Image.open("Images_GUI/det1.jpg")
        img5=img5.resize((210,210),Image.LANCZOS)
        self.photoimage5=ImageTk.PhotoImage(img5)
        
        b2=Button(bg_img,image=self.photoimage5,cursor="hand2",command=self.face_data)
        b2.place(x=400,y=100,width=220,height=220)
        
        b2_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=ft,bg="lightblue",)
        b2_1.place(x=400,y=300,width=220,height=40)
        
        #Attendance Button
        img6=Image.open("Images_GUI/att.jpg")
        img6=img6.resize((210,210),Image.LANCZOS)
        self.photoimage6=ImageTk.PhotoImage(img6)
        
        b3=Button(bg_img,command=self.attendance_panel,image=self.photoimage6,cursor="hand2")
        b3.place(x=700,y=100,width=220,height=220)
        
        b3_1=Button(bg_img,command=self.attendance_panel,text="Attendance",cursor="hand2",font=ft,bg="lightblue",)
        b3_1.place(x=700,y=300,width=220,height=40)
        
        #Help Button
        img7=Image.open("Images_GUI/hlp.jpg")
        img7=img7.resize((210,210),Image.LANCZOS)
        self.photoimage7=ImageTk.PhotoImage(img7)
        
        b4=Button(bg_img,command=self.help_support,image=self.photoimage7,cursor="hand2")
        b4.place(x=1000,y=100,width=220,height=220)
        
        b4_1=Button(bg_img,command=self.help_support,text="Help Support",cursor="hand2",font=ft,bg="lightblue",)
        b4_1.place(x=1000,y=300,width=220,height=40)
        
        #Train Button
        img8=Image.open("Images_GUI/tra.jpg")
        img8=img8.resize((210,210),Image.LANCZOS)
        self.photoimage8=ImageTk.PhotoImage(img8)
        
        b5=Button(bg_img,command=self.train_data,image=self.photoimage8,cursor="hand2")
        b5.place(x=100,y=400,width=220,height=220)
        
        b5_1=Button(bg_img,command=self.train_data,text="Train..",cursor="hand2",font=ft,bg="lightblue",)
        b5_1.place(x=100,y=600,width=220,height=40)
        
        # Photos Button
        img9=Image.open("Images_GUI/m1.png")
        img9=img9.resize((210,210),Image.LANCZOS)
        self.photoimage9=ImageTk.PhotoImage(img9)
        
        b6=Button(bg_img,command=self.open_img,image=self.photoimage9,cursor="hand2")
        b6.place(x=400,y=400,width=220,height=220)
        
        b6_1=Button(bg_img,command=self.open_img,text="Dataset",cursor="hand2",font=ft,bg="lightblue",)
        b6_1.place(x=400,y=600,width=220,height=40)
        
        # Developer Button
        img10=Image.open("Images_GUI/dev.jpg")
        img10=img10.resize((210,210),Image.LANCZOS)
        self.photoimage10=ImageTk.PhotoImage(img10)
        
        b7=Button(bg_img,command=self.developer_page,image=self.photoimage10,cursor="hand2")
        b7.place(x=700,y=400,width=220,height=220)
        
        b7_1=Button(bg_img,command=self.developer_page,text="Developer",cursor="hand2",font=ft,bg="lightblue",)
        b7_1.place(x=700,y=600,width=220,height=40)
        
        # Exit Button
        img11=Image.open("Images_GUI/exi.jpg")
        img11=img11.resize((210,210),Image.LANCZOS)
        self.photoimage11=ImageTk.PhotoImage(img11)
        
        b8=Button(bg_img,image=self.photoimage11,command=self.exit_page,cursor="hand2")
        b8.place(x=1000,y=400,width=220,height=220)
        
        b8_1=Button(bg_img,text="Exit",command=self.exit_page,cursor="hand2",font=ft,bg="lightblue",)
        b8_1.place(x=1000,y=600,width=220,height=40)
        
    def open_img(self):
        os.startfile("data")
        
        #=========================== Functions Buttons ============================
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_panel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developer_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    def help_support(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)
    def exit_page(self):
        self.root.destroy()
                
if __name__ == "__main__":  
    root=Tk()
    # root=ctk.CTk()
    obj=Face_Recognition_System(root)
    # root.resizable(False,False)
    root.mainloop()
