from calendar import calendar
from cgitb import text
from email import message
from email.mime import image
from tkinter import *
import datetime
import time
import os
from tkinter.font import BOLD
import pyautogui

play = False
play1 = 0


username = os.getlogin()

root = Tk()

root.overrideredirect(1)
root.geometry("400x500+1500+10")
root.config(bg='grey')
root.wm_attributes('-transparentcolor', 'grey')

nextIcon = PhotoImage(file = r"./content/next.png")
prevIcon = PhotoImage(file = r"./content/back.png")
playpauseIcon = PhotoImage(file = r"./content/play-button.png")
calendarIcon = PhotoImage(file = r"./content/calendar.png")
clockIcon = PhotoImage(file = r"./content/clock.png")


playpauseIcon = playpauseIcon.subsample(15, 15)
nextIcon = nextIcon.subsample(15, 15)
prevIcon = prevIcon.subsample(15, 15)
clockIcon = clockIcon.subsample(15, 15)
calendarIcon = calendarIcon.subsample(15, 15)


def update():
    root.after(1000, update)
    time['text'] = datetime.datetime.now().strftime("%H:%M:%S")
    date['text'] = datetime.datetime.now().strftime("%d %b %Y")
    if int(datetime.datetime.now().strftime("%H")) >= 5:
        welcome_message['text'] = f"Good morning, {username}!"
    if int(datetime.datetime.now().strftime("%H")) >= 12:
        welcome_message['text'] = f"Have a nice day, {username}!"
    if int(datetime.datetime.now().strftime("%H")) >= 19:
        welcome_message['text'] = f"Good evening, {username}!"
    if int(datetime.datetime.now().strftime("%H")) >= 22:
        welcome_message['text'] = f"Good night, {username}!"

def nexttrack():
    pyautogui.press('nexttrack')
def prevtrack():
    pyautogui.press('prevtrack')
def playpause():
    pyautogui.press('playpause')
    play1 += 1
    if play1%2 != 0:
        playpauseIcon = PhotoImage(file = r"./content/play-button.png")
    else:
        playpauseIcon = PhotoImage(file = r"./content/pause.png")



welcome_message = Label(root, fg="white", bg="grey")
clockIco = Label(root, image=clockIcon, bg="grey")
time = Label(root, fg="white", bg="grey")
calendarIco = Label(root, image=calendarIcon, bg="grey")
date = Label(root, fg="white", bg="grey")

previous_track = Button(root,command=prevtrack, image = prevIcon, bg="grey", borderwidth=0)
play_pause = Button(root,command=playpause, image = playpauseIcon, bg="grey", borderwidth=0)
next_track = Button(root, command=nexttrack, image = nextIcon, bg="grey", borderwidth=0)

unisans_thin = ("Uni Sans Thin", 15)
unisans_Heavy = ("Uni Sans heavy", 20)

welcome_message.config(font=unisans_Heavy)
time.config(font=unisans_thin)
date.config(font=unisans_thin)
next_track.config(height=50, width=50)
play_pause.config(height=50, width=50)
previous_track.config(height=50, width=50)



next_track.place(x=225, y=125)
play_pause.place(x=175, y=125)
previous_track.place(x=125, y=125)
welcome_message.place(x=75, y=5)
calendarIco.place(x=82, y=40)
date.place(x=125, y=45)
clockIco.place(x=82, y=85)
time.place(x=125, y=90)
update()

root.mainloop()