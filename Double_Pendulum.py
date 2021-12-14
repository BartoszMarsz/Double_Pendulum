from Data_output import *
import numpy as np
import time as t
h = 0.01
th1 = np.pi/3
th2 = np.pi/6
om1 = 0
om2 = 0
t1=t.time()
output(2,h,th1,th2,om1,om2)
t2=t.time()
print(t2-t1)

