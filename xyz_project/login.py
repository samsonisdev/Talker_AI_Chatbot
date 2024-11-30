from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

class Login:
    def __init__(self):
        self.login_window = Tk()
        self.login_window.title("Login")
        self.icon = PhotoImage(file="talker-logo.png")
        self.login_window.iconphoto(True, self.icon)
        self.img = ImageTk.PhotoImage(file="login-page.png")

        self.bgLabel = Label(self.login_window, image=self.img)
        self.bgLabel.grid(row=0, column=0)

        self.emailLabel = Label(self.login_window, text="Email:", font=("Poppins Regular", 15), bg='white')
        self.emailLabel.place(x=600, y=150)
        self.emailEntry = Entry(self.login_window, font=("Poppins Regular", 12), width=32, bg='light blue')
        self.emailEntry.place(x=600, y=190)


        self.passLabel = Label(self.login_window, text="Password:", font=("Poppins Regular", 15), bg='white')
        self.passLabel.place(x=600, y=240)
        self.passEntry = Entry(self.login_window, font=("Poppins Regular", 12), width=32, bg='light blue')
        self.passEntry.place(x=600, y=280)

        self.donebutton = Button(self.login_window, text="I'm done", font=("Poppins Regular", 12), height=1, width=20, fg='black', bg='gold',
                            command=self.done)
        self.donebutton.place(x=660, y=370)

        self.backbutton = Button(self.login_window, text="<", font=("Poppins Regular", 12), height=1, width=10,
                            fg='black', bg='gold', command=self.back)
        self.backbutton.place(x=3, y=553)

        self.login_window.mainloop()

    def back(self):
        self.login_window.destroy()
        import landing_page

    def done(self):

        if self.emailEntry.get() == "" or self.passEntry.get() == "":
            messagebox.showinfo('Error', 'All fields must be filled')

        else:
            try:
                self.connection = pymysql.connect(host='localhost', user='root', password='samsonSQL.123')
                self.curser = self.connection.cursor()
            except:
                return

            self.curser.execute('use TALKER')

            query = 'select * from talkerdata where Email=%s and Password=%s'
            self.curser.execute(query, (self.emailEntry.get(), self.passEntry.get()))
            emailnpass = self.curser.fetchone()

            if emailnpass == None:
                messagebox.showerror('Error', 'Email or Password do not match')
            else:
                self.login_window.destroy()
                import categories

Login()