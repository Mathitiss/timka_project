from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        bg_style = ttk.Style()
        bg_style.configure('bg.TFrame', background='#2B4F26')

        self.mainframe = MainFrame(ttk.Frame(root, style='bg.TFrame'))
        self.enterframe = EnterFrame(ttk.Frame(root, style='bg.TFrame'))   

        self.mainframe.frame.pack(fill='both', expand=True)


class MainFrame:
    def __init__(self, frame):
        self.frame = frame
        self.exist = True
        self.GUI()
        
    def GUI(self):
        image = Image.open("deer_logo.png") 
        resized_image = image.resize((450, 400))
        img = ImageTk.PhotoImage(resized_image)

        logo = ttk.Label(self.frame, image=img) # background='#2B4F26' !!!
        logo.pack()
        
        text1 = ttk.Label(self.frame, text="DeerView", font=("Courier New", 26, "bold"), background='#2B4F26', foreground='white')
        text1.pack()

        btn_style = ttk.Style()
        btn_style.configure('btn.TButton', width=15, height=1, font=("Courier New", 26, "bold"))

        button = ttk.Button(self.frame, text="НАЧАТЬ", command=self.go_back, style='btn.TButton')
        button.pack(pady=100)

        text2 = ttk.Label(self.frame, text="version alpha 1.0", font=("Courier New", 10), background='#2B4F26', foreground='white')
        text2.pack(side=BOTTOM)

    def go_back(self):
        self.frame.pack_forget()
        app.enterframe.frame.pack(fill='both', expand=True)
        if not app.enterframe.exist:
            app.enterframe.GUI()
        app.enterframe.exist = True


class EnterFrame:
    def __init__(self, frame):
        self.frame = frame
        self.frame.pack(fill='both', expand=True)
        self.exist = False
        
    def GUI(self):       
        text = ttk.Label(self.frame, text="EnterFrame", font=("Courier New", 26, "bold"))
        text.pack()

        button = ttk.Button(self.frame, text="BACK", command=self.go_back)
        button.pack(pady=100)

    def go_back(self):
        self.frame.pack_forget()
        app.mainframe.frame.pack(fill='both', expand=True)
        if not app.mainframe.exist:
            app.mainframe.GUI()
        app.mainframe.exist = True


root = Tk()
root.title("DeerView")
root.geometry("1440x860")

app = App(root)
root.mainloop()