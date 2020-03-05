import datetime
import time
import os
import tkinter.messagebox
def call():
    for x in range(3):
        os.system("say Siri喊你来上课了")
        tkinter.messagebox.showwarning("Alarm","Siri喊你来上课了！")
while True:
    now = datetime.datetime.now()
    if now.hour == 8:
        if now.minute == 0:
            call()
    if now.hour == 9:
        if now.minute == 0:
            call()
    if now.hour == 10:
        if now.minute == 0:
            call()
    if now.hour == 11:
        if now.minute == 0:
            call()
    if now.hour == 13:
        if now.minute == 0:
            call()
    if now.hour == 14:
        if now.minute == 0:
            call()
    time.sleep(5)

