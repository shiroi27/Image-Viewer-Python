from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
import os

def showimage():
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select Image File",
        filetypes=(
            ("JPG File", "*.jpg"),
            ("PNG File", "*.png"),
            ("All Files", "*.*")
        )
    )
    if filename:
        img = Image.open(filename)
        img_width, img_height = img.size
        root.geometry(f"{img_width}x{img_height + 100}")  # Resize window based on image size

    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image=img


root= Tk()

frame = Frame(root)
frame.pack(side=BOTTOM,padx=15,pady=15)

lbl = Label(root)
lbl.pack()

btn1 = Button(frame,text="SELECT IMAGE",command=showimage)
btn1.pack(side =tk.LEFT)

btn2 = Button(frame,text="EXIT" , command=lambda:exit())
btn2.pack(side = tk.LEFT,padx=12)

root.title("IMAGE VIEWER")
root.geometry("450x400+200+100")

root.mainloop()