from tkinter import *
from tkinter import messagebox
tk = Tk()
tk.title("Check percent")
L = Label(tk, text="Finished")
L.grid(row=0, column=0)
T = Text(tk, width=30, height=30)
T.grid(row=1, column=0)
L1 = Label(tk, text="Unfinished")
L1.grid(row=2, column=0)
T1 = Text(tk, width=30, height=30)
T1.grid(row=3, column=0)


def main():
	finished = len(T.get("0.0", "end").replace("\n", "").replace(" ", ""))
	unfinished = len(T1.get("0.0", "end").replace("\n", "").replace(" ", ""))
	percent = str(finished / (unfinished + finished) * 100) + "%"
	messagebox.showwarning("Result", percent)
	

B = Button(tk, text="Check", command=main)
B.grid(row=4, column=0)
tk.mainloop()
