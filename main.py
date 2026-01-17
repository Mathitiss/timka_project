from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

import sqlite3py


class App:
    def __init__(self, root):
        self.bg_style = ttk.Style()
        self.bg_style.configure('bg.TFrame', background='#2B4F26')

        self.btn_style = ttk.Style()
        self.btn_style.configure('btn.TButton', width=15, height=1, font=("Courier New", 26, "bold"))

        self.mainframe = MainFrame(ttk.Frame(root, style='bg.TFrame'))
        self.enterframe = EnterFrame(ttk.Frame(root, style='bg.TFrame'))
        self.workframe = Workspace(ttk.Frame(root, style='bg.TFrame'))

        self.mainframe.frame.pack(fill='both', expand=True)


class MainFrame:
    def __init__(self, frame):
        self.frame = frame
        self.GUI()

    def GUI(self):
        image = Image.open("deer_logo.png") 
        resized_image = image.resize((450, 400))
        img = ImageTk.PhotoImage(resized_image)

        logo = ttk.Label(self.frame, image=img) # background='#2B4F26' !!!
        logo.pack()

        text1 = ttk.Label(self.frame, text="DeerView", font=("Courier New", 26, "bold"), background='#2B4F26', foreground='white')
        text1.pack()

        button = ttk.Button(self.frame, text="START", command=self.func_start, style='btn.TButton')
        button.pack(pady=100)

        text2 = ttk.Label(self.frame, text="version alpha 1.0", font=("Courier New", 10), background='#2B4F26', foreground='white')
        text2.pack(side=BOTTOM)

    def func_start(self):
        self.frame.pack_forget()
        app.enterframe.frame.pack(fill='both', expand=True)
        app.enterframe.GUI()


class EnterFrame:
    def __init__(self, frame):
        self.frame = frame
        self.login_error = 0
        self.pass_error = 0

    def GUI(self):
        login_var = StringVar()
        pass_var = StringVar()

        self.login_entry = ttk.Entry(self.frame, font=("Courier New", 26, "bold"), textvariable = login_var)
        self.login_entry.pack(pady=10)

        self.password_entry = ttk.Entry(self.frame, show ="*", font=("Courier New", 26, "bold"), textvariable = pass_var)
        self.password_entry.pack()

        button = ttk.Button(self.frame, text="ENTER", command=self.func_enter, style='btn.TButton')
        button.pack(pady=30)

    def func_enter(self):
        login = self.login_entry.get()
        password = self.password_entry.get()

        database = sqlite3py.database
        
        if login in database:
            if database[login] == password:
                self.login_error = 0
                self.pass_error = 0

                self.frame.pack_forget()
                app.workframe.frame.pack(fill='both', expand=True)
                app.workframe.GUI()
            else:
                self.login_error += 1
                messagebox.showerror("Password error!", "Wrong password")
                if self.pass_error > 3:
                    messagebox.showwarning("A lot of wrong attempts", "If you are having trouble logging in." \
                "Contact your higher management.") 
        else:
            self.login_error += 1
            messagebox.showerror("Login error!", "Login not found")
            if self.login_error > 3:
                messagebox.showwarning("Множество неверных попыток", "If you are having trouble logging in." \
                "Contact your higher management.") 


class Workspace:
    def __init__(self, frame):
        self.frame = frame

    def GUI(self):
        pass


root = Tk()
root.title("DeerView")
root.geometry("1440x860")

app = App(root)
root.mainloop()