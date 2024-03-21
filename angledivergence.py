
"""This function finds the polar angles at which the array factor has local maxima
and calculates the divergence between those angles and the desired ones.
"""

import numpy as np
import MVDRalgorithm
from scipy.signal import find_peaks


def angle_divergence(initial_angles, M, SNR):

    # this is the array factor we will work on
    AF_diagram = MVDRalgorithm.MVDRalgorithm(M, initial_angles, SNR)[0]

    # create list that will contain the divergences of the angles
    Dth = list()
    # append the divergence of the first (desired) angle
    Dth.append(abs(np.array(AF_diagram).argmax()*0.1-initial_angles[0]))

    for i in range(1, len(initial_angles)):

        AF_shortened = np.zeros(200, dtype=np.complex_)
        inverse_AF = np.zeros(200, dtype=np.complex_)
        min_dist = 6000

        # in the array we save the AF values +/-10 degrees from the initial angle given to shorten the area of searching
        # the step is 0.1 so AF_dict has 200 items
        # we choose that arbitrarily considering that the null won't be far away from the initial angle
        # in the levels of noise we have
        for j in range(initial_angles[i]*10-100, initial_angles[i]*10+100):
            AF_shortened[j-(initial_angles[i]*10-100)] = AF_diagram[j]

        # find the inverse AF diagram
        # later we use the function that finds the peaks in order to find the minimums of the initial diagram
        for k in range(len(AF_shortened)):
            inverse_AF[k] = -AF_shortened[k]

        # find peaks of inverse, so the nulls
        AF_peaks_index = find_peaks(inverse_AF.real)[0]

        # move indices in the right place
        for z in range(len(AF_peaks_index)):
            AF_peaks_index[z] = AF_peaks_index[z] + (initial_angles[i]*10-100)

        # find the divergence between initial angles and real nulls
        for w in AF_peaks_index:
            if abs(w*0.1-initial_angles[i]) < min_dist:
                min_dist = abs(w*0.1-initial_angles[i])

        Dth.append(min_dist)

    return Dth
