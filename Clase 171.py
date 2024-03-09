# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 08:29:32 2024

@author: anyta
"""

from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time


root = Tk()
root.geometry("600x450")
clock_image = ImageTk.PhotoImage(Image.open("Reloj de Godzilla.jpg"))
clock_image2 = ImageTk.PhotoImage(Image.open("Reloj Fino.jpg"))
clock_image3 = ImageTk.PhotoImage(Image.open("Pared minus one.jpg"))
clock_image4 = ImageTk.PhotoImage(Image.open("Reloj japon.jpg"))


Hora_india = Label(root, text="India")
Hora_india.place(relx=0.2, rely=0.05, anchor=CENTER)

Reloj_India = Label(root)
Reloj_India["image"] = clock_image
Reloj_India.place(relx=0.2, rely=0.35, anchor=CENTER)

Time_India = Label(root)
Time_India.place(relx=0.2, rely=0.65, anchor=CENTER)

Hora_USA = Label(root, text="USA")
Hora_USA.place(relx=0.5, rely=0.05, anchor=CENTER)

Reloj_USA = Label(root)
Reloj_USA["image"] = clock_image2
Reloj_USA.place(relx=0.5, rely=0.35, anchor=CENTER)

USA_time = Label(root)
USA_time.place(relx=0.5, rely=0.65, anchor=CENTER)

Hora_Australia = Label(root, text="Australia")
Hora_Australia.place(relx=0.7, rely=0.05, anchor=CENTER)

Reloj_Australia = Label(root)
Reloj_Australia["image"] = clock_image3
Reloj_Australia.place(relx=0.7, rely=0.35, anchor=CENTER)

Australia_time = Label(root)
Australia_time.place(relx=0.9, rely=0.65, anchor=CENTER)

Hora_japon = Label(root, text="Japon")
Hora_japon.place(relx=0.9, rely=0.05, anchor=CENTER)

Reloj_japon = Label(root)
Reloj_japon["image"] = clock_image4
Reloj_japon.place(relx=0.9, rely=0.35, anchor=CENTER)

Japon_time = Label(root)
Japon_time.place(relx=0.9, rely=0.65, anchor=CENTER)

class India():
    def times(self):
        home = pytz.timezone("Asia/Kolkata")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        Time_India["text"] = "Time: " + current_time
        Time_India.after(200, self.times)
        
class USA():
    def times(self):
        home = pytz.timezone("US/Central")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        USA_time["text"] = "Time: " + current_time
        USA_time.after(200, self.times)
        
class Australia():
    def times(self):
        home = pytz.timezone("Australia/Sydney")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        Australia_time["text"] = "Time: " + current_time
        Australia_time.after(200, self.times)
        
class Japon():
    def times(self):
        home = pytz.timezone("Japon/Tokio")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        Japon_time["text"] = "Time: " + current_time
        Japon_time.after(200, self.times)
        
obj_india = India()
obj_USA = USA()
obj_Australia = Australia()
obj_Japon = Japon()

india_btn = Button(root, text="Show time", command=obj_india.times)
india_btn.place(relx=0.2, rely=0.8, anchor=CENTER)

USA_btn = Button(root, text="Show time", command=obj_USA.times)
USA_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

Australia_btn = Button(root, text="Show time", command=obj_Australia.times)
Australia_btn.place(relx=0.7, rely=0.8, anchor=CENTER)

Japon_btn = Button(root, text="Show time", command=obj_Japon.times)
Japon_btn.place(relx=0.9, rely=0.8, anchor=CENTER)

root.mainloop()