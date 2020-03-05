from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import sys
title = "Decode & Encode"
tk = Tk()
tk.title(title)
L = Label(tk, text="Input text to cope with it.")
L.grid(row=0, column=0)
T = Text(tk, width=30, height=30)
T.grid(row=1, column=0)
E = Entry(tk)
E.grid(row=2, column=0)
L1 = Label(tk, text="Move count")
L1.grid(row=2, column=1)
L2 = Label(tk, text="Coped Text")
L2.grid(row=3, column=0)
T1 = Text(tk, width=30, height=30)
T1.grid(row=4, column=0)
li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
      'x', 'y', 'z']


def file_not_found():
    tkinter.messagebox.showerror(title, "File Not Found!")


def permission_error():
    tkinter.messagebox.showerror(title, "Permission Error!")


def read_load_file():
    filename = tkinter.filedialog.askopenfilename(title="Open a file", filetypes=[("Text File", "*.txt"), ("Other files", "*.*")])
    try:
        with open(filename, "r") as obj:
            text = obj.read()
        T.insert(INSERT, text)
    except FileNotFoundError:
        file_not_found()
    except PermissionError:
        permission_error()


def save_as_file():
    filename = tkinter.filedialog.asksaveasfilename(title="Save a file", filetypes=[("Text File", "*.txt")])
    if ".txt" not in filename:
        filename = filename + ".txt"
    try:
        with open(filename, "w+") as obj:
            obj.write(T.get("0.0", "end"))
    except FileNotFoundError:
        file_not_found()
    except PermissionError:
        permission_error()


def encode():
    text = T.get("0.0", "end").lower()
    text_encoded = ""
    for each in text:
        if each in li:
            num = li.index(each) + int(E.get())
            if num > len(li) - 1:
                num = num - 26
            text_encoded = text_encoded + li[num]
    T1.delete("0.0", "end")
    T1.insert(INSERT, text_encoded)


def decode():
    text = T.get("0.0", "end").lower()
    text_decoded = ""
    for each in text:
        if each in li:
            num = li.index(each) - int(E.get())
            if num < 0:
                num = num + 26
            text_decoded = text_decoded + li[num]
    T1.delete("0.0", "end")
    T1.insert(INSERT, text_decoded)


def force_decode():
    text = T.get("0.0", "end").lower()
    text_decoded = ""
    for numm in range(1, 26):
        text_decoded = text_decoded + "%s: " % str(numm)
        for each in text:
            if each in li:
                num = li.index(each) - numm
                if num < 0:
                    num = num + 26
                text_decoded = text_decoded + li[num]
        text_decoded = text_decoded + "\n"
    T1.delete("0.0", "end")
    T1.insert(INSERT, text_decoded)


def _quit():
    cmd = tkinter.messagebox.askyesno(title, "Are you sure you want to quit?")
    if cmd:
        tk.destroy()
        sys.exit()


B = Button(tk, text="Encode", command=encode)
B.grid(row=5, column=0)
B1 = Button(tk, text="Decode", command=decode)
B1.grid(row=5, column=1)
B2 = Button(tk, text="Read File", command=read_load_file)
B2.grid(row=5, column=2)
B3 = Button(tk, text="Write File", command=save_as_file)
B3.grid(row=5, column=3)
B4 = Button(tk, text="Force Decode", command=force_decode)
B4.grid(row=5, column=4)
tk.mainloop()


