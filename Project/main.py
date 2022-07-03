'''
Pizza Ordering Simulator 
By Aaditya Kumar Muktavarapu
HU21CSEN0100580
amuktava@gitam.in
'''
from ast import Lambda
from getpass import getuser
from pkgutil import extend_path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter
from tkinter import *
import sqlite3

#Database Creation
conn=sqlite3.connect("Database.db")

#Cursor Creation
c=conn.cursor()

#Table Creation

#User Table
c.execute("""
            CREATE TABLE IF NOT EXISTS User("Phone number" int PRIMARY KEY,
            "Name" text,"Username" text, "Password" text)
            """)

conn.commit()

#home screen
home=Tk()
home.title("Aadi's Pizzeria")
home.geometry("500x300")
FONT=("Comic Sans MS",20,"bold")
lbl = Label(home, text = "Welcome to Aadi's Pizzeria",font=FONT)
lbl.pack()

#User Entries
l5=Label(home,text="Enter Username: ")
l5.pack()
si_username=Entry(home)
si_username.pack()
l6=Label(home,text="Enter Password: ")
l6.pack()
si_password=Entry(home,show="*")
si_password.pack()

#Order Window
def orderwin():
    for widget in home.winfo_children():
            widget.destroy()
    home.geometry("700x600")
    home.title("Order Your Pizza")

    orderfont=("",20,"bold")
    l7=Label(home,text="Order Your Pizza",anchor="center",font=orderfont)
    l7.pack()

    sizefont=("",14,"")
    l8=Label(home,text="Size",anchor="center",font=sizefont)
    l8.pack()

    #Empty list to store and add prices
    total=[]
    #Size of the pizza base
    def basesize():
        sizelabel=Label(home,text=r.get())
        sizelabel.pack()
        if r.get()=="Small":
            total.append(99)
            #print(total)
        elif r.get()=="Medium":
            total.append(199)
            #print(total)
        elif r.get()=="Large":
            total.append(399)
            #print(total)
    
    r=StringVar()
    r.set('Small')
    Radiobutton(home,text="Small (₹99)",variable=r,value="Small",command=basesize).pack()
    Radiobutton(home,text="Medium (₹199)",variable=r,value="Medium",command=basesize).pack()
    Radiobutton(home,text="Large (₹399)",variable=r,value="Large",command=basesize).pack()
   

    #Choice of toppings
    toppingfont=("",14,"")
    l9=Label(home,text="Toppings",anchor="center",font=toppingfont)
    l9.pack()

    toppings=[
        ("Sausage (₹40)","Sausage"),
        ("Chicken (₹40)","Chicken"),
        ("Pepperoni (₹40)","Pepperoni"),
        ("Extra Cheese (₹35)","Extra Cheese"),
        ("Olives (₹35)","Olives"),
        ("Jalepenos (₹35)","Jalepenos")
    ]
    top=StringVar()
    top.set("Sausage")

    def topprice():
        toplabel=Label(home,text=top.get())
        toplabel.pack()
        if top.get()=="Sausage":
            total.append(40)
            #print(total)
        elif top.get()=="Chicken":
            total.append(40)
            #print(total)
        elif top.get()=="Pepperoni":
            total.append(40)
            #print(total)
        elif top.get()=="Extra Cheese":
            total.append(35)
            #print(total)
        elif top.get()=="Olives":
            total.append(35)
            #print(total)
        elif top.get()=="Jalepenos":
            total.append(35)
            #print(total)

    for text,cost in toppings:
        Radiobutton(home,text=text,variable=top,value=cost,command=topprice).pack()
 

    def place():
        p=0
        for i in range(0,len(total)):
            p+=total[i]
        #print(p)
        confirm=Label(home,text="Your Order has been Confirmed! Your total is: ₹").pack()
        confirmp=Label(home,text=p).pack()
        thanks=Label(home,text="Thank You for ordering!").pack()

    placeorder=Button(home,text="Place Order",command=place)
    placeorder.pack()



#Sign up Window
def suw():
    global signupwin
    signupwin=Toplevel()
    signupwin.geometry("500x300")
    signupwin.title("Create Account")
    
    #Text box to enter user details
    l=Label(signupwin,text="Enter Name: ")
    l.pack()
    name=Entry(signupwin)
    name.pack()
    l1=Label(signupwin,text="Enter Username: ")
    l1.pack()
    su_username=Entry(signupwin)
    su_username.pack()
    l2=Label(signupwin,text="Enter Password: ")
    l2.pack()
    su_password=Entry(signupwin)
    su_password.pack()
    l3=Label(signupwin,text="Re-enter your password: ")
    l3.pack()
    repass=Entry(signupwin)
    repass.pack()
    l4=Label(signupwin,text="Enter your Phone Number: ")
    l4.pack()
    ph=Entry(signupwin)
    ph.pack()
    

    #saving Details to database
    def save():
        
        getname=name.get()
        getus=su_username.get()
        getpass=su_password.get()
        getrepass=repass.get()
        getph=ph.get()
        
        values=(getph,getname,getus,getpass)
        if getpass==getrepass:
            c.execute("INSERT into User VALUES(?,?,?,?)",values)
            conn.commit()
            orderwin()
                
        else:
            elbl=Label(signupwin,text="Passwords not Matching")
            elbl.pack()

        #ul=Label(signupwin,text=getus)
        #ul.pack()
    store=Button(signupwin,text="Save Details",command=save)
    store.pack()

#retrieving username and password from database and comparing with user inputted credentials
def check():
    getluser=si_username.get()
    getlpass=si_password.get()
    c.execute("SELECT * from User WHERE Username=(?)",(getluser,))
    data=c.fetchall()
    conn.commit()
    if getlpass==data[0][3] or getuser==data[0][1]:
        #suclbl=Label(home,text="Success!")
        #suclbl.pack()
        orderwin()
    else:
        elbl1=Label(home,text="Invalid Credentials")
        elbl1.pack()

SI=Button(home,text="Sign in",command=check)
SI.pack()
SU=Button(home,text="Sign up",command=suw)
SU.pack()

home.mainloop()
