from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql


# Base Class: Implements Encapsulation and Abstraction
class ChatbotPage:
    def __init__(self, root):
        self.root = root

    def clear_window(self):
        """Clears all widgets from the window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_page(self):
        """Abstract method for showing page content."""
        raise NotImplementedError("Subclasses must implement show_page")


# Derived Class: Inheritance and Polymorphism
class LandingPage(ChatbotPage):
    def show_page(self):
        self.clear_window()

        img = ImageTk.PhotoImage(file="landing-pagee.jpg")
        bg_label = Label(self.root, image=img)
        bg_label.image = img
        bg_label.pack()

        Button(self.root, text="Login", font=("Poppins Regular", 15, 'bold'), bg='gold',
               command=lambda: LoginPage(self.root).show_page()).place(x=70, y=350)
        Button(self.root, text="SignUp", font=("Poppins Regular", 15, 'bold'), bg='gold',
               command=lambda: SignupPage(self.root).show_page()).place(x=70, y=430)


class LoginPage(ChatbotPage):
    def show_page(self):
        self.clear_window()

        img = ImageTk.PhotoImage(file="login-page.png")
        bg_label = Label(self.root, image=img)
        bg_label.image = img
        bg_label.pack()

        Label(self.root, text="Email:", font=("Poppins Regular", 15), bg='white').place(x=600, y=150)
        email_entry = Entry(self.root, font=("Poppins Regular", 12), width=32, bg='light blue')
        email_entry.place(x=600, y=190)

        Label(self.root, text="Password:", font=("Poppins Regular", 15), bg='white').place(x=600, y=240)
        pass_entry = Entry(self.root, font=("Poppins Regular", 12), width=32, bg='light blue')
        pass_entry.place(x=600, y=280)

        Button(self.root, text="<", font=("Poppins Regular", 12), bg='gold',
               command=lambda: LandingPage(self.root).show_page()).place(x=3, y=553)
        Button(self.root, text="I'm done", font=("Poppins Regular", 12), bg='gold', command=self.validate_login).place(x=660, y=370)

    def validate_login(self):
        # Example of Encapsulation for DB access
        _host = "localhost"
        _user = "root"
        _password = "password"
        email = "example@example.com"  # Mock email; fetch from entry in real implementation.

        try:
            connection = pymysql.connect(host=_host, user=_user, password=_password)
            cursor = connection.cursor()
            cursor.execute("USE TALKER")
            # Perform login query...
            messagebox.showinfo("Success", "Logged in successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


class SignupPage(ChatbotPage):
    def show_page(self):
        self.clear_window()
        # Similar to LoginPage, implement specific UI and functionality


# Application Class
class TalkerChatbot:
    def __init__(self):
        self.root = Tk()
        self.root.title("Talker")
        self.icon = PhotoImage(file="talker-logo.png")
        self.root.iconphoto(True, self.icon)

        # Start with the Landing Page
        LandingPage(self.root).show_page()

        self.root.mainloop()


# Run the application
TalkerChatbot()
