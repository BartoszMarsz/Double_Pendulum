import numpy as np
m_1=1.0
m_2=1.0
L_1=1.0
L_2=1.0
M=m_2/(m_1+m_2)
g=9.81

def f_1(theta_1,theta_2,omega_1,omega_2):
    gamma = theta_1-theta_2
    A=g*(M*np.sin(theta_2)*np.cos(gamma)-np.sin(theta_1))
    B=M*np.sin(gamma)*(L_2*(omega_2**2)+L_1*(omega_1**2)*np.cos(gamma))
    C=L_1*(1-M*np.cos(gamma)**2)
    return (A-B)/C

def f_2(theta_1, theta_2, omega_1, omega_2):
    gamma = theta_1 - theta_2
    A=g*(np.sin(theta_1)*np.cos(gamma)-np.sin(theta_2))
    B=(L_1*(omega_1)**2+M*L_2*(omega_2)**2*np.cos(gamma))*np.sin(gamma)
    C=(L_2*(1-M*np.cos(gamma)**2))
    return (A+B)/C

def keys(_th1, _th2, _om1, _om2):
    K_th1_j=_om1
    K_th2_j=_om2
    K_om1_j=f_1(_th1,_th2,_om1,_om2)
    K_om2_j=f_2(_th1,_th2,_om1,_om2)
    return K_th1_j,K_th2_j,K_om1_j,K_om2_j

def Runge_Kutta(h,th1,th2,om1,om2):
    K_th1_1,K_th2_1,K_om1_1,K_om2_1=keys(th1,th2,om1,om2)
    K_th1_2,K_th2_2,K_om1_2,K_om2_2=keys(th1+0.5*K_th1_1*h,th2+0.5*K_th2_1*h,om1+0.5*K_om1_1*h,om2+0.5*K_om2_1*h)
    K_th1_3,K_th2_3,K_om1_3,K_om2_3=keys(th1+0.5*K_th1_2*h,th2+0.5*K_th2_2*h,om1+0.5*K_om1_2*h,om2+0.5*K_om2_2*h)
    K_th1_4,K_th2_4,K_om1_4,K_om2_4=keys(th1+K_th1_3*h,th2+K_th2_3*h,om1+K_om1_3*h,om2+K_om2_3*h)
    th1_= th1 + 1/6*(K_th1_1+2*K_th1_2+2*K_th1_3+K_th1_4)*h
    th2_= th2 + 1/6*(K_th2_1+2*K_th2_2+2*K_th2_3+K_th2_4)*h
    om1_= om1 + 1/6*(K_om1_1+2*K_om1_2+2*K_om1_3+K_om1_4)*h
    om2_= om2 + 1/6*(K_om2_1+2*K_om2_2+2*K_om2_3+K_om2_4)*h
    return th1_,th2_,om1_,om2_