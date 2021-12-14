import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt('trajectory.pdb', delimiter=';')
#print(data)
#th1(t)
time=data[:,0]
th1=data[:,1]
th2=data[:,2]
om1=data[:,3]
om2=data[:,4]
plt.subplot(221)
plt.plot(time,th1,color='b',lw=1,ls='-',label='theta1(t)')
plt.legend()
plt.subplot(222)
plt.plot(time,th2,color='r',lw=1,ls='-',label='theta2(t)')
plt.legend()
plt.subplot(223)
plt.plot(time,om1,color='g',lw=1,ls='-',label='omega1(t)')
plt.legend()
plt.subplot(224)
plt.plot(time,om2,color='y',lw=1,ls='-',label='omega2(t)')
plt.legend()
plt.show()