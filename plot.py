import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('trajectory.pdb', delimiter=';')
time = data[1:, 0]
th1 = data[1:, 1]
th2 = data[1:, 2]
om1 = data[1:, 3]
om2 = data[1:, 4]
t = data[0][0]
h = data[0][1]
l1 = data[0][2]
l2 = data[0][3]


def graph():
    plt.subplot(221)
    plt.title(r'Graph of $\theta_1(t)$', fontsize=15)
    plt.plot(time, th1, color='darkorange', lw=1, ls='-')
    plt.ylabel(r'$\theta_1$[rad]', fontsize=15)
    plt.yticks(fontsize=15)
    plt.xticks(fontsize=15)
    plt.xlim(0,t)
    plt.grid(color='dimgrey')

    plt.subplot(222)
    plt.title(r'Graph of $\theta_2(t)$', fontsize=15)
    plt.plot(time, th2, color='mediumblue', lw=1, ls='-')
    plt.ylabel(r'$\theta_2$[rad]', fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlim(0,t)
    plt.xticks(fontsize=15)
    plt.grid(color='dimgrey')

    plt.subplot(223)
    plt.title(r'Graph of $\omega_1(t)$', fontsize=15)
    plt.plot(time, om1, color='darkorange', lw=1, ls='-')
    plt.xlabel('t[s]', fontsize=15)
    plt.yticks(fontsize=15)
    plt.ylabel(r'$\omega_1[\frac{rad}{s}]$', fontsize=15)
    plt.xlim(0,t)
    plt.xticks(fontsize=15)
    plt.grid(color='dimgrey')

    plt.subplot(224)
    plt.title(r'Graph of $\omega_2(t)$', fontsize=15)
    plt.plot(time, om2, color='mediumblue', lw=1, ls='-')
    plt.xlabel('t[s]', fontsize=15)
    plt.yticks(fontsize=15)
    plt.ylabel(r'$\omega_2[\frac{rad}{s}]$', fontsize=15)
    plt.xlim(0,t)
    plt.xticks(fontsize=15)
    plt.grid(color='dimgrey')

    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.show()

def trajectory():
    fig, ax = plt.subplots()
    plt.title('Trajectory', fontsize=15)
    x1 = l1 * np.sin(th1)
    y1 = -l1 * np.cos(th1)
    x2 = l1 * np.sin(th1) + l2 * np.sin(th2)
    y2 = -l1 * np.cos(th1) - l2 * np.cos(th2)
    plt.plot(x1, y1, color='darkorange', label='mass 1')
    plt.plot(x2, y2, color='mediumblue', label='mass 2')
    plt.xticks(np.arange(-(l1 + l2), l1 + l2 + 0.1, 1), fontsize=15)
    plt.yticks(np.arange(-(l1 + l2), l1 + l2 + 0.1, 1), fontsize=15)

    ratio = 1.0
    x_left, x_right = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    ax.set_aspect(abs((x_right - x_left) / (y_low - y_high)) * ratio)

    plt.legend(loc='upper right',fontsize=15)
    plt.xlabel('x',fontsize=15)
    plt.ylabel('y',fontsize=15)

    ax.grid(color='dimgrey')
    ax.set_facecolor(color='black')

    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.show()
