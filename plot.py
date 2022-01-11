import matplotlib.pyplot as plt
import numpy as np

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
    plt.grid(color='dimgrey')

    plt.subplot(222)
    plt.plot(time, th2, color='r', lw=1, ls='-')
    plt.ylabel(r'$\theta_2$[rad]', fontsize=12)
    plt.xticks(np.arange(0, t+0.5, 1))
    plt.grid(color='dimgrey')


    plt.subplot(223)
    plt.plot(time, om1, color='g', lw=1, ls='-')
    plt.xlabel('t[s]', fontsize=12)
    plt.ylabel(r'$\omega_1[\frac{rad}{s}]$', fontsize=12)
    plt.xticks(np.arange(0, t+0.5, 1))
    plt.grid(color='dimgrey')


    plt.subplot(224)
    plt.plot(time, om2, color='y', lw=1, ls='-')
    plt.xlabel('t[s]', fontsize=12)
    plt.ylabel(r'$\omega_2[\frac{rad}{s}]$', fontsize=12)
    plt.xticks(np.arange(0, t+0.5, 1))
    plt.grid(color='dimgrey')

    plt.show()

def trajectory():
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

    ax.grid(color='dimgrey')
    ax.set_facecolor(color='black')

    plt.show()











