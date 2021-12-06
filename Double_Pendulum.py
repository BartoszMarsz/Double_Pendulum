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
    return (g(M*np.sin(theta_2)*np.cos(gamma)-np.sin(theta_1))
     -M*(L_2*((omega_2)^2)+L_1*((omega_1)^2)*np.cos(gamma))*np.sin(gamma))\
    /(L_1(1-M*(np.cos(gamma))^2))


def f_2(theta_1, theta_2, omega_1, omega_2):
    gamma = theta_1 - theta_2

    return (g(M*np.sin(theta_1)*np.cos(gamma)-np.sin(theta_2))
     +(L_1*((omega_1)^2)+M*L_2*((omega_2)^2)*np.cos(gamma))*np.sin(gamma))\
    /(L_2(1-M*(np.cos(gamma))^2))










