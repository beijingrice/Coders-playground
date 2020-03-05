import requests
import time
import tkinter.messagebox
url = "http://www.bj25schooledu.com.cn"
while True:
    body = requests.get(url)
    if body.status_code != 403:
        for x in range(3):
            print("WIN!")
            tkinter.messagebox.showwarning("Good news!","School website online!")
        break
    time.sleep(5)
            
