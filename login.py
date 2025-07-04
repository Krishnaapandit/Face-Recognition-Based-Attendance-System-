import subprocess
import cv2
from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
from train import Train
from student import Student
from train import Train
from attendance import Attendance
from developer import Developer
from helpsupport import Helpsupport
import os
#This are the libraries and other files require to run the code properly.


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")   #Here we have declared the title with size of the Frame

        
        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"d:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/mit.jpg")

        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame1= Frame(self.root,bg="#F2F2F2")
        frame1.place(x=560,y=170,width=340,height=450)

        img1=Image.open(r"d:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/logo.png")
        img1=img1.resize((120,120),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#F2F2F2")
        lb1img1.place(x=690,y=175, width=100,height=100)

        get_str = Label(frame1,text="Teacher's Login",font=("times new roman",20,"bold"),fg="Black",bg="#F2F2F2")
        get_str.place(x=80,y=100)

        #label1 
        username =lb1= Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="Black",bg="#F2F2F2")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="Black",bg="#F2F2F2")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=33,y=260,width=270)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#000000",bg="white",activeforeground="Black",activebackground="#000000")
        loginbtn.place(x=33,y=320,width=270,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.reg,text="Register",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="Black",bg="#F2F2F2",activeforeground="white",activebackground="#000000")
        loginbtn.place(x=33,y=370,width=50,height=20)


        # Creating Button Forget
        loginbtn=Button(frame1,command=self.forget_pwd,text="Forget",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="Black",bg="#F2F2F2",activeforeground="white",activebackground="#000000")
        loginbtn.place(x=90,y=370,width=50,height=20)
        
        '''Now in the above section we have added the paths for the background images, the buttons and there name and also we have created the username and password box
        where the user can enter their mail and password and a new user can register to create there valid credentials.  '''

    # This function is for register window. If the user dont have a valid account they can create it using register button.
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        else:
            # messagebox shows an error if the credentials are wrong("Error","Please Check Username or Password !")
            
            conn = mysql.connector.connect(username='root', password='host',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            mycursor.execute("select * from regteach where email=%s and pwd=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("YesNo","Access only Admin")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()
        
        
    #Reset Passowrd Function
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password='host',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s and ss_que=%s and s_ans=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update regteach set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, Please login with new Password!",parent=self.root2)
                


    #Forget window: In this window the user can reset there password
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter a Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(username='root', password='host',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="Black",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                
                #Security Question Label
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                #Options
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #Security Question answer label
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry oE security Answer
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                # New Password Label
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                # New password entry 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button of New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="black",bg="#F2F2F2",activeforeground="white",activebackground="black")
                loginbtn.place(x=70,y=300,width=270,height=35)


            

# Main Program 

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")  #The face recognition name is given to the code

        #Setting up the Image labels and adding background image
        
        img=Image.open(r"d:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/mitname.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"d:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/back.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Attendance Managment System",font=("verdana",30,"bold"),bg="white",fg="Black")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # In the below section the process for button creation is given
    
        # student button 1
        std_img_btn=Image.open(r"d:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/std.png")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=100,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Student Section",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="Black")
        std_b1_1.place(x=250,y=280,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"d:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/face.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=480,y=100,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.face_rec,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="Black")
        det_b1_1.place(x=480,y=280,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"d:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/attendds.jpg")
        att_img_btn=att_img_btn.resize((200,200),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=710,y=100,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="Black")
        att_b1_1.place(x=710,y=280,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"d:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/images.jpeg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.helpSupport,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=940,y=100,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.helpSupport,text="Help Suppot",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="Black")
        hlp_b1_1.place(x=940,y=280,width=180,height=45)

    
         # Train   button 5
        tra_img_btn=Image.open(r"d:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/folde.png")
        tra_img_btn=tra_img_btn.resize((180,180),Image.ANTIALIAS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=250,y=330,width=180,height=180)

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Train Data",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="Black")
        tra_b1_1.place(x=250,y=510,width=180,height=45)

        # Photo   button 6
        pho_img_btn=Image.open(r"d:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/camm.jpeg")
        pho_img_btn=pho_img_btn.resize((180,180),Image.ANTIALIAS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,command=self.open_img,image=self.pho_img1,cursor="hand2",)
        pho_b1.place(x=480,y=330,width=180,height=180)

        pho_b1_1 = Button(bg_img,command=self.open_img,text="Capture Image",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="Black")
        pho_b1_1.place(x=480,y=510,width=180,height=45)

        # Developers   button 7
        dev_img_btn=Image.open(r"d:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/devep.jpg")
        dev_img_btn=dev_img_btn.resize((180,180),Image.ANTIALIAS)
        self.dev_img1=ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(bg_img,command=self.developr,image=self.dev_img1,cursor="hand2",)
        dev_b1.place(x=710,y=330,width=180,height=180)

        dev_b1_1 = Button(bg_img,command=self.developr,text="Developers",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="Black")
        dev_b1_1.place(x=710,y=510,width=180,height=45)

        # exit   button 8
        exi_img_btn=Image.open(r"d:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/exi.jpg")
        exi_img_btn=exi_img_btn.resize((180,180),Image.ANTIALIAS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.Close,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=940,y=330,width=180,height=180)

        exi_b1_1 = Button(bg_img,command=self.Close,text="Exit",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="Black")
        exi_b1_1.place(x=940,y=510,width=180,height=45)

#Funtion for Opening Images Folder
    def open_img(self):
        capture = cv2.VideoCapture(0)  
        
        ret, frame = capture.read()

        if ret:
            save_directory = "D:/studentsdetails/"
            image_name = "test.jpg"         # Here we have added the image path and its name so that it should open this image and recognize the faces in that image
            image_path = os.path.join(save_directory, image_name)

            if os.path.exists(image_path):
                os.remove(image_path)

            cv2.imwrite(image_path, frame)
            print("Image saved:", image_path)
        else:
            print("Failed to capture image.")

        capture.release()  

# Functions Buttons
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        script_directory = r'D:/studentsdetails'

        script_name = 'd:/studentsdetails/faces.py'

        script_path = os.path.join(script_directory, script_name)

        os.chdir(script_directory)

        subprocess.Popen(['python', script_path],shell=True)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def helpSupport(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)
        
    def Close(self):
        root.destroy()

    
if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()

