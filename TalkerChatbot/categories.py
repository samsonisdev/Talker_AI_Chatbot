from tkinter import *
from PIL import ImageTk

class CategoryPage:
    def __init__(self):
        self.category_window = Tk()
        self.category_window.title("Talker Categories")

        self.bg = ImageTk.PhotoImage(file='category-page.jpg')
        self.bgLabel = Label(self.category_window, image=self.bg)
        self.bgLabel.grid(row=0, column=0)

        self.home = Button(self.category_window, text='Home', font=("Poppins Regular", 12), width='10', bg='gold')
        self.home.place(x=875, y=12)

        self.study = Button(self.category_window, text="Study", font=("Poppins Regular", 15), width='20', bg='gold', command=self.study_chat)
        self.study.place(x=200, y=250)

        self.research = Button(self.category_window, text="Research", font=("Poppins Regular", 15), width='20', bg='gold', command=self.research_chat)
        self.research.place(x=200, y=350)

        self.business = Button(self.category_window, text="Business", font=("Poppins Regular", 15), width='20', bg='gold', command=self.business_chat)
        self.business.place(x=550, y=250)

        self.general = Button(self.category_window, text="General", font=("Poppins Regular", 15), width='20', bg='gold', command=self.general_chat)
        self.general.place(x=550, y=350)

        self.category_window.mainloop()


    def study_chat(self):
        self.category_window.destroy()
        from talker_chat import StudyChat
        StudyChat()

    def research_chat(self):
        self.category_window.destroy()
        from talker_chat import ResearchChat
        ResearchChat()

    def business_chat(self):
        self.category_window.destroy()
        from talker_chat import BusinessChat
        BusinessChat()

    def general_chat(self):
        self.category_window.destroy()
        from talker_chat import GeneralChat
        GeneralChat()


# CategoryPage()