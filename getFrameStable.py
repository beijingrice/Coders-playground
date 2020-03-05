import cv2 as cv
from tkinter import *
import tkinter.filedialog
import os
import time

ascii_char = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
char_len = len(ascii_char)

filename = tkinter.filedialog.askopenfilename(title="Open a video to play.")
cap = cv.VideoCapture(filename)
# smaller = 5
while True:
    hasFrame, frame = cap.read()
    if not hasFrame:
        break
    # width = frame.shape[0]
    # height = frame.shape[1]
    img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # img_resize = cv.resize(img_gray, (int(width / smaller), int(height / smaller)))
    img_resize = cv.resize(img_gray, (510, 119))

    text = ''
    for row in img_resize:
        for pixel in row:
            text += ascii_char[int(pixel / 256 * char_len)]
        text += '\n'
    if os.name == "nt":
        os.system("cls")
    if os.name == "posix":
        os.system("clear")
    print(text)
    #time.sleep(0.03)
