import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image,ImageTk
import tkinter as tk
import pandas as pd
import random
from tkinter import messagebox
import os

root=ttk.Window(themename='cosmo')
root.title('Quran Memorizer')
root.iconbitmap('./assets/logo.ico')
background_img=ImageTk.PhotoImage(Image.open('./assets/background.jpg'))

surah_list=[]
completed_list=[]



def review_completed(completed_surah):
    open('pending.txt','w').close()
    if os.path.exists('completed_surah.csv') and os.path.getsize('completed_surah.csv') > 0:
        completed_list = pd.read_csv('completed_surah.csv', header=None)
    else:
        completed_list = pd.DataFrame()

    s_series = pd.DataFrame([completed_surah])
    completed_list = pd.concat([completed_list, s_series], ignore_index=True)
    completed_list.to_csv('completed_surah.csv', index=False, header=None)
    messagebox.showinfo('Completed', 'Surah Saved, Congratulations!!')

def try_later(surah):
    with open('pending.txt','w') as pending:
       pending.write(surah)
    messagebox.showinfo('Later','Surah Saved For Later')



def start_review():
    pending=''
    file_path='pending.txt'
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
       with open(file_path,'r') as file:
            random_surah=f"{file.read().strip()}"
       pending=" (Pending)"
    else:
      if not os.path.exists('surah_list.csv') or os.path.getsize('surah_list.csv') == 0:
         messagebox.showinfo('No Surah', 'The surah list is empty or not found. Please add surahs first.')
         return
      surah_df=pd.read_csv('surah_list.csv',header=None)
      try:
        completed_df=pd.read_csv('completed_surah.csv',header=None)
        if len(surah_df)==len(completed_df):
           yes_no=messagebox.askyesno('Complete','You have completed all surah.\n Clear all and start again?')
           if yes_no:
            open('completed_surah.csv','w').close()
           return
        random_number=random.randint(0,len(surah_df)-1)
        random_surah=surah_df.iloc[random_number].item()

        if len(surah_df)>len(completed_df):
         while random_surah in completed_df.values:
           random_number=random.randint(0,len(surah_df)-1)
           random_surah=surah_df.iloc[random_number].item()

      except:
        random_number=random.randint(0,len(surah_df)-1)
        random_surah=surah_df.iloc[random_number].item()
    review_window=ttk.Toplevel(root)
    review_window.geometry('400x200')
    review_window.iconbitmap('./assets/logo.ico')
    review_window.title('Hifdh Review')

    surah_name_label=ttk.Label(review_window,text=f"Surah For Review: {random_surah}{pending}",
                               font=('helvetica',13),bootstyle='primary',padding=(10,10))
    surah_name_label.pack(pady=10)

    completed_btn=ttk.Button(review_window,text=f'MARK " {random_surah.upper()} " AS REVIEW COMPLETED',
                             bootstyle='outline-success',command=lambda:[review_completed(random_surah),review_window.destroy()])
    completed_btn.pack()

    failed_btn=ttk.Button(review_window,text='TRY AGAIN LATER',bootstyle='outline-danger',width=36,
                          command=lambda:[try_later(random_surah),review_window.destroy()])
    failed_btn.pack(pady=20)

def save_surah(val):
    surah_list.append(val)
    df=pd.DataFrame(surah_list)
    df.to_csv("surah_list.csv",index=False,header=False,mode='a',)
    messagebox.showinfo('Success','Surah Saved')

def add_new_surah():
    add_surah_window=ttk.Toplevel(root)
    add_surah_label=ttk.Label(add_surah_window,text='Enter New Surah Name')
    add_surah_label.pack(padx=50,pady=5)
    surah_entry=ttk.Entry(add_surah_window)
    surah_entry.pack(padx=50,pady=10)
    surah_save_btn=ttk.Button(add_surah_window,text='Save Surah',command=lambda:[save_surah(surah_entry.get()),add_surah_window.destroy()])
    surah_save_btn.pack(padx=50,pady=10)
    
#create a canvas
canvas=tk.Canvas(root,width=background_img.width(),height=background_img.height())
canvas.pack(fill='both', expand=True)
canvas.create_image(0, 0, image=background_img, anchor='nw')

#create labels
title = ttk.Label(root, text="Quran Memorizer", font=("helvetica", 14),bootstyle='primary',relief="sunken",padding=(35,4))
start_button = ttk.Button(root, text="Start Review",command=start_review)
add_surah_button = ttk.Button(root, text="Add New Surah",command=add_new_surah)
calligraphy=ImageTk.PhotoImage(Image.open('./assets/calligraphy.png'))

# Place the labels on the canvas
canvas.create_window(145, 40, window=title)
canvas.create_window(320, 150, window=start_button)
canvas.create_window(320, 200, window=add_surah_button)
canvas.create_image(270, 0, image=calligraphy, anchor='nw')

start_review()
root.mainloop()