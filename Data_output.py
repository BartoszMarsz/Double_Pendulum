from Runge_Kutta_method import *
def output(const=(), var=[]):
    DATA = open('trajectory.pdb', 'w')
    DATA.write(str(const[0])+';'+str(const[1])+';'+str(const[2])+';'+str(const[3])+';'+'0')
    DATA.write('\n')
    for i in range(0,int(const[0]/const[1]+1)):
        DATA.write(str(round(i*const[1],2)))
        for j in var:
            DATA.write(';'+str(round(j,4)))
        DATA.write('\n')
        var = np.reshape(Runge_Kutta(const,var),(4))

    DATA.close()
