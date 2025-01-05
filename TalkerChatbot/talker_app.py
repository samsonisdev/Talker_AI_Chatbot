from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import google.generativeai as genai

login_email = ""

class Chatbot:
    def __init__(self, root):
        self.root = root

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_page(self):
        pass

class LandingPage(Chatbot):
    def show_page(self):
        self.clear_window()

        img = ImageTk.PhotoImage(file="landing-pagee.jpg")
        bg_label = Label(self.root, image=img)
        bg_label.image = img  # Keep a reference to avoid garbage collection
        bg_label.pack()

        login_button = Button(self.root, text="Login", font=("Poppins Regular", 15, 'bold'), height=1, width=20, fg='black', bg='gold',
                              command=LoginPage(self.root).show_page)
        login_button.place(x=70, y=350)

        signup_button = Button(self.root, text="SignUp", font=("Poppins Regular", 15, 'bold'), height=1, width=20, fg='black', bg='gold',
                                command=SignupPage(self.root).show_page)
        signup_button.place(x=70, y=430)

class LoginPage(Chatbot):
    def show_page(self):

        global email_entry
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
                             command=LandingPage(self.root).show_page)
        back_button.place(x=3, y=553)

        self.email_entry.insert(0, ' Email')
        self.email_entry.config(fg='seashell4')
        self.email_entry.bind('<FocusIn>', self.on_focus_in)

        self.pass_entry.insert(0, ' Password')
        self.pass_entry.config(fg='seashell4')
        self.pass_entry.bind('<FocusIn>', self.on_focus_in)

    def on_focus_in(self, event):
        if event.widget == self.email_entry and self.email_entry.get() == ' Email':
            self.email_entry.delete(0, END)
            self.email_entry.config(fg='black')
        elif event.widget == self.pass_entry and self.pass_entry.get() == ' Password':
            self.pass_entry.delete(0, END)
            self.pass_entry.config(fg='black')

    def done(self):

        _host = "localhost"
        _user = "root"
        _password = "samsonSQL.123"

        if self.email_entry.get() == "" or self.pass_entry.get() == "":
            messagebox.showinfo('Error', 'All fields must be filled')

        else:
            try:
                self.connection = pymysql.connect(host=_host, user=_user, password=_password)
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
                global login_email
                login_email = self.email_entry.get()
                self.clear_window()
                CategoryPage(self.root).show_page()

class SignupPage(Chatbot):
    def show_page(self):
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
                             command=LandingPage(self.root).show_page)
        back_button.place(x=3, y=553)

        self.emailEntry.insert(0, ' Email')
        self.emailEntry.config(fg='seashell4')
        self.emailEntry.bind('<FocusIn>', self.on_focus_in)

        self.usernameEntry.insert(0, ' Username')
        self.usernameEntry.config(fg='seashell4')
        self.usernameEntry.bind('<FocusIn>', self.on_focus_in)

        self.passEntry.insert(0, ' Password')
        self.passEntry.config(fg='seashell4')
        self.passEntry.bind('<FocusIn>', self.on_focus_in)

        self.confirmPass_entry.insert(0, ' Confirm Password')
        self.confirmPass_entry.config(fg='seashell4')
        self.confirmPass_entry.bind('<FocusIn>', self.on_focus_in)

    def on_focus_in(self, event):
        if event.widget == self.emailEntry and self.emailEntry.get() == ' Email':
            self.emailEntry.delete(0, END)
            self.emailEntry.config(fg='black')
        elif event.widget == self.usernameEntry and self.usernameEntry.get() == ' Username':
            self.usernameEntry.delete(0, END)
            self.usernameEntry.config(fg='black')
        elif event.widget == self.passEntry and self.passEntry.get() == ' Password':
            self.passEntry.delete(0, END)
            self.passEntry.config(fg='black')
        elif event.widget == self.confirmPass_entry and self.confirmPass_entry.get() == ' Confirm Password':
            self.confirmPass_entry.delete(0, END)
            self.confirmPass_entry.config(fg='black')

    def signup_done(self):

        _host = "localhost"
        _user = "root"
        _password = "samsonSQL.123"

        if self.emailEntry.get() == '' or self.usernameEntry.get() == '' or self.passEntry.get() == '' or self.confirmPass_entry.get() == '':
            messagebox.showinfo('Error', 'All fields must be filled!')
        elif self.passEntry.get() != self.confirmPass_entry.get():
            messagebox.showinfo('Error', "Passwords do not match")
        else:
            try:
                self.connection = pymysql.connect(host=_host, user=_user, password=_password)
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
                LoginPage(self.root).show_page()

