
"""This function locates the two maximum side lobes at a time
and insets nulls at the angles the maxima are
This procedure is repeated until the side lobe level (SLL)
is below -20dB.
"""

import numpy as np
import MVDRalgorithm
from scipy.signal import find_peaks


def interference_generator(initial_angles, M, SNR, num_of_interference):

    # calculate the AF given the 6 initial angles
    initial_AF = MVDRalgorithm.MVDRalgorithm(M, initial_angles, SNR)[0]

    # copy initial_AF in a second matrix
    initial_AF_2 = np.zeros(len(initial_AF), dtype=np.complex_)
    for i in range(len(initial_AF)):
        initial_AF_2[i] = initial_AF[i]

    # in this dictionary are stored the indices of peaks and the values of AF in this position
    peak_dict = dict()
    # find peak indices
    AF_peak_indices = find_peaks(initial_AF_2.real)[0]
    # find the values of AF of those indices
    values_of_peak_indices = [initial_AF_2[i] for i in AF_peak_indices]

    for i in range(len(AF_peak_indices)):
        peak_dict[AF_peak_indices[i]] = values_of_peak_indices[i]

    # sort the values of dictionary in ascending order
    sorted_AF_peak_values = sorted(peak_dict.items(), key=lambda x: x[1], reverse=True)
    converted_sorted_AF_peak_values = dict(sorted_AF_peak_values)

    # find the index and angle of the second maximum AF value
    second_maximum_of_AF_index = int(list(converted_sorted_AF_peak_values.keys())[1])
    second_maximum_of_AF_angle = second_maximum_of_AF_index * 0.1

    # find the index and angle of the third maximum AF value
    third_maximum_of_AF_index = int(list(converted_sorted_AF_peak_values.keys())[2])
    third_maximum_of_AF_angle = third_maximum_of_AF_index * 0.1

    # new_angles list now contains the 6 initial angles
    new_angles = initial_angles.copy()

    # calculation of side lobe level (SLL)
    SLL = 20 * np.log10(initial_AF_2[second_maximum_of_AF_index])
    SINR = 0

    new_AF = list()

    # while z does not exceed the number of the imaginary interference signals and SLL is above -20dB repeat
    # until we get the first AF diagram with SLL<=-20dB repeat
    z = 0
    while z < num_of_interference and SLL > -20:

        # the second and third angle to steer a null at is the angle where the next larger lobe is
        new_angles.append(second_maximum_of_AF_angle)
        new_angles.append(third_maximum_of_AF_angle)

        res = MVDRalgorithm.MVDRalgorithm(M, new_angles, SNR)
        # calculate the current AF
        new_AF = res[0]
        # calculate current SINR
        SINR = res[1]

        for i in range(len(new_AF)):
            initial_AF_2[i] = new_AF[i]

        peak_dict = dict()

        AF_peak_indices = find_peaks(initial_AF_2.real)[0]

        values_of_peak_indices = [initial_AF_2[i] for i in AF_peak_indices]

        for i in range(len(AF_peak_indices)):
            peak_dict[AF_peak_indices[i]] = values_of_peak_indices[i]

        sorted_AF_peak_values = sorted(peak_dict.items(), key=lambda x: x[1], reverse=True)
        converted_sorted_AF_peak_values = dict(sorted_AF_peak_values)

        # after erasing the main lobe we can calculate the grater side lobe because now it is the dominant one
        second_maximum_of_AF_index = int(list(converted_sorted_AF_peak_values.keys())[1])
        second_maximum_of_AF_angle = second_maximum_of_AF_index * 0.1

        third_maximum_of_AF_index = int(list(converted_sorted_AF_peak_values.keys())[2])
        third_maximum_of_AF_angle = third_maximum_of_AF_index * 0.1

        # calculate SLL
        SLL = 20 * np.log10(initial_AF_2[second_maximum_of_AF_index])

        z += 2

    print("SLL = ", SLL)
    print("new_angles = ", new_angles)

    step = 0.1
    x_axis = np.zeros((int(180 / step), 1), dtype=np.complex_)
    for i in range(int(180 / step)):
        x_axis[i] = step * i

    return SINR, SLL.real, new_AF, x_axis
