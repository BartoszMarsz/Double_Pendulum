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

def graph():
    plt.subplot(221)
    plt.plot(time, th1,color='b', lw=1, ls='-')
    plt.ylabel(r'$\theta_1$[rad]',fontsize=12)
    plt.xticks(np.arange(0, t+0.5, 1))
    plt.grid(color='lightgrey')

    plt.subplot(222)
    plt.plot(time, th2, color='r', lw=1, ls='-')
    plt.ylabel(r'$\theta_2$[rad]', fontsize=12)
    plt.xticks(np.arange(0, t+0.5, 1))
    plt.grid(color='lightgrey')

    plt.subplot(223)
    plt.plot(time, om1, color='g', lw=1, ls='-')
    plt.xlabel('t[s]', fontsize=12)
    plt.ylabel(r'$\omega_1[\frac{rad}{s}]$', fontsize=12)
    plt.xticks(np.arange(0, t+0.5, 1))
    plt.grid(color='lightgrey')

    plt.subplot(224)
    plt.plot(time, om2, color='y', lw=1, ls='-')
    plt.xlabel('t[s]', fontsize=12)
    plt.ylabel(r'$\omega_2[\frac{rad}{s}]$', fontsize=12)
    plt.xticks(np.arange(0, t+0.5, 1))
    plt.grid(color='lightgrey')
    #





    #
    plt.show()

def trajectory(const):
    fig, ax = plt.subplots()

    x1 = l1*np.sin(th1)
    y1 = -l1*np.cos(th1)
    x2=l1*np.sin(th1)+l2*np.sin(th2)
    y2=-l1*np.cos(th1)-l2*np.cos(th2)
    plt.plot(x1, y1, color='b', label='punk materialny1(t)')
    plt.plot(x2, y2, color='r', label='punkt materialny2(t)')
    plt.xticks(np.arange(-(l1+l2), l1+l2+0.1, 1))
    plt.yticks(np.arange(-(l1+l2), l1+l2+0.1, 1))

    ratio = 1.0
    x_left, x_right = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    ax.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)

    plt.legend(loc='upper right')
    plt.xlabel('x')
    plt.ylabel('y')
   #
    ax.grid(color='lightgrey')
    #ax.set_facecolor(color='')

    #
    plt.show()

def animation():
    x1_data = []
    y1_data = []
    x2_data = []
    y2_data = []
    fig, ax = plt.subplots()
    ax.set_xlim(-(l1+l2), (l1+l2))
    ax.set_ylim(-(l1+l2), (l1+l2))
    line1, = ax.plot(0, 0)
    line2, = ax.plot(0, 0)
    ratio = 1.0
    x_left, x_right = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    ax.set_aspect(abs((x_right - x_left) / (y_low - y_high)) * ratio)
    ax.grid(color='lightgrey')
    #ax.set_facecolor(color='darkblue')



    def animation_frame(i):
        x1_data=np.linspace(0.0, l1*np.sin(th1[i]),10)
        y1_data=np.linspace(0.0, -l1*np.cos(th1[i]),10)
        x2_data=np.linspace(l1*np.sin(th1[i]), l1*np.sin(th1[i])+l2*np.sin(th2[i]), 10)
        y2_data=np.linspace(-l1*np.cos(th1[i]), -l1*np.cos(th1[i])-l2*np.cos(th2[i]), 10)
        line1.set_xdata(x1_data)
        line1.set_ydata(y1_data)
        line2.set_xdata(x2_data)
        line2.set_ydata(y2_data)
        return line1, line2,

    animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, int(t/h), 1), interval=h*1000)
    plt.show()
