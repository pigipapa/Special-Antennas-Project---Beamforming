# Special Antennas Project in Beamforming - Minimum Variance Distortionless Response

This is the second assignment of the Special Antennas course for the School of Electrical and Computer Engineering, 8th semester, AUTh, 2023.

In this project the Minimum Variance Distortionless Response (MVDR) algorithm is implemented.

A. The beamformer uses a linear antenna array of 24 isotropic elements (M=24) arranged on the z-axis and spaced apart by d=λ/2. A desired signal (n=0) with arrival
angle θ0 and five interference signals (N=5) with arrival angles θ1, θ2, θ3, θ4 and θ5 enter the beamformer.

B. A method is proposed, according to which, for each hexagon of angles θ0, θ1, θ2, θ3, θ4, θ5 defined within the interval [30, 150] (deg), we allocate a maximum of
another 18 angles of arrival of imaginary (false) interference signals θ6, ... , θ23 in the interval of polar angles [0, 180] (deg). The main purpose is for the side
lobe level (SLL) to be less than or equal to -20 dB compared to the main lobe.

C. Signal to Interference plus Noise Ratio is alsoo calculated along with the deviation of the main lobe from the direction of the desired signal and the deviations
of the nulls from the directions of the interference signals.
