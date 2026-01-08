import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class Main(tk.Tk):
    def __init__(self): 
        super().__init__()

        mainframe = tk.Frame(self)
        mainframe.pack(fill='both', expand=True)

        self.page1 = Page1(mainframe, self)
        self.page1.pack(fill='both', expand=True)

        self.page2 = Page2(mainframe, self)
        self.page2.pack(fill='both', expand=True)

        self.page1.tkraise()


class Page1(tk.Frame):
    def __init__(self, parent, controller): 
        super().__init__(parent)
        self.controller = controller

        self.GUI()
        
    def GUI(self):
        self.controller.title("DeerView")
        self.controller.geometry("1440x860")
        self.controller.configure(bg='#2B4F26')

        image = Image.open("deer_logo.png") 
        resized_image = image.resize((450, 400))
        img = ImageTk.PhotoImage(resized_image)

        logo = tk.Label(self, image=img, borderwidth=0, highlightthickness=0)
        logo.image = img
        logo.pack()
        
        text1 = tk.Label(self, text="DeerView", font=("Courier New", 26, "bold"), bg='#2B4F26', fg='white')
        text1.pack()

        button = tk.Button(self, text="НАЧАТЬ", command=self.show_page2, width=15, height=1, font=("Courier New", 26, "bold"))
        button.pack(pady=100)

        text2 = tk.Label(self, text="version alpha 1.0", font=("Courier New", 10), bg='#2B4F26', fg='white')
        text2.pack(side=tk.BOTTOM)

    def show_page2(self):
        self.controller.page2.tkraise()


class Page2(tk.Frame):
    def __init__(self, parent, controller): 
        super().__init__(parent)
        self.GUI()

    def GUI(self):
        text1 = tk.Label(self, text="SECOND PAGE", font=("Courier New", 26, "bold"), bg='#2B4F26', fg='white')
        text1.pack()


app = Main()
app.mainloop()