import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image,ImageTk
import tkinter as tk
import pandas as pd


root=ttk.Window(themename='cosmo')
root.title('Quran Memorizer')
root.iconbitmap('./assets/logo.ico')
background_img=ImageTk.PhotoImage(Image.open('./assets/background.jpg'))

surah_list=[]
def save_surah(val):
    global surah_entry
    surah_list.append(val)
    df=pd.DataFrame(surah_list)
    df.to_csv("surah_list.csv",index=False,header=False,mode='a')
    

def add_new_surah():
    add_surah_window=ttk.Toplevel(root)
    add_surah_label=ttk.Label(add_surah_window,text='Enter New Surah Name')
    add_surah_label.pack(padx=50,pady=5)
    surah_entry=ttk.Entry(add_surah_window)
    surah_entry.pack(padx=50,pady=10)
    surah_save_btn=ttk.Button(add_surah_window,text='Save Surah',command=lambda:save_surah(surah_entry.get()))
    surah_save_btn.pack(padx=50,pady=10)
    
#create a canvas
canvas=tk.Canvas(root,width=background_img.width(),height=background_img.height())
canvas.pack(fill='both', expand=True)
canvas.create_image(0, 0, image=background_img, anchor='nw')

#create labels
title = ttk.Label(root, text="Quran Memorizer", font=("helvetica", 14),bootstyle='primary',relief="sunken",padding=(35,4))
start_button = ttk.Button(root, text="Start Review",)
add_surah_button = ttk.Button(root, text="Add New Surah",command=add_new_surah)
calligraphy=ImageTk.PhotoImage(Image.open('./assets/calligraphy.png'))

# Place the labels on the canvas
canvas.create_window(145, 40, window=title)
canvas.create_window(320, 150, window=start_button)
canvas.create_window(320, 200, window=add_surah_button)
canvas.create_image(270, 0, image=calligraphy, anchor='nw')


root.mainloop()