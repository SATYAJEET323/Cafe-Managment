from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
import random


class menu:
    def __init__(self, root):
        self.root = root
        self.root.title("MENU")
        self.root.geometry("500x600+0+0")

        # Connect to MySQL Database
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cafemanagement"
        )
        self.cursor = self.db_connection.cursor()

        # Fetch coffee names and prices from the database
        self.cursor.execute("SELECT cname, cprice FROM menu")
        self.coffee_data = self.cursor.fetchall()

        # ---------------------------variable--------------------------------------------------------
        self.var_token = StringVar()
        x = random.randint(100, 200)
        self.var_token.set(str(x))

        lbl_title = Label(self.root, text="COFFEE MENU", font=("times new roman", 30, "bold"), bg="brown", fg="white",
                          bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=500, height=50)

        main_frame = Frame(self.root, bd=0, relief=RIDGE, bg="white")
        main_frame.place(x=0, y=50, width=500, height=550)

        # Create a list to store items in the cart
        self.cart = []

        # ----------------------------COFFFES----------------------------------------------
        y_position = 52
        for coffee in self.coffee_data:
            cname, cprice = coffee
            coffee_frame = Frame(self.root, bd=3, relief=RIDGE)
            coffee_frame.place(x=0, y=y_position, width=500, height=90)

            coffee_img = Image.open(f"C:/Users/sattu/OneDrive/Desktop/py/blackcoffe.jpg")  # Assuming images are stored in a folder named 'images'
            coffee_img = coffee_img.resize((200, 100))
            self.photo_coffee_img = ImageTk.PhotoImage(coffee_img)

            lbl_coffee = Label(self.root, image=self.photo_coffee_img, bd=0, relief=SUNKEN)
            lbl_coffee.place(x=2, y=y_position, width=150, height=85)

#---------------------------------americano img ----------------------------

            amerimg=Image.open(r"C:/Users/sattu/OneDrive/Desktop/py/americano.jpg")
            amerimg=amerimg.resize((200,100))
            self.photoamerimg=ImageTk.PhotoImage(amerimg)

            lblamer=Label(self.root,image=self.photoamerimg,bd=0,relief=SUNKEN)
            lblamer.place(x=2,y=52,width=150,height=85)

#---------------------------------cappucino img -----------------
            cappimg=Image.open(r"C:/Users/sattu/OneDrive/Desktop/py/cappucino.jpeg")
            cappimg=cappimg.resize((200,100))
            self.photocappimg=ImageTk.PhotoImage(cappimg)

            lblcapp=Label(self.root,image=self.photocappimg,bd=0,relief=SUNKEN)
            lblcapp.place(x=2,y=143,width=150,height=85)

            
#--------------------latte img------------------------------
            latimg=Image.open(r"C:/Users/sattu/OneDrive/Desktop/py/latte.jpg")
            latimg=latimg.resize((200,100))
            self.photolatimg=ImageTk.PhotoImage(latimg)

            lbllat=Label(self.root,image=self.photolatimg,bd=0,relief=SUNKEN)
            lbllat.place(x=2,y=324,width=150,height=85)

#-------------------------mocha img--------------------
            mocimg=Image.open(r"C:/Users/sattu/OneDrive/Desktop/py/MOCHA.jpg")
            mocimg=mocimg.resize((200,100))
            self.photomocimg=ImageTk.PhotoImage(mocimg)

            lblmoc=Label(self.root,image=self.photomocimg,bd=0,relief=SUNKEN)
            lblmoc.place(x=2,y=235,width=150,height=85)

#----------------------price and name-------------------------

            lbl_cname = Label(coffee_frame, text=cname, font=("times new roman", 17, "bold"), fg="black", bd=0,
                              relief=RIDGE)
            lbl_cname.place(x=-38, y=-10, width=500, height=50)

            lbl_price = Label(coffee_frame, text="Price:₹" + str(cprice), font=("times new roman", 17, "bold"),
                              fg="black", bd=0, relief=RIDGE)
            lbl_price.place(x=-35, y=30, width=500, height=50)

            # Add button with command to add the coffee to the cart
            add_btn = Button(coffee_frame, bd=2, relief=RIDGE, text="ADD", font=("times new roman", 15, "bold"),
                             bg="black", fg="white", command=lambda cname=cname, cprice=cprice: self.add_to_cart(cname, cprice))
            add_btn.place(x=385, y=30, width=80, height=37)

            y_position += 91

        # ---------------------------------------------------------------------------------
        payment_btn = Button(main_frame, bd=2, relief=RIDGE, text="Go to cart", font=("times new roman", 15, "bold"),
                             bg="black", fg="white", command=self.show_cart)
        payment_btn.place(x=80, y=480, width=160, height=40)

        lbl_token = Label(main_frame, text="Token No.", font=("times new roman", 14, "bold"), bg="white", fg="black",
                          bd=0, relief=RIDGE)
        lbl_token.place(x=300, y=476, width=86, height=50)

        self.token = ttk.Entry(main_frame, textvariable=self.var_token, font=("times new roman", 15, "bold"),
                                state="readonly")
        self.token.place(x=406, y=482, width=83, height=30)

    def add_to_cart(self, cname, cprice):
        self.cart.append((cname, cprice))

    def show_cart(self):
        cart_window = Toplevel(self.root)
        cart_window.title("CART")
        cart_window.geometry("500x600+0+0")

        lbl_title = Label(cart_window, text="YOUR CART", font=("times new roman", 30, "bold"), bg="white", fg="black",
                          bd=5, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=500, height=50)

        y_position = 52
        for item in self.cart:
            cname, cprice = item
            cart_item_frame = Frame(cart_window, bd=3, relief=RIDGE)
            cart_item_frame.place(x=0, y=y_position, width=500, height=90)

            

            lbl_cname = Label(cart_item_frame, text=cname, font=("times new roman", 17, "bold"), fg="black", bd=0,
                              relief=RIDGE)
            lbl_cname.place(x=-38, y=-10, width=500, height=50)

            lbl_price = Label(cart_item_frame, text="Price: ₹" + str(cprice), font=("times new roman", 17, "bold"),
                              fg="black", bd=0, relief=RIDGE)
            lbl_price.place(x=-35, y=30, width=500, height=50)

            y_position += 91

        payment_btn = Button(cart_window, bd=2, relief=RIDGE, text="Pay Now", font=("times new roman", 15, "bold"),
                             bg="black", fg="white", command=self.pay)
        payment_btn.place(x=20, y=20, width=160, height=40)
              
       


        def pay(self):
        # Implement payment functionality here
            messagebox.showinfo("Payment", "Payment Successful!")

            




if __name__ == "__main__":
    root = Tk()
    menu_instance = menu(root)
    root.mainloop()
