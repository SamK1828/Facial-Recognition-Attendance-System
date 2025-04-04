from sys import path
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
import pymysql as mysql
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime

ft=("verdana",11,"bold")
ft1=("verdana",13,"bold")

class Face_Recognition:
    def __init__(self,root):
        
        self.recognized_faces = set()  # To keep track of recognized faces
        self.root=root
        #self.root.geometry("1366x900+0+0")
        #screen_width = self.root.winfo_screenwidth()-100
        #screen_height = self.root.winfo_screenheight()-100
        screen_width = 1530
        screen_height = 780
        #Set the size of the window based on the screen resolution
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.title("Face Detector")
        
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
        
        # backgorund image 
        bg1=Image.open("Images_GUI/bg2.jpg")
        bg1=bg1.resize((screen_width,screen_height),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # Background image Label
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=135,width=screen_width,height=screen_height)
        
        f_lb1 = Label(self.root,image=self.photoimage1)
        f_lb1.place(x=screen_width//2,y=0,width=screen_width//2,height=135)

        #Back Button
        bk_img=Image.open("Images_GUI/bb1.jpg")
        bk_img=bk_img.resize((120,40),Image.LANCZOS)
        self.pback=ImageTk.PhotoImage(bk_img)

        bk_button=Button(bg_img,command=self.root.destroy,image=self.pback,cursor="hand2")
        bk_button.place(x=50,y=100,width=120,height=40)
        
        #title section
        title_lb1 = Label(bg_img,text="Welcome to Face Recognition Panel",font=("verdana",30,"bold"),bg="white",fg="blue")
        title_lb1.place(x=0,y=0,width=screen_width,height=45)
        
        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open("Images_GUI/f_det.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2") 
        std_b1.place(x=600,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=600,y=350,width=180,height=45)
        
    #=====================Attendance===================
    
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDatalist = f.readlines()
            name_list = [line.split(",")[0] for line in myDatalist]
            if i not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"{i}, {r}, {n}, {dtString}, {d1}, Present\n")
                
    #================face recognition==================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                print(id)
                confidence = int((100 * (1 - predict / 300)))
                conn = mysql.connect(user='root', password='root', host='localhost', database='face_recognition', port=3306)
                mycursor = conn.cursor()

                # Fetch student name
                mycursor.execute("SELECT sname FROM student WHERE sid = %s", (id,))
                # n = mycursor.fetchone()
                name = mycursor.fetchone()
                
                name = name[0] if name else ""
                # Fetch roll number
                mycursor.execute("SELECT roll FROM student WHERE sid = %s", (id,))
                r = mycursor.fetchone()
                r = r[0] if r else ""
                # Fetch department name
                mycursor.execute("SELECT dept_name FROM student WHERE sid = %s", (id,))
                d = mycursor.fetchone()
                d = d[0] if d else ""
                # conn.close()
                if confidence > 77 :
                    cv2.putText(img, f"ID: {id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Dept: {d}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Roll: {r}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    if id not in self.recognized_faces:
                        self.mark_attendance(i=id, r=r, n=name, d=d)
                    self.recognized_faces.add(id)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

                coord = [x, y, w, h]
                
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.2, 5, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        videoCap = cv2.VideoCapture(0)
        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()
        
if __name__ == "__main__":  
    root=Tk()
    obj=Face_Recognition(root)
    root.resizable(False,False)
    root.mainloop()    