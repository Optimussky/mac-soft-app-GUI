#mac-soft.py
#calendar
from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import filedialog
import platform
import psutil

#brightness
import screen_brightness_control as pct

#audio
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#weather
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

#clock
from time import strftime

#calendar
from tkcalendar import *

#open google
import pyautogui

import subprocess
import webbrowser as wb
import random

root=Tk()
root.title('mac-soft Tool')
root.geometry("850x500+300+170")
root.resizable(False,False)
root.configure(bg='#292e3e')

#icon
image_icon=PhotoImage(file="Image/icon.png")
root.iconphoto(False,image_icon)


Body=Frame(root,width=900,height=600,bg="#d6d6d6")
Body.pack(pady=20,padx=20)

#-------------------------------
LHS = Frame(Body,width=310, height=435,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
LHS.place(x=10,y=10)

#logo
photo=PhotoImage(file="Image/laptop.png")
myimage=Label(LHS,image=photo,background="#f4f5f5")
myimage.place(x=2,y=20)

my_system = platform.uname()
l1=Label(LHS, text=my_system.node,bg="#f4f5f5",font=("Acumin Variable Concept",15,'bold'),justify="center")
l1.place(x=2,y=200)

l2=Label(LHS, text=f"System: {my_system.system}",bg="#f4f5f5",font=("Acumin Variable Concept",8),justify="center")
l2.place(x=20,y=225)

l3=Label(LHS, text=f"Version: {my_system.version}",bg="#f4f5f5",font=("Acumin Variable Concept",15),justify="center")
l3.place(x=20,y=250)

l4=Label(LHS, text=f"Machine: {my_system.machine}",bg="#f4f5f5",font=("Acumin Variable Concept",15),justify="center")
l4.place(x=20,y=285)

l5=Label(LHS, text=f"Total RAM Installed: {round(psutil.virtual_memory().total/1000000000,2)} GB",bg="#f4f5f5",font=("Acumin Variable Concept",15),justify="center")
l5.place(x=20,y=310)

l6=Label(LHS, text=f"Processor: {my_system.processor}",bg="#f4f5f5",font=("Acumin Variable Concept",7),justify="center")
l6.place(x=20,y=340)



#-------------------------------
RHS = Frame(Body,width=470, height=230,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
RHS.place(x=330,y=10)


system = Label(RHS, text='System', font=("Acumin Variable Concept",15),bg="#f4f5f5")
system.place(x=10, y=10)

##################################  Battery ##########################################


def converTime(seconds):
	minutes,seconds=divmod(seconds,60)
	hours,minutes=divmod(minutes,60)
	return "%d:%02d:%02d"% (hours,minutes,seconds)


def none():
	global battery_png
	global battery_label
	battery = psutil.sensors_battery()
	percent=battery.percent
	time=converTime(battery.secsleft)

	print(percent)
	#print(time)
	lbl.config(text=f"{str(percent)}%")
	lbl_plug.config(text=f"Plug in: {str(battery.power_plugged)}")#plug in Conectado
	lbl_time.config(text=f'{time} remaining')


	battery_label=Label(RHS,background="#f4f5f5")
	battery_label.place(x=15,y=50)

	lbl.after(1000,none)

	if battery.power_plugged==True:
		battery_png=PhotoImage(file="Image/charging.png")
		battery_label.config(image=battery_png)
	else:
		battery_png=PhotoImage(file='Image/battery.png')
		battery_label.config(image=battery_png)



lbl=Label(RHS,font=("Acumin Variable Concept",40,'bold'),bg="#f4f5f5")
lbl.place(x=200,y=400)

lbl_plug=Label(RHS,font=("Acumin Variable Concept",10),bg="#f4f5f5")
lbl_plug.place(x=20,y=100)

lbl_time=Label(RHS,font=("Acumin Variable Concept",15),bg="#f4f5f5")
lbl_time.place(x=200,y=100)


none()





#-------------------------------
RHB = Frame(Body,width=470, height=190,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
RHB.place(x=330,y=255)






root.mainloop()