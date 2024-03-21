import anglegenerator
import interferencegenerator
import angledivergence
import matplotlib.pyplot as plt
import createfile
import statistics


SNR = 20
delta = 10
M = 24
max_num_of_inter_signals = 18

initial_angles = anglegenerator.angle_generator(delta)
Dth = angledivergence.angle_divergence(initial_angles, M, SNR)
inter = interferencegenerator.interference_generator(initial_angles, M, SNR, max_num_of_inter_signals)

SINR = inter[0]
SLL = inter[1]

y_axis = inter[2].real
x_axis = inter[3].real

# plotting the normalized amplitude of antenna factor
plt.plot(x_axis, y_axis, label="Array Factor")
plt.title('radiation')
plt.ylabel('AF')
plt.xlabel('θ')
plt.legend()
plt.show()

file_input = initial_angles + Dth
file_input.append(SINR)
file_input.append(SLL)

data = createfile.create_file(file_input)
statistics.statistics_output(data[0], data[1], data[2], data[3])
