from tkinter import*
from PIL import Image,ImageTk
from menucafe import menu



class cafe_management:
    def __init__(self,root):
        self.root=root
        self.root.title("COFFEE SHOP")
        self.root.geometry("500x600+0+0")

#-------------------------------------image 1----------------------------------------------------------------------------


        img1=Image.open(r"C:/Users/sattu/OneDrive/Desktop/py/registerbgimg.jpg")
        img1=img1.resize((500,200))
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg1=Label(self.root,image=self.photoimg1,bd=4,relief=SUNKEN)
        lblimg1.place(x=0,y=0,width=500,height=200)

#-------------------------------------title----------------------------------------------------------------------------
        lbl_title=Label(self.root,text="BREW PERFECT COFFEE",font=("times new roman",30,"bold"),bg="white",fg="black",bd=5,relief=RIDGE)
        lbl_title.place(x=0,y=200,width=500,height=50)

#------------------------------------main frame-------------------------------------------------------------------------------------------
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=250,width=500,height=350)

#------------------------------------btn frame-------------------------------------------------------------------------------
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=0,width=500,height=40)

#-------------------------------------btn------------------------------------------------------------------
        menu_btn=Button(btn_frame,bd=2,relief=RIDGE,text="MENU",command=self.menu_details,font=("times new roman",17,"bold"),bg="black",fg="white")
        menu_btn.place(x=0,y=0,width=125,height=40)

        cart_btn=Button(btn_frame,bd=2,relief=RIDGE,text="CART",font=("times new roman",17,"bold"),bg="black",fg="white")
        cart_btn.place(x=125,y=0,width=125,height=40)

        history_btn=Button(btn_frame,bd=2,relief=RIDGE,text="HISTORY",font=("times new roman",15,"bold"),bg="black",fg="white")
        history_btn.place(x=250,y=0,width=125,height=40)

        ctnus_btn=Button(btn_frame,bd=2,relief=RIDGE,text="CONTACT US",font=("times new roman",12,"bold"),bg="black",fg="white")
        ctnus_btn.place(x=375,y=0,width=125,height=40)


        img2=Image.open(r"C:/Users/sattu/OneDrive/Desktop/py/home.jpg")
        img2=img2.resize((500,300))
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(main_frame,image=self.photoimg2,bd=4,relief=SUNKEN)
        lblimg2.place(x=0,y=40,width=499,height=303)


    def menu_details(self):
        self.new_window=Toplevel(self.root)
        self.app=menu(self.new_window)              #class of new window to open

 





if __name__=="__main__":
    root=Tk()
    win=cafe_management(root)
    root.mainloop()