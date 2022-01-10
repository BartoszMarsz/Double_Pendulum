import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

data = np.loadtxt('trajectory.pdb', delimiter=';')
time=data[1:, 0]
th1=data[1:, 1]
th2=data[1:, 2]
om1=data[1:, 3]
om2=data[1:, 4]
t=data[0][0]
h=data[0][1]
l1=data[0][2]
l2=data[0][3]

def animation():
    x1_data = []
    y1_data = []
    x2_data = []
    y2_data = []
    x1traj_data = []
    y1traj_data = []
    x2traj_data = []
    y2traj_data = []
    fig, ax = plt.subplots()
    ax.set_xlim(-(l1+l2), (l1+l2))
    ax.set_ylim(-(l1+l2), (l1+l2))
    line1, = ax.plot(0, 0)
    line2, = ax.plot(0, 0)
    traj1, = ax.plot(0, 0)
    traj2, = ax.plot(0, 0)
    ratio = 1.0
    x_left, x_right = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    ax.set_aspect(abs((x_right - x_left) / (y_low - y_high)) * ratio)
    ax.grid(color='dimgrey')
    ax.set_facecolor(color='black')


    def animation_frame(i):
        x1_data=np.linspace(0.0, l1*np.sin(th1[i]),10)
        y1_data=np.linspace(0.0, -l1*np.cos(th1[i]),10)
        x2_data=np.linspace(l1*np.sin(th1[i]), l1*np.sin(th1[i])+l2*np.sin(th2[i]), 10)
        y2_data=np.linspace(-l1*np.cos(th1[i]), -l1*np.cos(th1[i])-l2*np.cos(th2[i]), 10)
        x1traj_data.append(l1*np.sin(th1[i]))
        y1traj_data.append(-l1*np.cos(th1[i]))
        x2traj_data.append(l1*np.sin(th1[i])+l2*np.sin(th2[i]))
        y2traj_data.append(-l1*np.cos(th1[i])-l2*np.cos(th2[i]))
        line1.set_xdata(x1_data)
        line1.set_ydata(y1_data)
        line2.set_xdata(x2_data)
        line2.set_ydata(y2_data)
        traj1.set_xdata(x1traj_data)
        traj1.set_ydata(y1traj_data)
        traj2.set_xdata(x2traj_data)
        traj2.set_ydata(y2traj_data)
        return line1, line2, traj1, traj2

    animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, int(t/h), 1), interval=h*1000)
    plt.show()

animation()