from tkinter import *
from PIL import Image,ImageTk
import os
import sqlite3
from tkinter import messagebox

main= Tk()
main.geometry("1366x768+60+10")
main.title("Login")
main.resizable(0, 0)
conn = sqlite3.connect('EmployeeInfo.db')
c = conn.cursor()
record_id = employeeID.get()
c.execute("SELECT*from employees WHERE oid = " + record_id)
records = c.fetchall()
global fullname
global department
global age
global gender
global contact
global address

myimg = ImageTk.PhotoImage(Image.open('./images/update.png'))
Label(image=myimg).pack()
fullname_lbl = Label(main, text="Full Name", font=('Consolas', 15), bg="white")
fullname_lbl.place(x=180, y=200)
department_lbl = Label(main, text="Department", font=('Consolas', 15), bg="white")
department_lbl.place(x=720, y=200)
age_lbl = Label(main, text="Age", font=('Consolas', 15), bg="white")
age_lbl.place(x=180, y=290)
gender_lbl = Label(main, text="Gender", font=('Consolas', 15), bg="white")
gender_lbl.place(x=720, y=290)
contact_lbl = Label(main, text="Contact", font=('Consolas', 15), bg="white")
contact_lbl.place(x=180, y=380)
address_lbl = Label(main, text="Address", font=('Consolas', 15), bg="white")
address_lbl.place(x=720, y=380)

fullname = Entry(main, width=25, border=0, font=('Consolas', 15))
fullname.place(x=180, y=230)
department = Entry(main, width=25, border=0, font=('Consolas', 15))
department.place(x=720, y=230)
age = Entry(main, width=25, border=0, font=('Consolas', 15))
age.place(x=180, y=320)
gender = Entry(main, width=25, border=0, font=('Consolas', 15))
gender.place(x=720, y=320)
contact = Entry(main, width=25, border=0, font=('Consolas', 15))
contact.place(x=180, y=410)
address = Entry(main, width=25, border=0, font=('Consolas', 15))
address.place(x=720, y=410)
add_btn = Button(main, text="ADD", font=('Consolas', 15), cursor='hand2',
                     bg="#00bff3", border=0, activebackground="#00bff3", padx=25, pady=10)
add_btn.place(x=560, y=630)
clear_btn = Button(main, text="CLEAR", font=('Consolas', 15), cursor='hand2',
                       bg="#00bff3", border=0, activebackground="#00bff3", padx=25, pady=10)
clear_btn.place(x=715, y=630)
main.mainloop()