from Runge_Kutta_method import *
def output(time,h,th1,th2,om1,om2):
    DATA = open('trajectory.pdb', 'a')
    for i in range(1,int(time/h+1)):
        DATA.write(str(round(i*h,2))+';'+str(round(th1,4))+';'+str(round(th2,4))+';'+str(round(om1,4))+';'+str(round(om2,4))+'\n')
        th1,th2,om1,om2 = Runge_Kutta(h,th1,th2,om1,om2)
    DATA.close()