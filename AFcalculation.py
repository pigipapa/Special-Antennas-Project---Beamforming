
"""This function calculates and returns the normalized array factor of an array antenna.
"""

import math
import numpy as np
import cmath


def AFtheta(weights, M, step):

    # hermitian of weight matrix
    wh = np.transpose(weights).conj()

    #initialization of antenna factor and steering vector
    AFth = np.zeros((int(180/step), 1), dtype=np.complex_)
    ath = np.zeros((M, 1), dtype=np.complex_)

    # calculation of AF
    for j in range(int(180/step)):
        for i in range(M):
            c = cmath.exp(i * 1j * math.pi * math.cos(math.radians(j*step)))
            c = round(c.real, 3) + round(c.imag, 3) * 1j
            ath[i] = c
        AFth[j] = abs(np.dot(wh, ath))

    # the maximum of AF amplitude in order to normalize
    maxAF = max(AFth).real[0]
    for j in range(int(180/step)):
        AFth[j] = AFth[j]/maxAF

    return AFth
