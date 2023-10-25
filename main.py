from tkinter import *
import tkinter as tk
from tkinter import ttk, font

# defs
def clear(object):
   slaves = object.grid_slaves()
   for x in slaves:
      x.destroy()
def firstpage():
   clear(mframe)
   win.title('Доска с тасками')

   lbl2 = Label(mframe, bg='#ADD8E6', height=300, width=150)
   lbl2.pack()
   lbl3 = Label(mframe, bg='#ADD8E6', height=300, width=150)
   lbl3.pack()
   lbl4 = Label(mframe, bg='#ADD8E6', height=300, width=150)
   lbl4.pack()

def secondpage():
   clear(mframe)
   win.title('Аккаунт')

   login = Entry(mframe, width=150).pack(padx=100)
   password = Entry(mframe, width=150).pack(padx=100)



# window
win = Tk()
win.title('Таск-менеджер')
win.geometry('600x400+150+100')
win.resizable(False, False)
ttk.Style().theme_use('clam')
pic2 = PhotoImage(file='logo.png')
win.iconphoto(False, pic2)

# font
font1 = font.Font(family='codicon.ttf', size=12)
ttk.Style().configure('my.TButton', font=font1, background='#4169E1', foreground='white')

# images
pic1 = PhotoImage(file='cifra1.png')
tick1 = PhotoImage(file='tick1.png')
tick2 = PhotoImage(file='tick2.png')
tick3 = PhotoImage(file='tick3.png')

# notebook
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
frame1 = ttk.Frame(notebook)
frame1.pack(fill=BOTH, expand=True)
notebook.add(frame1, text="Task manager", image=pic2, compound=LEFT)

# option frame
oframe = Frame(win, bg='#4169E1')

lbl1 = Label(oframe, image=pic1).pack()

btn1 = ttk.Button(oframe, text='Таски', style='my.TButton', width=100, command=firstpage).pack()
btn3 = ttk.Button(oframe, text='Аккаунт', style='my.TButton', width=100, command=secondpage).pack()

oframe.pack(side=tk.LEFT)
oframe.pack_propagate(False)
oframe.config(width=100, height=400)

# main frame
mframe = Frame(win, bg='white')

mframe.pack(side=tk.RIGHT)
mframe.pack_propagate(False)
mframe.config(width=500, height=400)


win.mainloop()
