from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Dhruv\'s Clock')


def time():
    string = strftime('%I:%M:%S %p')
    # To make the clock format 24 hrs. Simply change the strftime('%I:%M:%S %p') to strftime('%H:%M:%S %p').
    lbl.config(text=string)
    lbl.after(1000, time)  # It will update the time after every (1000 milliseconds i.e. after 1 second)


lbl = Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')

lbl.pack(anchor='center')
time()

mainloop()
