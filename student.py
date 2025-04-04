from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql as mysql
import cv2 
#Computer Vision Library
ft=("verdana",11,"bold")
ft1=("verdana",13,"bold")

class Student:
    def __init__(self,root):
        self.root=root
        #self.root.geometry("1366x900+0+0")
        #screen_width = self.root.winfo_screenwidth()-100
        #screen_height = self.root.winfo_screenheight()-100
        screen_width = 1530
        screen_height = 780
        #Set the size of the window based on the screen resolution
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        
        self.root.title("Student Section")
        
        #--------------Variables--------------#
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mob=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_searchTX=StringVar()
        self.var_search=StringVar()
        
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
        
        #Background Image
        img2=Image.open("Images_GUI/bg3.jpg")
        img2=img2.resize((screen_width,screen_height),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        
        
        bg_img= Label(self.root,image=self.photoimage2)
        bg_img.place(x=0,y=135,width=screen_width,height=screen_height)
        
        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",35,"bold"),bg="white",fg="Black")
        title_lbl.place(x=0,y=0,width=screen_width,height=50)

        #Back Button
        bk_img=Image.open("Images_GUI/bb1.jpg")
        bk_img=bk_img.resize((120,40),Image.LANCZOS)
        self.pback=ImageTk.PhotoImage(bk_img)

        bk_button=Button(title_lbl,command=self.root.destroy,image=self.pback,cursor="hand2")
        bk_button.place(x=10,y=0,width=120,height=40)
        
        #Main Frame
        mainframe=Frame(bg_img,bd=2,bg="white")
        mainframe.place(x=5,y=60,width=screen_width-15,height=screen_height-205)
        
        #Left Side Frame
        left_frame=LabelFrame(mainframe,bd=2,bg="white",relief=RIDGE,text="Student Details",font=ft1)
        left_frame.place(x=10,y=10,width=screen_width//2,height=screen_height-220)
        
        img_left=Image.open("Images_GUI/loginBg1.jpg")
        img_left=img_left.resize((screen_width//2,135),Image.LANCZOS)
        self.photoimage_left=ImageTk.PhotoImage(img_left)
        
        f_lb1 = Label(left_frame,image=self.photoimage_left)
        f_lb1.place(x=5,y=0,width=screen_width//2-15,height=135)
        
        #Current Course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Details",font=ft)
        current_course_frame.place(x=5,y=140,width=screen_width//2-14,height=105)
        #Department
        dep_label=Label(current_course_frame,text="Department",font=ft,bg="white",fg="blue")
        dep_label.grid(row=0,column=0,padx=5)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=ft,width=15,state="readonly")
        dep_combo['values']=('Select Department','CSE','IT','AIDS','CIVIL','MECH',"EE")
        dep_combo.current(0)    
        dep_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)
        
        #Course
        cou_label=Label(current_course_frame,text="Course",font=ft,bg="white",fg="blue")
        cou_label.grid(row=0,column=2,padx=5,sticky=W)
        #Course ComoBox
        cou_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=ft,width=15,state="readonly")
        cou_combo['values']=("Select Course","SE","FE","TE","BE")
        cou_combo.current(0)    
        cou_combo.grid(row=0,column=3,padx=5,pady=10,sticky=W)
        
        #Year
        year_label=Label(current_course_frame,text="Year",font=ft,bg="white",fg="blue")
        year_label.grid(row=1,column=0,padx=5,pady=10,sticky=W)
        #year combobox
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,width=15,font=ft,state="readonly")
        year_combo["values"]=("Select Year","2017-21","2018-22","2019-23","2020-24","2021-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)
        
        #Semester 
        semester_label=Label(current_course_frame,text="Semester",font=ft,bg="white",fg="blue")
        semester_label.grid(row=1,column=2,padx=5,sticky=W)

        #semester combo box 
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,width=15,font=ft,state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=5,pady=10,sticky=W)
        
        #Class Student Details
        class_Student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Details",font=ft)
        class_Student_frame.place(x=5,y=250,width=screen_width//2-14,height=screen_height-495)
        
        studentId_label=Label(class_Student_frame,text="StudentId:",fg="blue",font=ft,bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        
        studentId_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=15,font=ft)
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        #Student name
        student_name_label = Label(class_Student_frame,text="Std-Name:",font=ft,fg="blue",bg="white")
        student_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=15,font=ft)
        student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        
        #Class Division
        student_div_label = Label(class_Student_frame,text="Class Division:",font=ft,fg="blue",bg="white")
        student_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        #student_div_entry = ttk.Entry(class_Student_frame,textvariable=self.var_div,width=15,font=ft)
        #student_div_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
        student_div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,width=12,font=ft,state="readonly")
        student_div_combo["values"]=("Select Division","A","B","C","D")
        student_div_combo.current(0)
        student_div_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
        #Roll No
        student_roll_label = Label(class_Student_frame,text="Roll-No:",font=ft,fg="blue",bg="white")
        student_roll_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=15,font=ft)
        student_roll_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Gender
        student_gender_label = Label(class_Student_frame,text="Gender:",font=ft,fg="blue",bg="white")
        student_gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        #combo box 
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=12,font=ft,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Date of Birth
        student_dob_label = Label(class_Student_frame,text="DOB:",font=ft,fg="blue",bg="white")
        student_dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        student_dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=15,font=ft)
        student_dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #Email
        student_email_label = Label(class_Student_frame,text="Email:",font=ft,fg="blue",bg="white")
        student_email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        student_email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=15,font=ft)
        student_email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #Phone Number
        student_mob_label = Label(class_Student_frame,text="Mob-No:",font=ft,fg="blue",bg="white")
        student_mob_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        student_mob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_mob,width=15,font=ft)
        student_mob_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        #Address
        student_address_label = Label(class_Student_frame,text="Address:",font=ft,fg="blue",bg="white")
        student_address_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        student_address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width=15,font=("verdana",12,"bold"))
        student_address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)
        
        #Teacher Name
        student_tutor_label = Label(class_Student_frame,text="Tutor Name:",font=ft,fg="blue",bg="white")
        student_tutor_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)

        student_tutor_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=15,font=ft)
        student_tutor_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)

        #Radio Buttons
        self.var_radio1=StringVar()
        
        radiobtn1=ttk.Radiobutton(class_Student_frame,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=5,column=0,padx=5,pady=5,sticky=W)
        
        radiobtn2=ttk.Radiobutton(class_Student_frame,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobtn2.grid(row=5,column=1,padx=5,pady=5,sticky=W)
        
        #Adding All The Buttons to Perform Operations.....
        #Button Frame
        btn_frame = Frame(class_Student_frame,bd=2,bg="silver",relief=RIDGE)
        btn_frame.place(x=8,y=205,width=screen_width//2-200,height=55)
        
        #Save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=7,font=ft,fg="black",bg="skyblue")
        save_btn.grid(row=0,column=0,padx=7,pady=10,sticky=W)

        #Update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=7,font=ft,fg="black",bg="skyblue")
        update_btn.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        #Delete button
        del_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=7,font=ft,fg="black",bg="skyblue")
        del_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        #Reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=7,font=ft,fg="black",bg="skyblue")
        reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #Take photo button
        take_photo_btn=Button(btn_frame,text="Take Photo Sample",command=self.generate_dataset,width=16,font=ft,fg="black",bg="skyblue")
        take_photo_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        
        
        
        
        
        
        #Right Side Frame
        
        right_frame=LabelFrame(mainframe,bd=2,bg="white",relief=RIDGE,text="Student Details",font=ft1)
        right_frame.place(x=screen_width//2+20,y=10,width=screen_width//2-50,height=screen_height-220)
        #left_frame.place(x=10,y=10,width=screen_width//2,height=screen_height-220)
        
        img_right=Image.open("Images_GUI/loginBg1.jpg")
        img_right=img_right.resize((screen_width//2-65,135),Image.LANCZOS)
        self.photoimage_right=ImageTk.PhotoImage(img_right)
        
        f_lb1 = Label(right_frame,image=self.photoimage_right)
        f_lb1.place(x=5,y=0,width=screen_width//2-65,height=135)
        
        #---------------Search System-----------
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=ft1)
        search_frame.place(x=5,y=140,width=screen_width//2-65,height=70)
        
        search_label = Label(search_frame,text="Search:",font=ft,fg="black",bg="skyblue")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        
        #combo box 
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=12,font=ft,state="readonly")
        search_combo["values"]=("Select","Roll-No","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)
        
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=12,font=ft)
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        
        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=ft,fg="white",bg="orange")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)
        
        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=8,font=ft,fg="white",bg="green")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)
        
        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=215,width=screen_width//2-65,height=320)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        col=("ID","Name","Dep","Course","Year","Sem","Div","Gender","DOB","Mob-No","Address","Roll-No","Email","Teacher","Photo")
        #create table 
        self.student_table = ttk.Treeview(table_frame,columns=col,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Full Name")
        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Mob-No",text="Mob-No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Roll-No",text="Roll-No")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="PhotoSample")
        self.student_table["show"]="headings"

        
        # Set Width of Colums 
        self.student_table.column("ID",width=20)
        self.student_table.column("Name",width=150)
        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=60)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Mob-No",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Roll-No",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
        #========================== Functions Declaration ===================================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_gender.get()=="Select Gender" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields That are Mandatory!!",parent=self.root)
        else:
            
            try:
                conn = mysql.connect(user='root', password='root',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_div.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_mob.get(),
                self.var_address.get(),
                self.var_roll.get(),
                self.var_email.get(),
                self.var_teacher.get(),
                self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records Saved Successfully!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    def fetch_data(self):
        conn = mysql.connect(user='root', password='root',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()
        sql_query="select * from student"
        mycursor.execute(sql_query)
        data=mycursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    #====================Get Cursor========================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_std_id.set(data[0]),
        self.var_std_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_course.set(data[3]),
        self.var_year.set(data[4]),
        self.var_semester.set(data[5]),
        self.var_div.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_mob.set(data[9]),
        self.var_address.set(data[10]),
        self.var_roll.set(data[11]),
        self.var_email.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    
    #Update Function
    def update_data(self):
    
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_gender.get()=="Select Gender" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="Select Division" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields That are Mandatory!!",parent=self.root)
        
        else:
            try:
                Update=messagebox.askyesno("Update","Do You Want to Update ?",parent=self.root)
                if Update>0:
                    conn = mysql.connect(user='root', password='root',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("update student set sname=%s,dept_name=%s,course=%s,year=%s,semester=%s,division=%s,gender=%s,dob=%s,mob=%s,address=%s,roll=%s,email=%s,teacher=%s,Photosample=%s where sid=%s",
                    (
                    self.var_std_name.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_mob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                    ))
                    
                
                else:
                    if not Update:
                        return
                        
                messagebox.showinfo("Success","Student Details Updated Successfully...",parent=self.root)
                
                conn.commit()
                conn.close()
                self.fetch_data()
                self.reset_data()
                
                
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    #Delete Function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID Required !!!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do You Want to Delete This Data",parent=self.root)
                if delete>0:
                    conn = mysql.connect(user='root', password='root',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor()
                    sql_query="delete from student where sid=%s"
                    val=(self.var_std_id.get(),)
                    mycursor.execute(sql_query,val)
                
                else:
                    if not delete:
                        return
                
                messagebox.showinfo("Delete","Data Deleted Successfully",parent=self.root)
                conn.commit()
                conn.close()
                self.fetch_data()
                self.reset_data()
                
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                
                    
     #Reset Function               
    def reset_data(self):
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_div.set("Select Division"),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_mob.set(""),
        self.var_address.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
    
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connect(user='root', password='root',host='localhost',database='face_recognition',port=3306)
                my_cursor = conn.cursor()
                sql = "SELECT sid,sname,dept_name,course,year,semester,division,gender,dob,mob,address,roll,email,teacher,Photosample FROM student where roll='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    #Generate Data Set : Take Photo Samples....
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_gender.get()=="Select Gender" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="Select Division" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields That are Mandatory!!",parent=self.root)
        
        else:
            try:
                conn = mysql.connect(user='root', password='root',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myresult=mycursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                mycursor.execute("update student set sname=%s,dept_name=%s,course=%s,year=%s,semester=%s,division=%s,gender=%s,dob=%s,mob=%s,address=%s,roll=%s,email=%s,teacher=%s,Photosample=%s where sid=%s",
                    (
                    self.var_std_name.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_mob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #========================Load Predefined Data on Face frontals From open cv===========================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling Factor =1.3
                    #Minimum Neighbour=5
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capturing Images....",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
        
if __name__ == "__main__":  
    root=Tk()
    obj=Student(root)
    root.resizable(False,False)
    root.mainloop()        