from tkinter import Tk, Entry, Label, Button
print("欢迎使用中秋祝福生成器")
tk = Tk()
tk.title = ("中秋祝福生成器")
E = Entry(tk)
E.grid(row=0, column=0)
L = Label(tk, text="输入老师名称")
L.grid(row=0, column=1)
def main():
    if "," in E.get():
        names = E.get().split(",")
    if "，" in E.get():
        names = E.get().split("，")
    for each in names:
        print("谢谢您，我尊敬的%s老师！祝您中秋佳节快乐！" % each)
B = Button(tk, text="Start" ,command=main)
B.grid(row=1, column=0)
tk.mainloop()