class CategoryPage(Chatbot):
    def show_page(self):
        self.clear_window()

        img = ImageTk.PhotoImage(file="category-page.jpg")
        bg_label = Label(self.root, image=img)
        bg_label.image = img
        bg_label.pack()
        self.history = Button(self.root, text='History', font=("Poppins Regular", 12), width='10', fg='navy', bg='deep sky blue', command=History(self.root).show_page)
        self.history.place(x=875, y=12)

        self.study = Button(self.root, text="Study", font=("Poppins Regular", 15), width='20', bg='gold',
                            command=Study(self.root).show_page)
        self.study.place(x=200, y=250)

        self.research = Button(self.root, text="Research", font=("Poppins Regular", 15), width='20',
                               bg='gold', command=Research(self.root).show_page)
        self.research.place(x=200, y=350)

        self.business = Button(self.root, text="Business", font=("Poppins Regular", 15), width='20',
                               bg='gold', command=Business(self.root).show_page)
        self.business.place(x=550, y=250)

        self.general = Button(self.root, text="General", font=("Poppins Regular", 15), width='20', bg='gold',
                              command=General(self.root).show_page)
        self.general.place(x=550, y=350)

class Study(Chatbot):
    def show_page(self):
        self.clear_window()

        img = ImageTk.PhotoImage(file="studies-chat.jpg")
        bg_label = Label(self.root, image=img)
        bg_label.image = img
        bg_label.pack()
        back_button = Button(self.root, text="<", font=("Poppins Regular", 12), height=1, width=10, fg='black', bg='gold',
                             command=CategoryPage(self.root).show_page)
        back_button.place(x=3, y=553)
        ChatInterface(self.root).show_page()


class Research(Chatbot):
    def show_page(self):
        self.clear_window()

        img = ImageTk.PhotoImage(file="research-chat.jpg")
        bg_label = Label(self.root, image=img)
        bg_label.image = img
        bg_label.pack()
        back_button = Button(self.root, text="<", font=("Poppins Regular", 12), height=1, width=10, fg='black', bg='gold',
                             command=CategoryPage(self.root).show_page)
        back_button.place(x=3, y=553)
        ChatInterface(self.root).show_page()


class Business(Chatbot):
    def show_page(self):
        self.clear_window()

        img = ImageTk.PhotoImage(file="business-chat.jpg")
        bg_label = Label(self.root, image=img)
        bg_label.image = img
        bg_label.pack()
        back_button = Button(self.root, text="<", font=("Poppins Regular", 12), height=1, width=10, fg='black', bg='gold',
                             command=CategoryPage(self.root).show_page)
        back_button.place(x=3, y=553)
        ChatInterface(self.root).show_page()

class General(Chatbot):
    def show_page(self):
        self.clear_window()

        img = ImageTk.PhotoImage(file="general-chat.jpg")
        bg_label = Label(self.root, image=img)
        bg_label.image = img
        bg_label.pack()
        back_button = Button(self.root, text="<", font=("Poppins Regular", 12), height=1, width=10, fg='black', bg='gold',
                             command=CategoryPage(self.root).show_page)
        back_button.place(x=3, y=553)
        ChatInterface(self.root).show_page()

