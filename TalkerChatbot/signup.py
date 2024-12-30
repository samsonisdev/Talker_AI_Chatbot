from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import cryptography

class SignUp:
    def __init__(self):
        self.signup_window = Tk()
        self.signup_window.title("SignUp")
        self.icon = PhotoImage(file="talker-logo.png")
        self.signup_window.iconphoto(True, self.icon)
        self.img = ImageTk.PhotoImage(file="signup-page.jpg")

        self.bgLabel = Label(self.signup_window, image=self.img)
        self.bgLabel.grid(row=0, column=0)

        self.emailLabel = Label(self.signup_window, text="Email:", font=("Poppins Regular", 15), bg='white')
        self.emailLabel.place(x=600, y=140)
        self.emailEntry = Entry(self.signup_window, font=("Poppins Regular", 12), width=32, bg='light blue')
        self.emailEntry.place(x=600, y=180)

        self.usernameLabel = Label(self.signup_window, text="Username:", font=("Poppins Regular", 15), bg='white')
        self.usernameLabel.place(x=600, y=220)
        self.usernameEntry = Entry(self.signup_window, font=("Poppins Regular", 12), width=32, bg='light blue')
        self.usernameEntry.place(x=600, y=260)

        self.passLabel = Label(self.signup_window, text="Password:", font=("Poppins Regular", 15), bg='white')
        self.passLabel.place(x=600, y=310)
        self.passEntry = Entry(self.signup_window, font=("Poppins Regular", 12), width=32, bg='light blue')
        self.passEntry.place(x=600, y=350)

        self.confirmpassLabel = Label(self.signup_window, text="Confirm Password:", font=("Poppins Regular", 15), bg='white')
        self.confirmpassLabel.place(x=600, y=400)
        self.confirmpassEntry = Entry(self.signup_window, font=("Poppins Regular", 12), width=32, bg='light blue')
        self.confirmpassEntry.place(x=600, y=440)

        self.donebutton = Button(self.signup_window, text="I'm done", font=("Poppins Regular", 12), height=1, width=20, fg='black', bg='gold', command=self.login_page)
        self.donebutton.place(x=660, y=490)

        self.backbutton = Button(self.signup_window, text="<", font=("Poppins Regular", 12), height=1, width=10,
                            fg='black', bg='gold', command=self.back)
        self.backbutton.place(x=3, y=553)

        self.signup_window.mainloop()

    def back(self):
        self.signup_window.destroy()
        import landing_page

    def login_page(self):

        if self.emailEntry.get() == '' or self.usernameEntry.get() == '' or self.passEntry.get() == '' or self.confirmpassEntry.get() == '':
            messagebox.showinfo('Error', 'All fields must be filled!')
        elif self.passEntry.get() != self.confirmpassEntry.get():
            messagebox.showinfo('Error', "Passwords do not match")
        else:
            try:
                self.connection = pymysql.connect(host='localhost', user='root', password='samsonSQL.123')
                self.curser = self.connection.cursor()
            except:
                messagebox.showinfo('Error', 'Connectivity Error')
                return
            try:
                self.curser.execute('create database TALKER')
                self.curser.execute('use TALKER')
                self.curser.execute('create table talkerdata(ID int auto_increment primary key not null, Email varchar(30), Username varchar(20), Password varchar(20))')
            except:
                self.curser.execute('use TALKER')

            # making sure the new username is not same as the old one
            query = 'select * from talkerdata where Username=%s'
            self.curser.execute(query, (self.usernameEntry.get()))

            row = self.curser.fetchone()

            if row != None:
                messagebox.showinfo('Error', 'Username Already Exists')
            else:
                query = 'insert into talkerdata(Email,Username,Password) values(%s, %s, %s)'
                self.curser.execute(query, (self.emailEntry.get(), self.usernameEntry.get(), self.passEntry.get()))

                self.connection.commit()
                self.connection.close()

                self.signup_window.destroy()
                import login

# SignUp()