from tkinter import *
from PIL import Image,ImageTk
import webbrowser 
ft=("VERDENA",14,"bold")


class Helpsupport:
    def __init__(self,root):
        self.root=root
        #self.root.geometry("1366x900+0+0")
        #screen_width = self.root.winfo_screenwidth()-100
        #screen_height = self.root.winfo_screenheight()-100
        screen_width = 1530
        screen_height = 780
        #Set the size of the window based on the screen resolution
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.title("Help Support Section")

# This part is image labels setting start 

        # backgorund image 
        bg1=Image.open("Images_GUI/TS.jpg")
        bg1=bg1.resize((screen_width,screen_height),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=screen_width,height=screen_height)

        #title section
        title_lb1 = Label(bg_img,text="Help Support",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=screen_width,height=45)

        #Back Button
        bk_img=Image.open("Images_GUI/bb1.jpg")
        bk_img=bk_img.resize((120,40),Image.LANCZOS)
        self.pback=ImageTk.PhotoImage(bk_img)

        bk_button=Button(bg_img,command=self.root.destroy,image=self.pback,cursor="hand2")
        bk_button.place(x=1350,y=100,width=120,height=40)

        # Developer 1 Frame
        dev1_frame=Frame(bg_img,bd=2,bg="#064f76")
        dev1_frame.place(x=50,y=150,width=600,height=180)

        dev1_btn=Image.open("Images_GUI/me.jpg")
        dev1_btn=dev1_btn.resize((180,180),Image.LANCZOS)
        self.dev11=ImageTk.PhotoImage(dev1_btn)

        std_b1 = Button(dev1_frame,image=self.dev11,cursor="hand2")
        std_b1.place(x=0,y=0,width=180,height=180)
        
        dev1_label_name=Label(dev1_frame,text="Mail Me: kalegaonkarsamarth@gmail.com",font=ft,fg="white",bg="#064f76")
        dev1_label_name.place(x=180,y=5)
        dev1_label_name=Label(dev1_frame,text="Social Media: ",font=ft,fg="white",bg="#064f76")
        dev1_label_name.place(x=180,y=60)

        dev1_label_contact=Label(dev1_frame,text="Contact: +91 8766431527",font=ft,fg="white",bg="#064f76")
        dev1_label_contact.place(x=180,y=115)

        insta_img_btn_1=Image.open("Images_GUI/linkedin.png")
        insta_img_btn_1=insta_img_btn_1.resize((50,50),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(insta_img_btn_1)

        att_b1 = Button(dev1_frame,command=self.linkedin_sam,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=320,y=50,width=50,height=50)

        gmail_img_btn_1=Image.open("Images_GUI/gmail1.png")
        gmail_img_btn_1=gmail_img_btn_1.resize((60,50),Image.LANCZOS)
        self.att_img2=ImageTk.PhotoImage(gmail_img_btn_1)

        att_b2 = Button(dev1_frame,command=self.gmail_sam,image=self.att_img2,cursor="hand2",)
        att_b2.place(x=400,y=50,width=60,height=50)

        # Developer 2 Frame
        dev2_frame=Frame(bg_img,bd=2,bg="#064f76")
        dev2_frame.place(x=50,y=440,width=600,height=180)

        dev2_btn=Image.open("Images_GUI/ranjay.jpg")
        dev2_btn=dev2_btn.resize((180,180),Image.LANCZOS)
        self.dev22=ImageTk.PhotoImage(dev2_btn)

        std_b2 = Button(dev2_frame,image=self.dev22,cursor="hand2")
        std_b2.place(x=0,y=0,width=180,height=180)
        
        dev2_label_name=Label(dev2_frame,text="Mail Me: ran2492002@gmail.com",font=ft,fg="white",bg="#064f76")
        dev2_label_name.place(x=180,y=5)
        dev2_label_name=Label(dev2_frame,text="Social Media: ",font=ft,fg="white",bg="#064f76")
        dev2_label_name.place(x=180,y=60)

        dev2_label_contact=Label(dev2_frame,text="Contact: +91 81496 33683",font=ft,fg="white",bg="#064f76")
        dev2_label_contact.place(x=180,y=115)

        insta_img_btn_2=Image.open("Images_GUI/linkedin.png")
        insta_img_btn_2=insta_img_btn_2.resize((50,50),Image.LANCZOS)
        self.att_img=ImageTk.PhotoImage(insta_img_btn_2)

        att_b1 = Button(dev2_frame,command=self.linkedin_ranjay,image=self.att_img,cursor="hand2",)
        att_b1.place(x=320,y=50,width=50,height=50)

        gmail_img_btn_2=Image.open("Images_GUI/gmail1.png")
        gmail_img_btn_2=gmail_img_btn_2.resize((60,50),Image.LANCZOS)
        self.att_img3=ImageTk.PhotoImage(gmail_img_btn_2)

        att_b2 = Button(dev2_frame,command=self.gmail_ranjay,image=self.att_img3,cursor="hand2",)
        att_b2.place(x=400,y=50,width=60,height=50)
        
        # create function for button 
    
    # def instagram(self):
    #     self.new = 1
    #     self.url = "https://www.facebook.com/"
    #     webbrowser.open(self.url,new=self.new)
    
    def gmail_sam(self):
        self.new = 1
        self.url = "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=DmwnWrRvwLqDcbXjMqcTXNqHdxMlQxrFLKrlRKzGhZZGkLWRxqvXvFhSSxlBlnnpWKhQTsxgbmdb"
        webbrowser.open(self.url,new=self.new)

    def gmail_ranjay(self):
        self.new = 1
        self.url = "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=jrjtXSpVvBGMMVLBtjPCCkbRXnvZjqbGKDqHqMVPJWJZVVhfPDqFPMRcPxPKTLNmmSfWzfMQ"
        webbrowser.open(self.url,new=self.new)

    def linkedin_sam(self):
        self.new = 1
        self.url = "https://www.linkedin.com/in/samarth-kalegaonkar/"
        webbrowser.open(self.url,new=self.new)

    def linkedin_ranjay(self):
        self.new = 1
        self.url = "https://www.linkedin.com/in/ranjay-devendra-singh-b5ba3723a/"
        webbrowser.open(self.url,new=self.new)

if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()