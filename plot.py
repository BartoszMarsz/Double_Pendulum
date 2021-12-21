import matplotlib.pyplot as plt
import numpy as np



data = np.loadtxt('trajectory.pdb', delimiter=';')
time=data[:,0]
th1=data[:,1]
th2=data[:,2]
om1=data[:,3]
om2=data[:,4]
t=data[-1][0]


plt.subplot(221)
plt.plot(time,th1,color='b',lw=1,ls='-',label='theta1(t)')
plt.ylabel('theta1',fontsize=12)

plt.xlabel('t[s]',fontsize=12)
plt.xticks(np.arange(0,t,1))
plt.legend(loc='upper right')
plt.xlabel('t[t]')
plt.ylabel('theta1')


plt.subplot(222)
plt.plot(time,th2,color='r',lw=1,ls='-',label='theta2(t)')
plt.legend(loc='upper right')
plt.xlabel('t[s]')
plt.ylabel('theta2')
plt.xticks(np.arange(0,t,1))


plt.subplot(223)
plt.plot(time,om1,color='g',lw=1,ls='-',label='omega1(t)')
plt.legend(loc='upper right')
plt.xlabel('t[s]')
plt.ylabel('omega1[rad/s]')
plt.xticks(np.arange(0,t,1))

plt.subplot(224)
plt.plot(time,om2,color='y',lw=1,ls='-',label='omega2(t)')
plt.legend(loc='upper right')
plt.xlabel('t[s]')
plt.ylabel('omega2[rad/s]')
plt.xticks(np.arange(0,t,1))


plt.show()

#-----------

fig, ax = plt.subplots()

x1 = 1*np.sin(data[:,1])
y1 = -1*np.cos(data[:,1])
x2=1*np.sin(data[:,1])+1*np.sin(data[:,2])
y2=-1*np.cos(data[:,1])-1*np.cos(data[:,2])
plt.plot(x1,y1,color='b',label='punk materialny1(t)')
plt.plot(x2,y2,color='r',label='punkt materialny2(t)')
plt.xticks(np.arange(-2,2.5,1))
plt.yticks(np.arange(-2,2.5,1))

ratio = 1.0
x_left, x_right = ax.get_xlim()
y_low, y_high = ax.get_ylim()
ax.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)

plt.legend(loc='upper right')
plt.xlabel('x')
plt.ylabel('y')
plt.show()