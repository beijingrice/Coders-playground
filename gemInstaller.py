from tkinter import *
import os
tk = Tk()
tk.title("Gem installer")
E = Entry(tk)
E.grid(row=0, column=0)
L = Label(tk, text="Package name")
L.grid(row=0, column=1)
def main():
	os.system("sudo gem install %s" % E.get())
B = Button(tk, text="Install", command=main)
B.grid(row=1, column=0)
tk.mainloop()