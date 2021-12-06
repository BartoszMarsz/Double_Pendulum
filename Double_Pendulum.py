print('Hello world!')


import numpy as np

m_1=1
m_2=1
L_1=1
L_2=1
M=m_2/(m_1+m_2)
g=10

def f_1(theta_1,theta_2,omega_1,omega_2):
    gamma = theta_1-theta_2
    A=M*np.sin(theta_2)*np.cos(gamma)-np.sin(theta_1)
    B=M*L_2*((omega_2)^2)+L_1*((omega_1)^2)
    C=np.cos(gamma)*np.sin(gamma)
    D=L_1*(1-M*(np.cos(gamma))^2)
    return (g*(A-B)*C)/D


def f_2(theta_1, theta_2, omega_1, omega_2):
    gamma = theta_1 - theta_2
    A=(M*np.sin(theta_1)*np.cos(gamma)-np.sin(theta_2))
    B=(L_1*((omega_1)^2)+M*L_2*((omega_2)^2)*np.cos(gamma))**np.sin(gamma)
    C=(L_2*(1-M*(np.cos(gamma))^2))
    return (g*A+B)/C

K_th1_1=0
K_th2_1=0








