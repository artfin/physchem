import numpy as np
import math as m
import matplotlib.pyplot as plt

dE = 7824.0 * 1.986 * 10**(-23) # J

class Electron(object):
	def __init__(self, g):
		self.g = g

	def _electronic_energy(self, temperature):
		return (self.g * m.exp(-dE / (k * temperature)) * dE) / (1 + self.g * m.exp(- dE / (k * temperature)))

	def _electronic_capacity(self, temperature):
		return (self.g * dE**2 * m.exp( - 2 * dE  / (k * temperature)) / (k * temperature**2 * (1 + self.g * m.exp(- dE / (k * temperature))) ** 2))

# -------------------------------------------------------------
electron = Electron(1)
temperatures = np.arange(temp_start, temp_end, dtemp)
electronic_energy = [electron._electronic_energy(temperature) for temperature in temperatures]
electronic_capacity = [electron._electronic_capacity(temperature) for temperature in temperatures]
# -------------------------------------------------------------

# -------------------------------------------------------------
# ELECTRONIC ENERGY
plt.figure(figsize = (6, 8))
plt.plot(temperatures, electronic_energy)
plt.show()
# -------------------------------------------------------------

# -------------------------------------------------------------
# ELECTRONIC CAPACITY
plt.figure(figsize = (6,8))
plt.plot(temperatures, electronic_capacity)
plt.show()
# -------------------------------------------------------------



