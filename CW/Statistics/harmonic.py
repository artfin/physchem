import numpy as np
import math as m
import matplotlib.pyplot as plt

omega = 2 * 10**(-1)
h = 6.63 * 10**(-34)
k = 1.38 * 10**(-23)

N = 2 # levels in oscillator

def _vibrational_partition_function(temperature):
	summ = 0
	beta = 1 / (k * temperature)

	for j in range(0, (N + 1)):
		summ += m.exp(- h * omega * beta * (j + 0.5))

	return summ

def _vibrational_energy(vibrational_partition_function, temperatures):
	vibrational_energy = []

	for i in range(0, (len(temperatures) - 1)):
		vibrational_energy.append(k * temperatures[i]**2 * (m.log(vibrational_partition_function[i + 1]) - m.log(vibrational_partition_function[i])) / (temperatures[i + 1] - temperatures[i]))

	return vibrational_energy

# def _vibrational_energy(temperature):
# 	beta = 1 / (k * temperature)
# 	return .5 * h * omega - h * omega * N * m.exp(- h * omega* beta * N) + h * omega * m.exp(- h * omega * beta) * \
# 	 	   (1 - m.exp(- h * omega * beta * N)) / (1 - m.exp(- h * omega * beta))

temp_start = 100
temp_end = 3000
dtemp = 0.1

temperatures = np.arange(temp_start, temp_end, dtemp)
vibrational_partition_function = [_vibrational_partition_function(temperature) for temperature in temperatures]
vibrational_energy = _vibrational_energy(vibrational_partition_function, temperatures)

plt.figure(figsize = (6, 8))
plt.plot(temperatures[0 : (len(temperatures) - 1)], vibrational_energy)
plt.show()