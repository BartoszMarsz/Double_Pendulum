import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

data = np.loadtxt('trajectory.pdb', delimiter=';')
time = np.array(data[1:, 0])
th1 = np.array(data[1:, 1])
th2 = np.array(data[1:, 2])
om1 = np.array(data[1:, 3])
om2 = np.array(data[1:, 4])
t = data[0][0]
h = data[0][1]
l1 = data[0][2]
l2 = data[0][3]

X1 = l1 * np.sin(th1)
Y1 = -l1 * np.cos(th1)
X2 = l1 * np.sin(th1) + l2 * np.sin(th2)
Y2 = -l1 * np.cos(th1) - l2 * np.cos(th2)


def animation():
    # defining figure and plots
    fig = plt.figure(figsize=(15, 5))
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 3)
    ax3 = fig.add_subplot(2, 2, (2, 4))

    # defining axises
    ax1.set_xlim(0, t)
    ax1.set_ylim(-10, 10)
    ax2.set_xlim(0, t)
    ax2.set_ylim(-10, 10)
    ax3.set_xlim(-1.1 * (l1 + l2), 1.1 * (l1 + l2))
    ax3.set_ylim(-1.1 * (l1 + l2), 1.1 * (l1 + l2))

    ax1.set_ylabel('[rad]', fontsize=12)
    ax2.set_ylabel(r'[$\frac{rad}{s}$]', fontsize=15)
    ax2.set_xlabel('t[s]', fontsize=12)
    ax3.set_xlabel('[m]', fontsize=12)
    ax3.set_ylabel('[m]', fontsize=12)

    # specifying appearance
    ax1.grid(color='dimgrey')
    ax1.set_facecolor(color='black')
    ax2.grid(color='dimgrey')
    ax2.set_facecolor(color='black')
    ax3.grid(color='dimgrey')
    ax3.set_facecolor(color='black')

    ratio = 1.0
    x_left, x_right = ax3.get_xlim()
    y_low, y_high = ax3.get_ylim()
    ax3.set_aspect(abs((x_right - x_left) / (y_low - y_high)) * ratio)

    # defining objects

    # theta and omega (graphs)
    TH1, = ax1.plot(0, 0)
    TH2, = ax1.plot(0, 0)
    OM1, = ax2.plot(0, 0)
    OM2, = ax2.plot(0, 0)
    # pendulum (motion)
    trajectory1, = ax3.plot(0, 0)
    trajectory2, = ax3.plot(0, 0)
    line1, = ax3.plot(0, 0)
    line2, = ax3.plot(0, 0)

    # defining legends
    ax1.legend((TH1, TH2), (r'$\theta_1$', r'$\theta_2$'), loc='upper right', shadow=True, labelcolor='white',
               facecolor='black')
    ax2.legend((OM1, OM2), (r'$\omega_1$', r'$\omega_2$'), loc='upper right', shadow=True, labelcolor='white',
               facecolor='black')

    # specifying objects appearance
    trajectory1.set_color('lightgray')
    trajectory1.set_alpha(0.3)
    trajectory2.set_color('lightgray')
    trajectory2.set_alpha(0.3)
    line1.set_color('darkorange')
    line2.set_color('mediumblue')
    line1.set_linewidth(2)
    line2.set_linewidth(2)

    def animation_frame(i):
        TH1.set_xdata(time[:i])
        TH1.set_ydata(th1[:i])
        TH2.set_xdata(time[:i])
        TH2.set_ydata(th2[:i])
        OM1.set_xdata(time[:i])
        OM1.set_ydata(om1[:i])
        OM2.set_xdata(time[:i])
        OM2.set_ydata(om2[:i])

        line1.set_xdata([0.0, X1[i]])
        line1.set_ydata([0.0, Y1[i]])
        line2.set_xdata([X1[i], X2[i]])
        line2.set_ydata([Y1[i], Y2[i]])
        trajectory1.set_xdata(X1[:i])
        trajectory1.set_ydata(Y1[:i])
        trajectory2.set_xdata(X2[:i])
        trajectory2.set_ydata(Y2[:i])

        return TH1, TH2, OM1, OM2, line1, line2, trajectory1, trajectory2,

    anim = FuncAnimation(fig, func=animation_frame, frames=range(1, int(t / h), 5), interval=10 * 5, repeat=False)
    plt.show()
