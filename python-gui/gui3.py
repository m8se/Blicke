#!/usr/bin/env python

import matplotlib
matplotlib.use('TkAgg')

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler


from matplotlib.figure import Figure

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

root = Tk.Tk()
root.wm_title("Embedding in TK")


f = Figure(figsize=(5,4), dpi=100)
a = f.add_subplot(111)
t = arange(0.0,3.0,0.01)
s = sin(2*pi*t)

a.plot(t,s)




def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

f1=Tk.Frame(root)
f1.pack(side=Tk.LEFT)
Tk.Button(f1,text="Hello").pack()

f2=Tk.Frame(root)
f2.pack(side=Tk.LEFT,fill=Tk.BOTH,expand=1)


canvas = FigureCanvasTkAgg(f, master=f2)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


f3=Tk.Frame(f2)
f3.pack()

button = Tk.Button(f3, text='Quit', command=_quit)
button.pack(side=Tk.LEFT)
label=Tk.Label(f3,text="Check this out!")
label.pack(side=Tk.LEFT)

# a tk.DrawingArea



Tk.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.