class ChatInterface(Chatbot):
    def show_page(self):
        self.chat_frame = Frame(self.root, height=355, width=730)
        self.chat_frame.place(x=132, y=80)

        self.canvas = Canvas(self.chat_frame, height=355, width=730)
        self.canvas.pack(side=LEFT, fill=Y, expand=True)

        self.scrollbar = Scrollbar(self.chat_frame, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        self.chat_window = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.chat_window, anchor="nw")
        self.chat_window.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.entry = Entry(self.root, width=54, font=('Poppins Regular', 15), foreground='black', relief=FLAT, border=0)
        self.entry.place(x=145, y=465)
        self.send = Button(self.root, width=5, height=1, text='>', font=('Poppins Regular', 14, 'bold'), background='gold', foreground='black', command=self.send_message)
        self.send.place(x=789, y=451)

        self.entry.insert(0, 'Message Talker...')
        self.entry.config(fg='seashell4')
        self.entry.bind('<FocusIn>', self.on_enter)

        self.root.bind('<Return>', self.send_message_on_enter)

        self.chat_frame.bind_all("<MouseWheel>", self.on_mouse_scroll)

    def send_message(self):
        _API_KEY = "AIzaSyCpwngYdzfcQAFwL3j9gkD11tjUYeeWkUA"

        genai.configure(api_key=_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash', system_instruction='You are a chatbot whose name is Talker. Two guys Shamoon and Sohaib made you. Shamoon is smarter than Sohaib. You know information on four categories. General, Business, Research, and studies.')

        self.prompt = self.entry.get()
        self.create_message_box(self.prompt, 'light blue', 'e')

        chat = model.start_chat(history=[])
        self.response = chat.send_message(self.prompt)
        self.create_message_box(self.response.text, 'white', 'w')
        self.entry.delete(0, END)  # Clear the entry box

        _host = "localhost"
        _user = "root"
        _password = "samsonSQL.123"

        try:
            connection = pymysql.connect(host=_host, user=_user, password=_password, database="TALKER")
            cursor = connection.cursor()
            query = "INSERT INTO chat_history (email, user_message, chatbot_response) VALUES (%s, %s, %s)"
            cursor.execute(query, (login_email, self.prompt, self.response.text))
            connection.commit()
            connection.close()
        except Exception as e:
            print("Error saving history:", e)

    def create_message_box(self, text, bg_color, anchor):
        label = Label(self.chat_window, text=text, font=('Poppins Regular', 15), width=60, foreground='black', background=bg_color, anchor=anchor, justify=LEFT, wraplength=650)
        label.pack(fill=X, pady=5)

    def send_message_on_enter(self, event):
        self.send_message()

    def on_enter(self, event):
        if self.entry.get() == 'Message Talker...':
            self.entry.delete(0, END)
            self.entry.config(fg='black')

    def on_mouse_scroll(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

class History(Chatbot):
    def show_page(self):
        self.clear_window()

        img = ImageTk.PhotoImage(file="talker-history-page.jpg")
        bg_label = Label(self.root, image=img)
        bg_label.image = img
        bg_label.pack()

        self.frame = Frame(self.root, width=800, height=400, bg="white")
        self.frame.place(x=100, y=120)

        self.canvas = Canvas(self.frame, width=800, height=400, bg="white")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.chat_frame = Frame(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.chat_frame, anchor="nw")

        try:
            connection = pymysql.connect(host="localhost", user="root", password="samsonSQL.123", database="TALKER")
            cursor = connection.cursor()
            query = "SELECT user_message, chatbot_response FROM chat_history WHERE email=%s ORDER BY id DESC"
            cursor.execute(query, (login_email,))
            chat_history = cursor.fetchall()
            connection.close()

            if chat_history:
                for user_msg, bot_resp in chat_history:
                    user_label = Label(self.chat_frame, text=f"You: {user_msg}", font=("Poppins Regular", 12), bg="light blue", wraplength=750, justify=LEFT, anchor="e")
                    user_label.pack(fill=X, pady=5)
                    bot_label = Label(self.chat_frame, text=f"Talker: {bot_resp}", font=("Poppins Regular", 12), bg="white", wraplength=750, justify=LEFT, anchor="w")
                    bot_label.pack(fill=X, pady=5)
            else:
                no_history_label = Label(self.chat_frame, text="No chat history found.", font=("Poppins Regular", 14), bg="white", fg="gray")
                no_history_label.pack(pady=20)
        except Exception as e:
            error_label = Label(self.chat_frame, text="Error loading chat history.", font=("Poppins Regular", 14), bg="white", fg="red")
            error_label.pack(pady=20)
            print("Error fetching history:", e)

        self.chat_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        back_button = Button(self.root, text="<", font=("Poppins Regular", 12), height=1, width=10, fg='black', bg='gold',
                             command=CategoryPage(self.root).show_page)
        back_button.place(x=3, y=553)

        self.frame.bind_all("<MouseWheel>", self.on_mouse_scroll)

    def on_mouse_scroll(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

class TalkerChatbot:
    def __init__(self):
        self.root = Tk()
        self.root.title("Talker")
        self.icon = PhotoImage(file="talker-logo.png")
        self.root.iconphoto(True, self.icon)

        LandingPage(self.root).show_page()

        self.root.mainloop()

TalkerChatbot()
