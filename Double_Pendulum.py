from Data_output import *
import numpy as np
import time

l1 = 1
l2 = 1
m1 = 1
m2 = 1
h = 0.01
t = 60

const = (t, h, l1, l2, m1, m2)

th1 = np.pi / 3
th2 = np.pi / 3 + np.pi / 3
om1 = 0
om2 = 3

var = [th1, th2, om1, om2]

t1 = time.time()
output(const, var)
t2 = time.time()
print(t2 - t1)
from plot import *
from animation import *

graph()
trajectory()
animation()
