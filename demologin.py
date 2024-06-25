from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from home import cafe_management
import mysql.connector

class Home:
    def __init__(self, root):
        self.root = root
        self.root.title("Home")
        self.root.geometry("500x500")

        # Add your home page widgets here

class Login_u:
    def __init__(self, root):
        self.root = root
        self.root.title("USER LOGIN")
        self.root.geometry("500x600+0+0")

        # Connect to MySQL database
        self.mydb = mysql.connector.connect(
            host="localhost", 
            user="root",
            password="",
            database="cafemanagement"
        )
        self.mycursor = self.mydb.cursor()

        # Login Background
        img1 = Image.open(r"C:/Users/sattu/OneDrive/Desktop/py/loginbg.jpg")
        img1 = img1.resize((500, 600))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(self.root, image=self.photoimg1, bd=2, relief=SUNKEN)
        lblimg1.place(x=0, y=0, width=500, height=600)

        # Main Frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white", borderwidth=0)
        main_frame.place(x=30, y=100, width=250, height=430)

        # Login Image
        img2 = Image.open(r"C:/Users/sattu/OneDrive/Desktop/py/upic.jpg")
        img2 = img2.resize((150, 150))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(main_frame, image=self.photoimg2, relief=SUNKEN, borderwidth=0)
        lblimg2.place(x=70, y=10, width=100, height=100)

        # Title
        lbl_title = Label(main_frame, text="LOGIN", font=("times new roman", 20, "bold"), bg="white", fg="black",
                          relief=RIDGE, borderwidth=0)
        lbl_title.place(x=0, y=110, width=250, height=50)

        # Username Label and Entry
        lbl_username = Label(main_frame, text="UserName               *", font=("times new roman", 15, "bold"),
                             bg="white", fg="black", relief=RIDGE, borderwidth=0)
        lbl_username.place(x=0, y=150, width=200, height=50)
        self.user = ttk.Entry(main_frame, font=("times new roman", 15, "italic"))
        self.user.place(x=10, y=190, width=210, height=30)

        # Password Label and Entry
        lbl_pasw = Label(main_frame, text="Password                *", font=("times new roman", 15, "bold"),
                         bg="white", fg="black", relief=RIDGE, borderwidth=0)
        lbl_pasw.place(x=0, y=220, width=200, height=50)
        self.pasw = ttk.Entry(main_frame, font=("times new roman", 15, "italic"), show="*")
        self.pasw.place(x=10, y=260, width=210, height=30)

        # Login Button
        login_btn = Button(main_frame, bd=1, relief=RIDGE, text="LOGIN", font=("times new roman", 17, "bold"),
                           bg="black", fg="white", command=self.verify_login)
        login_btn.place(x=75, y=310, width=100, height=30)

        # Register Button
        register_btn = Button(main_frame, bd=0, relief=RIDGE, text="Don't have an account",
                              font=("times new roman", 12, "bold"), bg="white", fg="blue")
        register_btn.place(x=30, y=360, width=200, height=15)

    def verify_login(self):
        username = self.user.get()
        password = self.pasw.get()

        # SQL query to select user from database
        sql = "SELECT * FROM register WHERE un = %s AND pass = %s"
        val = (username, password)
        self.mycursor.execute(sql, val)

        # Fetch one record
        user = self.mycursor.fetchone()

        if user:
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()  # Destroy login window
            home_root = Tk()  # Create home window
            home = cafe_management(home_root)
            home_root.mainloop()
        else:
            messagebox.showerror("Error", "Invalid username or password")

if __name__ == "__main__":
    root = Tk()
    win = Login_u(root)
    root.mainloop()
