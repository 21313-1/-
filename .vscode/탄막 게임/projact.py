# import
import tkinter
from tkinter import ttk
 
# instance
window = tkinter.Tk()
 
# title
window.title("First Window")
 
# geomerty
window.geometry('300x100')
 
# preventing GUI from resizing
window.resizable(False, False)
 
def buttonClicked():
    label.configure(foreground='blue')
    labelNew.configure(text='안녕하세요! ' + name.get())
 
# Label
label = ttk.Label(window, text="이름을 입력하세요")
label.grid(column=0, row=0)
 
# Button
button = ttk.Button(window, text="클릭", command=buttonClicked)
button.grid(column=1, row=1)
 
# Text Box
name = tkinter.StringVar()
textbox = ttk.Entry(window, width=12, textvariable=name)
textbox.grid(column=0, row=1)
 
# Label
labelNew = ttk.Label(window, text="")
labelNew.grid(column=1, row=2)
 
# start GUI
window.mainloop()