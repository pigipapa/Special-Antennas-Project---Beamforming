
"""This function calculates and prints the minimum value, the maximum value,
the average and the standard deviation of Dth0 results, Dth results,
SINR results and SLL results given as lists withdrawn from the AoAdev_SINR_SLL.txt file.
"""

import numpy as np


def statistics_output(resDth0, resDth, resSINR, resSLL):

    # converting the elements of the lists from string to integers
    resDth0 = [eval(i) for i in resDth0]
    resDth = [eval(i) for i in resDth]
    resSINR = [eval(i) for i in resSINR]
    resSLL = [eval(i) for i in resSLL]

    # for Dth0
    min_value_of_Dth0 = min(resDth0)
    max_value_of_Dth0 = max(resDth0)
    average_of_Dth0 = sum(resDth0) / len(resDth0)
    stdev_of_Dth0 = np.std(resDth0)

    print("min_value_of_Dth0 = ", round(min_value_of_Dth0, 3))
    print("max_value_of_Dth0 = ", round(max_value_of_Dth0, 3))
    print("average_of_Dth0 = ", round(average_of_Dth0, 3))
    print("stdev_of_Dth0 = ", stdev_of_Dth0)

    # for Dth
    min_value_of_Dth = min(resDth)
    max_value_of_Dth = max(resDth)
    average_of_Dth = sum(resDth) / len(resDth)
    stdev_of_Dth = np.std(resDth)

    print("min_value_of_Dth = ", round(min_value_of_Dth, 3))
    print("max_value_of_Dth = ", round(max_value_of_Dth, 3))
    print("average_of_Dth = ", round(average_of_Dth, 3))
    print("stdev_of_Dth = ", stdev_of_Dth)

    # for SINR
    min_value_of_SINR = min(resSINR)
    max_value_of_SINR = max(resSINR)
    average_of_SINR = sum(resSINR) / len(resSINR)
    stdev_of_SINR = np.std(resSINR)

    print("min_value_of_SINR = ", round(min_value_of_SINR, 3))
    print("max_value_of_SINR = ", round(max_value_of_SINR, 3))
    print("average_of_SINR = ", round(average_of_SINR, 3))
    print("stdev_of_SINR = ", stdev_of_SINR)

    # for SLL
    min_value_of_SLL = min(resSLL)
    max_value_of_SLL = max(resSLL)
    average_of_SLL = sum(resSLL) / len(resSLL)
    stdev_of_SLL = np.std(resSLL)

    print("min_value_of_SLL = ", round(min_value_of_SLL, 3))
    print("max_value_of_SLL = ", round(max_value_of_SLL, 3))
    print("average_of_SLL = ", round(average_of_SLL, 3))
    print("stdev_of_SLL = ", stdev_of_SLL)
