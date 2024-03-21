
"""This function generates a random set of 6 polar angles
of the desired and interference signals in the set [30, 150](deg)
The angles are separated by "delta" degrees.
"""

from numpy import random


def angle_generator(delta):

    theta = [0 for i in range(6)]
    k = 0

    angles_sets = list()

    # as k increases the angle we consider Θ0 at first increases by 1
    # the process repeats as many times as it takes for the larger angle to reach 150 degrees
    while theta[5] < 150:

        # create a set of 6 angles in range [30,150] that differ delta from one another
        for i in range(6):
            theta[i] = (30 + k) + i * delta

        # append first set into the list that concentrates every set
        angles_sets.append(theta)

        # make 5 more sets with the same angles as above but different order
        for j in range(5):
            a = theta.copy()
            a.remove(theta[j+1])
            a.insert(0, theta[j+1])
            angles_sets.append(a)

        k = k + 1

    # a random set that has been generated above is returned every time the function is called
    x = random.randint(len(angles_sets))

    return angles_sets[x]
