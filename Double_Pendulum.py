from Data_output import *
import numpy as np
from tkinter import *

root = Tk()
root.title('Double Pendulum')

t_th1 = Label(root, text='theta1 [rad]')
t_th2 = Label(root, text='theta2 [rad]')
t_om1 = Label(root, text='omega1 [rad]')
t_om2 = Label(root, text='omega2 [rad]')

e_th1 = Entry(root, width=15, borderwidth=5)
e_th1.insert(0,0)
e_th2 = Entry(root, width=15, borderwidth=5)
e_th2.insert(0,0)
e_om1 = Entry(root, width=15, borderwidth=5)
e_om1.insert(0,0)
e_om2 = Entry(root, width=15, borderwidth=5)
e_om2.insert(0,0)

t_l1 = Label(root, text='l1 [m]')
t_l2 = Label(root, text='l2 [m]')
t_m1 = Label(root, text='m1 [kg]')
t_m2 = Label(root, text='m2 [kg]')

e_l1 = Entry(root, width=15, borderwidth=5)
e_l1.insert(0,1)
e_l2 = Entry(root, width=15, borderwidth=5)
e_l2.insert(0,1)
e_m1 = Entry(root, width=15, borderwidth=5)
e_m1.insert(0,1)
e_m2 = Entry(root, width=15, borderwidth=5)
e_m2.insert(0,1)

t_t = Label(root, text='How many seconds?')
e_t = Entry(root, width=15, borderwidth=5)

def Go():
    l1 = float(e_l1.get())
    l2 = float(e_l2.get())
    m1 = float(e_m1.get())
    m2 = float(e_m2.get())
    h = 0.01
    t = float(e_t.get())
    const = (t, h, l1, l2, m1, m2)
    th1 = float(e_th1.get())
    th2 = float(e_th2.get())
    om1 = float(e_om1.get())
    om2 = float(e_om2.get())
    var = [th1, th2, om1, om2]
    output(const, var)
    root.quit()


b_plot = Button(root, text='Go!', command=Go, padx=50)

t_th1.grid(column=0, row=0)
t_th2.grid(column=0, row=1)
t_om1.grid(column=0, row=2)
t_om2.grid(column=0, row=3)

e_th1.grid(column=1, row=0)
e_th2.grid(column=1, row=1)
e_om1.grid(column=1, row=2)
e_om2.grid(column=1, row=3)

t_l1.grid(column=2, row=0)
t_l2.grid(column=2, row=1)
t_m1.grid(column=2, row=2)
t_m2.grid(column=2, row=3)

e_l1.grid(column=3, row=0)
e_l2.grid(column=3, row=1)
e_m1.grid(column=3, row=2)
e_m2.grid(column=3, row=3)

t_t.grid(column=0, row=4)
e_t.grid(column=1, row=4)

b_plot.grid(column=0, row=5, columnspan=4)

root.mainloop()

from plot import *
from animation import *

graph()
trajectory()
animation()
