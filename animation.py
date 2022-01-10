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
def graph_anim():
    time_data =[]
    th1_data =[]
    th2_data =[]
    om1_data=[]
    om2_data=[]

    fig, (ax1,ax2) = plt.subplots(2,1)
    ax1.set_xlim(0, t)
    ax1.set_ylim(-5, 5)
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
        time_data.append(time[i])
        th1_data.append(th1[i])
        th2_data.append(th2[i])
        om1_data.append(om1[i])
        om2_data.append(om2[i])
        TH1.set_xdata(time_data)
        TH1.set_ydata(th1_data)
        TH2.set_xdata(time_data)
        TH2.set_ydata(th2_data)
        OM1.set_xdata(time_data)
        OM1.set_ydata(om1_data)
        OM2.set_xdata(time_data)
        OM2.set_ydata(om2_data)
        return TH1, TH2, OM1, OM2,

    animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, int(t/h), 1), interval=h*1000)
    plt.show()

def animation():
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
graph_anim()
animation()