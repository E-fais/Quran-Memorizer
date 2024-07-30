import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image,ImageTk
import tkinter as tk

root=ttk.Window(themename='cosmo')
root.title('Hifdh App')
root.iconbitmap('./assets/logo.ico')

background_img=ImageTk.PhotoImage(Image.open('./assets/background.jpg'))
#create a canvas
canvas=tk.Canvas(root,width=background_img.width(),height=background_img.height())
canvas.pack(fill='both', expand=True)
canvas.create_image(0, 0, image=background_img, anchor='nw')

#create labels
title = ttk.Label(root, text="Quran Memorizer", font=("helvetica", 14),bootstyle='primary',relief="sunken",padding=(35,4))
start_button = ttk.Button(root, text="Start Review",)
add_surah_button = ttk.Button(root, text="Add New Surah",)
calligraphy=ImageTk.PhotoImage(Image.open('./assets/calligraphy.png'))

# Place the labels on the canvas
canvas.create_window(145, 40, window=title)
canvas.create_window(320, 150, window=start_button)
canvas.create_window(320, 200, window=add_surah_button)
canvas.create_image(270, 0, image=calligraphy, anchor='nw')





root.mainloop()