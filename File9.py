from tkinter import*
from tkinter.colorchooser import askcolor

clr,clr1="White","Black"

def chgclr():
    result=askcolor(color="#b0ff62",title="Select Background Color")
    print(result)
    win.configure(background=result[1])

win=Tk()
win.title("Color Dialog")
win.wm_iconbitmap("icons/smiling.ico")
win.geometry("300x300+200+100")
win.configure(background=clr)

Button(text="choose Color",bg=clr1,fg=clr,command=chgclr).place(x=100,y=120)


win.mainloop()
