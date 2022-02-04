from Data_output import *
from tkinter import *

root = Tk()
root.title('Double Pendulum')

t_th1 = Label(root, text='theta1 [rad]', font=("Arial", 15))
t_th2 = Label(root, text='theta2 [rad]', font=("Arial", 15))
t_om1 = Label(root, text='omega1 [rad/s]', font=("Arial", 15))
t_om2 = Label(root, text='omega2 [rad/s]', font=("Arial", 15))

e_th1 = Entry(root, width=15, borderwidth=5, font=("Arial", 15))
e_th1.insert(0, 0)
e_th2 = Entry(root, width=15, borderwidth=5,font=("Arial", 15))
e_th2.insert(0, 0)
e_om1 = Entry(root, width=15, borderwidth=5,font=("Arial", 15))
e_om1.insert(0, 0)
e_om2 = Entry(root, width=15, borderwidth=5,font=("Arial", 15))
e_om2.insert(0, 0)

t_l1 = Label(root, text='l1 [m]', font=("Arial", 15))
t_l2 = Label(root, text='l2 [m]', font=("Arial", 15))
t_m1 = Label(root, text='m1 [kg]', font=("Arial", 15))
t_m2 = Label(root, text='m2 [kg]', font=("Arial", 15))

e_l1 = Entry(root, width=15, borderwidth=5,font=("Arial", 15))
e_l1.insert(0, 1)
e_l2 = Entry(root, width=15, borderwidth=5,font=("Arial", 15))
e_l2.insert(0, 1)
e_m1 = Entry(root, width=15, borderwidth=5,font=("Arial", 15))
e_m1.insert(0, 1)
e_m2 = Entry(root, width=15, borderwidth=5,font=("Arial", 15))
e_m2.insert(0, 1)

t_t = Label(root, text='How many seconds?',font=("Arial", 15))
e_t = Entry(root, width=15, borderwidth=5,font=("Arial", 15))
e_t.insert(0, 10)


def compute():
    try:
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
    except ValueError:
        t_err = Label(root, text='Error! Bad values type.').grid()
    else:
        try:
            if l1 < 1 or l2 < 1 or m1 < 1 or m2 < 1 or l1 > 10 or l2 > 10 or m1 > 10 or m2 > 10 or t < 0.01:
                raise ValueError()
        except ValueError:
            t_err = Label(root, text='Error! Bad values.').grid()
        else:
            output(const, var)
            root.quit()

b_compute = Button(root, text='Compute!', command=compute, padx=100, pady=25, font=("Arial", 15))

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

b_compute.grid(column=0, row=5, columnspan=4)

root.mainloop()
from plot import *
from animation import *

animation()
graph()
trajectory()