from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import google.generativeai as genai

class TalkerChatbot:
    def __init__(self):
        self.root = Tk()
        self.root.title("Talker")
        self.icon = PhotoImage(file="talker-logo.png")
        self.root.iconphoto(True, self.icon)

        self.show_landing_page()

        self.root.mainloop()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_landing_page(self):
        self.clear_window()

        img = ImageTk.PhotoImage(file="landing-pagee.jpg")
        bg_label = Label(self.root, image=img)
        bg_label.image = img  # Keep a reference to avoid garbage collection
        bg_label.pack()

        login_button = Button(self.root, text="Login", font=("Poppins Regular", 15, 'bold'), height=1, width=20, fg='black', bg='gold',
                              command=self.show_login_page)
        login_button.place(x=70, y=350)

        signup_button = Button(self.root, text="SignUp", font=("Poppins Regular", 15, 'bold'), height=1, width=20, fg='black', bg='gold',
                                command=self.show_signup_page)
        signup_button.place(x=70, y=430)

    def show_login_page(self):
        self.clear_window()

        img = ImageTk.PhotoImage(file="login-page.png")
        bg_label = Label(self.root, image=img)
        bg_label.image = img
        bg_label.pack()

        self.email_label = Label(self.root, text="Email:", font=("Poppins Regular", 15), bg='white')
        self.email_label.place(x=600, y=150)
        self.email_entry = Entry(self.root, font=("Poppins Regular", 12), width=32, bg='light blue')
        self.email_entry.place(x=600, y=190)

        self.pass_label = Label(self.root, text="Password:", font=("Poppins Regular", 15), bg='white')
        self.pass_label.place(x=600, y=240)
        self.pass_entry = Entry(self.root, font=("Poppins Regular", 12), width=32, bg='light blue')
        self.pass_entry.place(x=600, y=280)

        self.donebutton = Button(self.root, text="I'm done", font=("Poppins Regular", 12), height=1, width=20, fg='black', bg='gold',
                            command=self.done)
        self.donebutton.place(x=660, y=370)

        back_button = Button(self.root, text="<", font=("Poppins Regular", 12), height=1, width=10, fg='black', bg='gold',
                             command=self.show_landing_page)
        back_button.place(x=3, y=553)

    def done(self):

        if self.email_entry.get() == "" or self.pass_entry.get() == "":
            messagebox.showinfo('Error', 'All fields must be filled')

        else:
            try:
                self.connection = pymysql.connect(host='localhost', user='root', password='samsonSQL.123')
                self.curser = self.connection.cursor()
            except:
                return

            self.curser.execute('use TALKER')

            query = 'select * from talkerdata where Email=%s and Password=%s'
            self.curser.execute(query, (self.email_entry.get(), self.pass_entry.get()))
            emailnpass = self.curser.fetchone()

            if emailnpass == None:
                messagebox.showerror('Error', 'Email or Password do not match')
            else:
                self.clear_window()
                self.show_category_page()

    def show_signup_page(self):
        self.clear_window()

        img = ImageTk.PhotoImage(file="signup-page.jpg")
        bg_label = Label(self.root, image=img)
        bg_label.image = img
        bg_label.pack()

        self.emailLabel = Label(self.root, text="Email:", font=("Poppins Regular", 15), bg='white')
        self.emailLabel.place(x=600, y=140)
        self.emailEntry = Entry(self.root, font=("Poppins Regular", 12), width=32, bg='light blue')
        self.emailEntry.place(x=600, y=180)

        self.usernameLabel = Label(self.root, text="Username:", font=("Poppins Regular", 15), bg='white')
        self.usernameLabel.place(x=600, y=220)
        self.usernameEntry = Entry(self.root, font=("Poppins Regular", 12), width=32, bg='light blue')
        self.usernameEntry.place(x=600, y=260)

        self.passLabel = Label(self.root, text="Password:", font=("Poppins Regular", 15), bg='white')
        self.passLabel.place(x=600, y=310)
        self.passEntry = Entry(self.root, font=("Poppins Regular", 12), width=32, bg='light blue')
        self.passEntry.place(x=600, y=350)

        self.confirmPass_label = Label(self.root, text="Confirm Password:", font=("Poppins Regular", 15), bg='white')
        self.confirmPass_label.place(x=600, y=400)
        self.confirmPass_entry = Entry(self.root, font=("Poppins Regular", 12), width=32, bg='light blue')
        self.confirmPass_entry.place(x=600, y=440)

        self.donebutton = Button(self.root, text="I'm done", font=("Poppins Regular", 12), height=1, width=20, fg='black', bg='gold', command=self.signup_done)
        self.donebutton.place(x=660, y=490)

        back_button = Button(self.root, text="<", font=("Poppins Regular", 12), height=1, width=10, fg='black', bg='gold',
                             command=self.show_landing_page)
        back_button.place(x=3, y=553)

    def signup_done(self):

        if self.emailEntry.get() == '' or self.usernameEntry.get() == '' or self.passEntry.get() == '' or self.confirmPass_entry.get() == '':
            messagebox.showinfo('Error', 'All fields must be filled!')
        elif self.passEntry.get() != self.confirmPass_entry.get():
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

                self.clear_window()
                self.show_login_page()

    def show_category_page(self):
        self.clear_window()
        img = ImageTk.PhotoImage(file="category-page.jpg")
        bg_label = Label(self.root, image=img)
        bg_label.image = img
        bg_label.pack()
        self.home = Button(self.root, text='Home', font=("Poppins Regular", 12), width='10', bg='gold', command=self.show_landing_page)
        self.home.place(x=875, y=12)

        self.study = Button(self.root, text="Study", font=("Poppins Regular", 15), width='20', bg='gold',
                            command=self.study_chat)
        self.study.place(x=200, y=250)

        self.research = Button(self.root, text="Research", font=("Poppins Regular", 15), width='20',
                               bg='gold', command=self.research_chat)
        self.research.place(x=200, y=350)

        self.business = Button(self.root, text="Business", font=("Poppins Regular", 15), width='20',
                               bg='gold', command=self.business_chat)
        self.business.place(x=550, y=250)

        self.general = Button(self.root, text="General", font=("Poppins Regular", 15), width='20', bg='gold',
                              command=self.general_chat)
        self.general.place(x=550, y=350)

    def study_chat(self):
        self.clear_window()
        img = ImageTk.PhotoImage(file="studies-chat.jpg")
        bg_label = Label(self.root, image=img)
        bg_label.image = img
        bg_label.pack()
        back_button = Button(self.root, text="<", font=("Poppins Regular", 12), height=1, width=10, fg='black', bg='gold',
                             command=self.show_category_page)
        back_button.place(x=3, y=553)
        self.chat_talker()
        pass

    def research_chat(self):
        self.clear_window()
        img = ImageTk.PhotoImage(file="research-chat.jpg")
        bg_label = Label(self.root, image=img)
        bg_label.image = img
        bg_label.pack()
        back_button = Button(self.root, text="<", font=("Poppins Regular", 12), height=1, width=10, fg='black', bg='gold',
                             command=self.show_category_page)
        back_button.place(x=3, y=553)
        self.chat_talker()
        pass

    def business_chat(self):
        self.clear_window()
        img = ImageTk.PhotoImage(file="business-chat.jpg")
        bg_label = Label(self.root, image=img)
        bg_label.image = img
        bg_label.pack()
        back_button = Button(self.root, text="<", font=("Poppins Regular", 12), height=1, width=10, fg='black', bg='gold',
                             command=self.show_category_page)
        back_button.place(x=3, y=553)
        self.chat_talker()
        pass

    def general_chat(self):
        self.clear_window()
        img = ImageTk.PhotoImage(file="general-chat.jpg")
        bg_label = Label(self.root, image=img)
        bg_label.image = img
        bg_label.pack()
        back_button = Button(self.root, text="<", font=("Poppins Regular", 12), height=1, width=10, fg='black', bg='gold',
                             command=self.show_category_page)
        back_button.place(x=3, y=553)
        self.chat_talker()
        pass

    def chat_talker(self):
        self.chat_frame = Frame(height=355, width=730)
        self.chat_frame.place(x=132, y=80)

        self.entry = Entry(self.root, width=54, font=('Poppins Regular', 15), foreground='black', relief=FLAT, border=0)
        self.entry.place(x=145, y=465)
        self.send = Button(self.root, width=5, height=1, text='>', font=('Poppins Regular', 14, 'bold'), background='gold', foreground='black', command=self.send_message)
        self.send.place(x=789, y=451)

        self.entry.insert(0, 'Message Talker...')
        self.entry.config(fg='seashell4')
        self.entry.bind('<FocusIn>', self.on_enter)

    def send_message(self):

        yi = 10

        genai.configure(api_key="AIzaSyCpwngYdzfcQAFwL3j9gkD11tjUYeeWkUA")
        model = genai.GenerativeModel('gemini-1.5-flash')

        self.prompt = self.entry.get()
        self.prompt_label = Label(self.chat_frame, text=self.prompt, height=1, width=58, font=('Poppins Regular', 15), foreground='black', background='light blue', anchor='e')
        self.prompt_label.place(x=15, y=yi)

        chat = model.start_chat(history=[])
        self.response = chat.send_message(self.prompt)
        self.response_label = Label(self.chat_frame, text=self.response.text, height=2, width=58, font=('Poppins Regular', 15), foreground='black', background='white', anchor='w')
        self.response_label.place(x=15, y=yi+50)

        yi += 10

    def on_enter(self, e):
        self.entry.delete(0, 'end')
        self.entry.config(fg='black')


TalkerChatbot()
