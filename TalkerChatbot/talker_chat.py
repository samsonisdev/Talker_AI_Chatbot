from tkinter import *
from PIL import ImageTk
import google.generativeai as genai

class TalkerChat:
    def __init__(self):
        self.chat_window = Tk()
        self.chat_window.geometry('990x600')

    def place_image(self, image):
        self.img = ImageTk.PhotoImage(file=image)
        self.img_label = Label(self.chat_window, image=self.img)
        self.img_label.place(x=0, y=0)

        # self.img = ImageTk.PhotoImage(file=image)
        # self.img_label = Label(self.chat_window, image=self.img)
        # self.img_label.place(x=0, y=0)

        self.chat_frame = Frame(height=355, width=730)
        self.chat_frame.place(x=132, y=80)

        self.entry = Entry(self.chat_window, width=54, font=('Poppins Regular', 15), foreground='black', relief=FLAT, border=0)
        self.entry.place(x=145, y=465)
        self.send = Button(self.chat_window, width=5, height=1, text='>', font=('Poppins Regular', 14, 'bold'), background='gold', foreground='black', command=self.send_message)
        self.send.place(x=789, y=451)

        self.entry.insert(0, 'Message Talker...')
        self.entry.config(fg='seashell4')
        self.entry.bind('<FocusIn>', self.on_enter)

        self.chat_window.mainloop()

    def on_enter(self, e):
        self.entry.delete(0, 'end')
        self.entry.config(fg='black')

    def send_message(self):

        yi = 10

        genai.configure(api_key="AIzaSyCpwngYdzfcQAFwL3j9gkD11tjUYeeWkUA")
        model = genai.GenerativeModel('gemini-1.5-flash', generation_config=genai.GenerationConfig(temperature=0.9))

        self.prompt = self.entry.get()
        self.prompt_label = Label(self.chat_frame, text=self.prompt, height=1, width=58, font=('Poppins Regular', 15), foreground='black', background='light blue', anchor='e')
        self.prompt_label.place(x=15, y=yi)

        chat = model.start_chat(history=[])
        self.response = chat.send_message(self.prompt)
        self.response_label = Label(self.chat_frame, text=self.response.text, height=2, width=58, font=('Poppins Regular', 15), foreground='black', background='white', anchor='w')
        self.response_label.place(x=15, y=yi+50)

        yi += 10

class StudyChat(TalkerChat):
    def __init__(self):
        super().__init__()
        self.place_image('studies-chat.jpg')

class ResearchChat(TalkerChat):
    def __init__(self):
        super().__init__()
        self.place_image('research-chat.jpg')


class BusinessChat(TalkerChat):
    def __init__(self):
        super().__init__()
        self.place_image('business-chat.jpg')

class GeneralChat(TalkerChat):
    def __init__(self):
        super().__init__()
        self.place_image('general-chat.jpg')

