import numpy as np
import math as m
import matplotlib.pyplot as plt

h = 6.63 * 10**(-34)
c = 3 * 10**(10)
k = 1.38 * 10**(-23)
Na = 6.022 * 10**(23)
R = 8.314

dE = 7824.0 * 1.986 * 10**(-23) # J

temp_start = 1
temp_end = 20000
dtemp = 2

class Electron(object):
	def __init__(self, g):
		self.g = g

	def _electronic_energy(self, temperature):
		return (self.g * m.exp(-dE / (k * temperature)) * dE) / (1 + self.g * m.exp(- dE / (k * temperature)))

	def _electronic_capacity(self, temperature):
		return (self.g * dE**2 * m.exp( - dE  / (k * temperature)) / (k * temperature**2 * (1 + self.g * m.exp(- dE / (k * temperature))) ** 2))

	def _electronic_capacity_derivative(self, electronic_capacity, temperatures):
		electronic_capacity_derivative = []

		for i in range(0, len(electronic_capacity) - 1):
			electronic_capacity_derivative.append((electronic_capacity[i+1] - electronic_capacity[i]) / (temperatures[i+1] - temperatures[i]))

		return electronic_capacity_derivative

	def _find_maximum_capacity(self, electronic_capacity, temperatures):
		maximum = max(electronic_capacity)
		temperature = temperatures[electronic_capacity.index(maximum)]
		return [temperature, maximum]

# -------------------------------------------------------------
#0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 
# glist = [1, 10, 100, 1000, 10000]

# electrons = []
# temperatures = np.arange(temp_start, temp_end, dtemp)

# electronic_capacity = []
# counter = 0

# for g in glist:
# 	electron = Electron(g)
# 	electrons.append(electron)

# 	electronic_energy = [electrons[counter]._electronic_energy(temperature) for temperature in temperatures]
# 	electronic_capacity.append([electrons[counter]._electronic_capacity(temperature) for temperature in temperatures])

# 	counter += 1
#maximum = electron._find_maximum_capacity(electronic_capacity, temperatures)
# -------------------------------------------------------------

# -------------------------------------------------------------
# ELECTRONIC ENERGY
# plt.figure(figsize = (6, 8))
# plt.plot(temperatures, electronic_energy)
# plt.show()
# -------------------------------------------------------------

# -------------------------------------------------------------
#ELECTRONIC CAPACITY
# plt.figure(figsize = (6,8))
# for counter in range(0, len(glist)):
# 	plt.plot(temperatures, electronic_capacity[counter])

# plt.show()
# -------------------------------------------------------------


# -------------------------------------------------------------
temperatures = np.arange(temp_start, temp_end, dtemp)

max_temperature = []
glist = [0.01, 0.1, 1, 10, 100]

for g in glist:
	electron = Electron(g)
	electronic_energy = [electron._electronic_energy(temperature) for temperature in temperatures]
	electronic_capacity = [electron._electronic_capacity(temperature) for temperature in temperatures]
	maximum = electron._find_maximum_capacity(electronic_capacity, temperatures)
	max_temperature.append(maximum[0])
# -------------------------------------------------------------

# -------------------------------------------------------------
# # TEMPERATURE IN MAXIMUM FROM G
plt.figure(figsize = (6,8))
plt.scatter(glist, max_temperature)
plt.show()
# -------------------------------------------------------------
