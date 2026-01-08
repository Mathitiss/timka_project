from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Main:
    def __init__(self, r):
        bg_style = ttk.Style()
        bg_style.configure('bg.TFrame', background='#2B4F26')

        self.mainframe = ttk.Frame(r, style='bg.TFrame')
        self.mainframe.pack(fill='both', expand=True)

        # self.page1.tkraise()
        self.GUI()
        
    def GUI(self):
        image = Image.open("deer_logo.png") 
        resized_image = image.resize((450, 400))
        img = ImageTk.PhotoImage(resized_image)

        logo = ttk.Label(self.mainframe, image=img, background='#2B4F26')
        logo.image = img
        logo.pack()
        
        text1 = ttk.Label(self.mainframe, text="DeerView", font=("Courier New", 26, "bold"), background='#2B4F26', foreground='white')
        text1.pack()

        btn_style = ttk.Style()
        btn_style.configure('btn.TButton', width=15, height=1, font=("Courier New", 26, "bold"))

        button = ttk.Button(self.mainframe, text="НАЧАТЬ", command=self.show_page2, style='btn.TButton')
        button.pack(pady=100)

        text2 = ttk.Label(self.mainframe, text="version alpha 1.0", font=("Courier New", 10), background='#2B4F26', foreground='white')
        text2.pack(side=BOTTOM)

    def show_page2(self):
        pass
        # tkraise()

# class Enter():
#     def __init__(self): 
#         self.GUI()
        
#     def GUI(self):
#         pass


root = Tk()
root.title("DeerView")
root.geometry("1440x860")

App = Main(root)
root.mainloop()