import numpy as np
import math as m
import matplotlib.pyplot as plt

omega = 2 * 10**(5)
h = 6.63 * 10**(-34)
k = 1.38 * 10**(-23)
c = 3 * 10**(8)

temp_start = 10
temp_end = 20000
dtemp = 1

temperatures = np.arange(temp_start, temp_end, dtemp)

class Vibration(object):
	def __init__(self, N):
		self.N = N

	def _vibrational_energy(self, temperature):
		beta = 1 / (k * temperature)

		return (h * c * omega / 2 / k - h * c * omega * (m.exp(-h * c * omega * beta * (self.N + 1)) - m.exp(-h * c * omega * beta)) / \
			(1 - m.exp(-h * c * omega * beta)) / k)

	def _vibrational_capacity(self, vibrational_energy, temperatures):

		vibrational_capacity = []

		for i in range(0, (len(vibrational_energy) - 1)):
			vibrational_capacity.append((vibrational_energy[i + 1] - vibrational_energy[i]) / (temperatures[i + 1] - temperatures[i]))

		return vibrational_capacity

N_list = [2, 3, 5, 10, 15, 20, 50]

plt.figure(figsize = (6, 8))

for N in N_list:
	vibration = Vibration(N)
	
	vibrational_energy = [vibration._vibrational_energy(temperature) for temperature in temperatures]
	vibrational_capacity = vibration._vibrational_capacity(vibrational_energy, temperatures)

	plt.plot(temperatures[0 : (len(temperatures) - 1)], vibrational_capacity, '-')

plt.show()
