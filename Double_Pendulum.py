from Runge_Kutta_method import *
import numpy as np
import time as t
h = 0.001
th1 = np.pi/3
th2 = 0.0
om1 = 0.0
om2 = 0.0
t1=t.time()
for i in range(1,10001):
    th1,th2,om1,om2 = Runge_Kutta(h,th1,th2,om1,om2)
t2=t.time()
print(th1,th2,om1,om2)
print(t2-t1)





