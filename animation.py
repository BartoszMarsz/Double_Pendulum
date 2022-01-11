import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import time as ti
data = np.loadtxt('trajectory.pdb', delimiter=';')
time=np.array(data[1:, 0])
th1=np.array(data[1:, 1])
th2=np.array(data[1:, 2])
om1=np.array(data[1:, 3])
om2=np.array(data[1:, 4])
t=data[0][0]
h=data[0][1]
l1=data[0][2]
l2=data[0][3]

X1 = l1*np.sin(th1)
Y1 = -l1*np.cos(th1)
X2 = l1*np.sin(th1)+l2*np.sin(th2)
Y2 = -l1*np.cos(th1)-l2*np.cos(th2)
def graph_anim():
    fig, (ax1,ax2) = plt.subplots(2,1)
    ax1.set_xlim(0, t)
    ax1.set_ylim(-10, 10)
    ax2.set_xlim(0, t)
    ax2.set_ylim(-10, 10)
    ax1.set_ylabel('[rad]', fontsize=12)
    ax2.set_ylabel(r'[$\frac{rad}{s}$]', fontsize=15)
    ax2.set_xlabel('t[s]', fontsize=12)
    TH1, = ax1.plot(0, 0)
    TH2, = ax1.plot(0, 0)
    OM1, = ax2.plot(0, 0)
    OM2, = ax2.plot(0, 0)
    ax1.legend((TH1, TH2), (r'$\theta_1$', r'$\theta_2$'), loc='upper right', shadow=True, labelcolor='white', facecolor='black')
    ax2.legend((OM1, OM2), (r'$\omega_1$', r'$\omega_2$'), loc='upper right', shadow=True, labelcolor='white', facecolor='black')
    ax1.grid(color='dimgrey')
    ax1.set_facecolor(color='black')
    ax2.grid(color='dimgrey')
    ax2.set_facecolor(color='black')
    def animation_frame(i):
        TH1.set_xdata(time[:i])
        TH1.set_ydata(th1[:i])
        TH2.set_xdata(time[:i])
        TH2.set_ydata(th2[:i])
        OM1.set_xdata(time[:i])
        OM1.set_ydata(om1[:i])
        OM2.set_xdata(time[:i])
        OM2.set_ydata(om2[:i])
        return TH1, TH2, OM1, OM2,

    animation = FuncAnimation(fig, func=animation_frame, frames=range(1,1000,10), interval=100, repeat=False)

    plt.show()

def animation():
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
        line1.set_xdata([0.0, X1[i]])
        line1.set_ydata([0.0, Y1[i]])
        line2.set_xdata([X1[i], X2[i]])
        line2.set_ydata([Y1[i], Y2[i]])
        traj1.set_xdata(X1[:i])
        traj1.set_ydata(Y1[:i])
        traj2.set_xdata(X2[:i])
        traj2.set_ydata(Y2[:i])
        return line1, line2, traj1, traj2

    animation = FuncAnimation(fig, func=animation_frame, frames=range(1,1000,10), interval=100, repeat=False)
    plt.show()