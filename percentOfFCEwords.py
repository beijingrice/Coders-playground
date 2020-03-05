from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("How many word had you inputted.")
E = Entry(tk)
E.grid(row=0, column=0)
L = Label(tk, text="Now's pages")
L.grid(row=0, column=1)


def main():
    try:
        nowPage = int(E.get())
    except ValueError:
        tkinter.messagebox.showerror("Error","Your input is not an 'String' that can be changed to 'Int'")
        return
    tkinter.messagebox.showwarning("Now","Now you had finished %s of FCE words!" % (str(nowPage / 232 * 100) + "%"))


B = Button(tk, text="Check", command=main)
B.grid(row=1,column=0)
tk.mainloop()
