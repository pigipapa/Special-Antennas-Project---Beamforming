
"""This function implies the algorithm of Minimum Variance Distortionless Response beamformer
with a difference in diagonal loading.
"""

import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
import AFcalculation


def MVDRalgorithm(M, angles, SNR):

    ad = np.zeros(M, dtype=np.complex_)  # initialization of steering vector of the desired signal

    #  set values of steering vector of desired signal
    for i in range(M):
        c = cmath.exp(i * 1j * math.pi * math.cos(math.radians(angles[0])))
        c = round(c.real, 3) + round(c.imag, 3) * 1j
        ad[i] = c

    # hermitian of steering vector of the desired signal
    adh = np.transpose(ad).conj()

    Pn = 10**(-SNR/10)  # power of noise
    Rnn = np.identity(M)*Pn  # covariance matrix of noise
    Rgg = np.identity(len(angles))  # covariance matrix of modulating function
    A = np.zeros((M, len(angles)), dtype=np.complex_)  # steering matrix initialization

    # set values of steering matrix
    for i in range(M):
        for j in range(len(angles)):
            a = cmath.exp(1j * i * math.pi * math.cos(math.radians(angles[j])))
            a = round(a.real, 3) + round(a.imag, 3) * 1j
            A[i][j] = a

    # hermitian of steering matrix
    Ah = np.transpose(A).conj()
    # the dot product of A and Rgg to help with calculations
    ARgg = np.dot(A, Rgg)
    # covariance matrix of initial signal x
    Rxx = np.add(np.dot(ARgg, Ah), Rnn)

    # diagonal loading that depends on the SNR
    if SNR >= 10:
        Rxx = np.add(Rxx, 100*Pn * np.identity(len(Rxx)))
    elif 0 <= SNR < 10:
        Rxx = np.add(Rxx, 10 * Pn * np.identity(len(Rxx)))
    else:
        Rxx = np.add(Rxx, Pn * np.identity(len(Rxx)))

    # the dot product of adh and Rxx
    adhRxx = np.dot(adh, np.linalg.inv(Rxx))
    # weights of modulation matrix
    Wmv = np.dot(np.linalg.inv(Rxx), ad) / (np.dot(adhRxx, ad))
    # covariance of interference signal modulation function
    Rgigi = np.identity(len(angles)-1)
    # initialization of steering matrix of interference signals
    Ai = np.zeros((M, len(angles)-1), dtype=np.complex_)

    # set values of steering matrix of interference signals
    for i in range(M):
        for j in range(len(angles)-1):
            a = cmath.exp(1j * i * math.pi * math.cos(math.radians(angles[j+1])))
            a = round(a.real, 3) + round(a.imag, 3) * 1j
            Ai[i][j] = a

    # hermitian of steering matrix of interference signals
    Aih = np.transpose(Ai).conj()
    # hermitian of weights matrix
    Wmvh = np.transpose(Wmv).conj()
    # hermitian of desired signals' steering vector
    adh = np.transpose(ad).conj()
    # dot product of Ai and Rgigi
    AiRgigi = np.dot(Ai, Rgigi)

    # calculation of SINR in dB
    SINR = 10 * math.log10((np.dot(np.dot(Wmvh, ad), np.dot(adh, Wmv))
                            / np.add(np.dot(np.dot(Wmvh, AiRgigi), np.dot(Aih, Wmv)),
                                     np.dot(np.dot(Wmvh, Rnn), Wmv))).real)

    step = 0.1  # step of angle sweep

    # initialization and calculation of x-axis values
    x_axis = np.zeros((int(180/step), 1), dtype=np.complex_)
    for i in range(int(180/step)):
        x_axis[i] = step*i

    # calculation of y-axis values from our function
    y_axis = AFcalculation.AFtheta(Wmv, M, step)

    """
    # plotting the normalized amplitude of antenna factor
    plt.plot(x_axis, y_axis, label="Array Factor")
    plt.title('radiation')
    plt.ylabel('AF')
    plt.xlabel('θ')
    plt.legend()
    plt.show()
    """

    return y_axis, SINR, x_axis
