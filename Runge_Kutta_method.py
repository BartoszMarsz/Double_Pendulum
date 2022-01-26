import numpy as np
import sys

def Runge_Kutta(const, var):
    var = np.reshape(np.array(var), (4, 1))
    t, h, L_1, L_2, m_1, m_2 = const
    M = m_2 / (m_1 + m_2)
    g = 9.81

    def f_1(var):
        theta_1, theta_2, omega_1, omega_2 = var
        gamma = theta_1 - theta_2
        A = g * (M * np.sin(theta_2) * np.cos(gamma) - np.sin(theta_1))
        B = M * np.sin(gamma) * (L_2 * (omega_2 ** 2) + L_1 * (omega_1 ** 2) * np.cos(gamma))
        C = L_1 * (1 - M * np.cos(gamma) ** 2)
        return (A - B) / C

    def f_2(var):
        theta_1, theta_2, omega_1, omega_2 = var
        gamma = theta_1 - theta_2
        A = g * (np.sin(theta_1) * np.cos(gamma) - np.sin(theta_2))
        B = (L_1 * (omega_1) ** 2 + M * L_2 * (omega_2) ** 2 * np.cos(gamma)) * np.sin(gamma)
        C = (L_2 * (1 - M * np.cos(gamma) ** 2))
        return (A + B) / C

    def keys(var):
        K_th1_j = var[2]
        K_th2_j = var[3]
        K_om1_j = f_1(var)
        K_om2_j = f_2(var)
        return np.array([K_th1_j, K_th2_j, K_om1_j, K_om2_j])

    K_1 = keys(var)
    K_2 = keys(var + 0.5 * K_1 * const[1])
    K_3 = keys(var + 0.5 * K_2 * const[1])
    K_4 = keys(var + K_3 * const[1])


    K = np.array([K_1, K_2, K_3, K_4])

    var = var + 1 / 6 * const[1] * (np.reshape(K[0] + 2 * K[1] + 2 * K[2] + K[3], (4, 1)))
    return var
