from Runge_Kutta_method import *
h = 0.01
th1_0 = 1.047
th2_0 = 0
om1_0 = 0
om2_0 = 0
th1_1,th2_1,om1_1,om2_1 = Runge_Kutta(h,th1_0,th2_0,om1_0,om2_0)
print(th1_1,th2_1,om1_1,om2_1)







