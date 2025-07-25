from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
#This are the libraries and other files require to run the code properly.

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")   #The code is named as register and the size is define

        # Here we declared the Variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_cnum=StringVar()
        self.var_email=StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()

#From this part we and the images created box and tile and buttons for registration process
        self.bg=ImageTk.PhotoImage(file=r"d:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/back.png")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,bg="#F2F2F2")
        frame.place(x=20,y=60,width=900,height=580)
        

        '''img1=Image.open(r"D:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/reg1.png")
        img1=img1.resize((450,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#F2F2F2")
        lb1img1.place(x=300,y=100, width=500,height=100)'''
        

        get_str = Label(frame,text="Registration",font=("times new roman",40,"bold"),fg="Black",bg="#F2F2F2")
        get_str.place(x=330,y=80)

        #Label for First name
        fname =lb1= Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="Black",bg="#F2F2F2")
        fname.place(x=100,y=200)

        #Entry of first name
        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txtuser.place(x=103,y=225,width=270)


        #Label for last name
        lname =lb1= Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="Black",bg="#F2F2F2")
        lname.place(x=100,y=270)

        #Entry of last name
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=295,width=270)

       

        #Label for contact number
        cnum =lb1= Label(frame,text="Contact No:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
        cnum.place(x=530,y=200)

        #Entry for contact number 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_cnum,font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=225,width=270)


        #Label for email
        email =lb1= Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
        email.place(x=530,y=270)

        #Entry for email
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=295,width=270)

       

        #Label for security question  
        ssq =lb1= Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
        ssq.place(x=100,y=350)

        #Options for security question
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=103,y=375,width=270)


        #Label of security question answer
        sa =lb1= Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
        sa.place(x=100,y=420)

        #Entry of security question answer
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_sa,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=445,width=270)


        #Label for password
        pwd =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
        pwd.place(x=530,y=350)

        #Entry of password
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=375,width=270)


        #Label for confirm password
        cpwd =lb1= Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
        cpwd.place(x=530,y=420)

        #Entry of confirm password
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_cpwd,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=445,width=270)

        # Checkbutton
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"),fg="black",bg="#F2F2F2")
        checkbtn.place(x=100,y=480,width=270)


        # Creating Button for Register
        loginbtn=Button(frame,command=self.reg,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="Black",bg="#F2F2F2",activeforeground="white",activebackground="#000000")
        loginbtn.place(x=103,y=510,width=270,height=35)

        # Creating Button for Login
        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="Black",bg="#F2F2F2",activeforeground="white",activebackground="#000000")
        loginbtn.place(x=533,y=510,width=270,height=35)



#This section is for checking everything and if anything is missing then it display the given message

    def reg(self):
        if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_cnum.get()=="" or self.var_email.get()=="" or self.var_ssq.get()=="Select" or self.var_sa.get()=="" or self.var_pwd.get()=="" or self.var_cpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!")
        elif(self.var_check.get()==0):
            messagebox.showerror("Error","Please Check the Agree Terms and Conditons!")
        else:
        
            try:
                conn = mysql.connector.connect(username='root', password='host',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                query=("select * from regteach where email=%s")
                value=(self.var_email.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another email")
                else:
                    mycursor.execute("insert into regteach values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_cnum.get(),
                    self.var_email.get(),
                    self.var_ssq.get(),
                    self.var_sa.get(),
                    self.var_pwd.get()
                    ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Registerd!",parent=self.root) #Once successfull registration is done it will display the given message
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()