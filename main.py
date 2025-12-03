import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# ОСНОВА
root = tk.Tk()

root.title("DeerView")
root.geometry("1440x860")
root.configure(bg='#2B4F26')

# ЛОГО
image = Image.open("deer_logo.png") 
resized_image = image.resize((450, 400))
img = ImageTk.PhotoImage(resized_image)

logo = Label(image=img, borderwidth=0, highlightthickness=0)
logo.image = img
logo.pack()

# ТЕКСТ
text1 = tk.Label(root, text="DeerView", font=("Courier New", 26, "bold"), bg='#2B4F26', fg='white')
text1.pack()

# КНОПКА СТАРТ
button = tk.Button(root, text="НАЧАТЬ", command=None, width=15, height=1, font=("Courier New", 26, "bold"))
button.pack(pady=100)

# ТЕКСТ ВЕРСИЯ
text2 = tk.Label(root, text="version alpha 1.0", font=("Courier New", 10), bg='#2B4F26', fg='white')
text2.pack(side=tk.BOTTOM)

# ЗАПУСК
root.mainloop()