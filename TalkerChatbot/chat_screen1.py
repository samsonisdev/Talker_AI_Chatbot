from tkinter import *
from PIL import ImageTk

class StudyScreen:
    def __init__(self):
        self.window = Tk()
        self.studies_screen()
        self.window.mainloop()

    def studies_screen(self):
        self.bg = ImageTk.PhotoImage(file='chatscreen-study.jpg')
        self.image_label = Label(self.window, image=self.bg)
        self.image_label.grid(row=0, column=0)

        self.entry = Entry(self.window, width=40, font=('Poppins Regular', 15), foreground='black', relief=FLAT, border=0)
        self.entry.place(x=150, y=295)

        self.send = Button(self.window, width=5, height=1, text='>', font=('Poppins Regular', 14, 'bold'), background='gold', foreground='black', command=self.main_chat)
        self.send.place(x=790, y = 284)
        def on_enter(e):
            self.entry.delete(0, 'end')
            self.entry.config(fg='black')

        self.entry.insert(0, 'Message Talker...')
        self.entry.config(fg='seashell4')
        self.entry.bind('<FocusIn>', on_enter)

    def main_chat(self):
        self.window.destroy()
        from talker_chat import TalkerChat

StudyScreen()

class GeneralScreen:
    def __init__(self):
        self.window = Tk()
        self.general_screen()
        self.window.mainloop()
    def general_screen(self):
        self.bg = ImageTk.PhotoImage(file='chatscreen-general.jpg')
        self.image_label = Label(self.window, image=self.bg)
        self.image_label.grid(row=0, column=0)

        self.entry = Entry(self.window, width=40, font=('Poppins Regular', 15), foreground='black', relief=FLAT,
                           border=0)
        self.entry.place(x=150, y=295)

        self.send = Button(self.window, width=5, height=1, text='>', font=('Poppins Regular', 14, 'bold'), background='gold', foreground='black', command=self.main_chat)
        self.send.place(x=790, y = 284)

        def on_enter(e):
            self.entry.delete(0, 'end')
            self.entry.config(fg='black')

        self.entry.insert(0, 'Message Talker...')
        self.entry.config(fg='seashell4')
        self.entry.bind('<FocusIn>', on_enter)

    def main_chat(self):
        self.window.destroy()
        from talker_chat import TalkerChat

class ResearchScreen:
    def __init__(self):
        self.window = Tk()
        self.research_screen()
        self.window.mainloop()

    def research_screen(self):
        self.bg = ImageTk.PhotoImage(file='chatscreen-research.jpg')
        self.image_label = Label(self.window, image=self.bg)
        self.image_label.grid(row=0, column=0)

        self.entry = Entry(self.window, width=40, font=('Poppins Regular', 15), foreground='black', relief=FLAT,
                           border=0)
        self.entry.place(x=150, y=295)

        self.send = Button(self.window, width=5, height=1, text='>', font=('Poppins Regular', 14, 'bold'), background='gold', foreground='black', command=self.main_chat)
        self.send.place(x=790, y = 284)

        def on_enter(e):
            self.entry.delete(0, 'end')
            self.entry.config(fg='black')

        self.entry.insert(0, 'Message Talker...')
        self.entry.config(fg='seashell4')
        self.entry.bind('<FocusIn>', on_enter)

    def main_chat(self):
        self.window.destroy()
        from talker_chat import TalkerChat

class BusinessScreen:
    def __init__(self):
        self.window = Tk()
        self.business_screen()
        self.window.mainloop()

    def business_screen(self):
        self.bg = ImageTk.PhotoImage(file='chatscreen-business.jpg')
        self.image_label = Label(self.window, image=self.bg)
        self.image_label.grid(row=0, column=0)

        self.entry = Entry(self.window, width=40, font=('Poppins Regular', 15), foreground='black', relief=FLAT,
                           border=0)
        self.entry.place(x=150, y=295)

        self.send = Button(self.window, width=5, height=1, text='>', font=('Poppins Regular', 14, 'bold'), background='gold', foreground='black', command=self.main_chat)
        self.send.place(x=790, y = 284)

        def on_enter(e):
            self.entry.delete(0, 'end')
            self.entry.config(fg='black')

        self.entry.insert(0, 'Message Talker...')
        self.entry.config(fg='seashell4')
        self.entry.bind('<FocusIn>', on_enter)

    def main_chat(self):
        self.window.destroy()
        from talker_chat import TalkerChat


