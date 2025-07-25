from tkinter import*
from PIL import Image,ImageTk
import webbrowser
#This are the libraries and other files require to run the code properly.

class Helpsupport:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Help Support")
        
        #Setting up the Image labels, Buttons and adding background image 

        # Header image  
        img=Image.open(r"d:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/mitname.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # Setting image as a lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # Backgorund image 
        bg1=Image.open(r"d:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/bg4.png")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # Setting image as a lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Help Support",font=("verdana",30,"bold"),bg="white",fg="Black")
        title_lb1.place(x=0,y=0,width=1366,height=45)

    
        # Student button
        std_img_btn=Image.open(r"D:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/web.png")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.website,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.website,text="Website",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="Black")
        std_b1_1.place(x=250,y=380,width=180,height=45)

        # Detect Face button 
        det_img_btn=Image.open(r"D:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/fb.png")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.facebook,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=480,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.facebook,text="Facebook",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="Black")
        det_b1_1.place(x=480,y=380,width=180,height=45)

         # Attendance System button 
        att_img_btn=Image.open(r"D:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/yt.png")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.youtube,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=710,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.youtube,text="Youtube",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="Black")
        att_b1_1.place(x=710,y=380,width=180,height=45)

         # Help Support button 
        hlp_img_btn=Image.open(r"D:/Python-FYP-Face-Recognition-Attendence-System-master/Images_GUI/gmail.png")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=940,y=200,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="Black")
        hlp_b1_1.place(x=940,y=380,width=180,height=45)
  
  #Previous code of buttons    
        
    # Now creating function for button 
    def website(self):
        self.new = 1
        self.url = "https://exceleprep.com/"
        webbrowser.open(self.url,new=self.new)
    
    def facebook(self):
        self.new = 1
        self.url = "https://www.facebook.com/"
        webbrowser.open(self.url,new=self.new)
    
    def youtube(self):
        self.new = 1
        self.url = "https://www.youtube.com/channel/UCwpFCX_Z4SVkAT_6hPeUnsA"
        webbrowser.open(self.url,new=self.new)
    
    def gmail(self):
        self.new = 1
        self.url = "https://www.gmail.com"
        webbrowser.open(self.url,new=self.new)



if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()