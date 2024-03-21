
"""This function creates a new file called AoAdev_SINR_SLL.txt and saves
the initial angles θ0, θ1, θ2, θ3, θ4, θ5, the angle divergences Δθ0, Δθ1, Δθ2,
Δθ3, Δθ4, Δθ5, the SINR and SLL values in one line.
Afterwards, the data are split into 4 categories: a list containing all Δθ0,
a list containing all Δθ0, Δθ1, Δθ2, Δθ3, Δθ4, Δθ5, a list containing all SINR values
and a list containing SLL values, which are returned.
"""


def create_file(file_input):

    # append data into file
    with open('AoAdev_SINR_SLL.txt', 'a') as f:
        for line in file_input:
            f.write(f"{line} ")
        f.write("\n")
    f.close()

    # split data into 4 different lists
    f = open('AoAdev_SINR_SLL.txt', "r")
    lines = f.readlines()
    resDth0 = []
    resDth = []
    resSINR = []
    resSLL = []
    for x in lines:
        resDth0.append(x.split(' ')[6])
        resDth.append(x.split(' ')[7])
        resDth.append(x.split(' ')[8])
        resDth.append(x.split(' ')[9])
        resDth.append(x.split(' ')[10])
        resDth.append(x.split(' ')[11])
        resSINR.append(x.split(' ')[12])
        resSLL.append(x.split(' ')[13])
    f.close()

    return resDth0, resDth, resSINR, resSLL
