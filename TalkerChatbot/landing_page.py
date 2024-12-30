from tkinter import *
from PIL import ImageTk

class Landing_Page:
    def __init__(self):
        self.landing_window = Tk()
        self.landing_window.title("Talker")
        self.icon = PhotoImage(file="talker-logo.png")
        self.landing_window.iconphoto(True, self.icon)
        self.img = ImageTk.PhotoImage(file="landing-pagee.jpg")

        bgLabel = Label(self.landing_window, image=self.img)
        bgLabel.grid(row=0, column=0)

        login_button = Button(self.landing_window, text="Login", font=("Poppins Regular", 15, 'bold'), height=1,width=20, fg='black',bg='gold',
                              command=self.loginPage)
        login_button.place(x=70, y=350)

        signup_button = Button(self.landing_window, text="SignUp", font=("Poppins Regular", 15, 'bold'), height=1,
                              width=20, fg='black', bg='gold', command=self.signupPage)
        signup_button.place(x=70, y=430)

        self.landing_window.mainloop()

    def loginPage(self):
        self.landing_window.destroy()
        import login

    def signupPage(self):
        self.landing_window.destroy()
        import signup

# Landing_Page()