import numpy as np
import math as m
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO)

omega = 2169.
h = 6.63 * 10**(-34)
c = 3 * 10**(10)
k = 1.38 * 10**(-23)
Na = 6.022 * 10**(23)
R = 8.314

mu = 12 * 16 / (12 + 16) * 1.66054 * 10**(-27) # reduced mass in kg
I = mu * (1.128 * 10**(-10))**2                # moment of inertia in kg * m^2
B_tilde = h / (8 * m.pi**2 * I * c)            # in cm^(-1)
print B_tilde

logging.info(k / (h * c))

theta_rot = B_tilde / 0.695                    # rotational temperature in K
print theta_rot

logging.info("rotational temperature: %s", theta_rot)

j_max = 3	

class Rotation(object):
	def __init__(self):
		logging.info("initializing rotation class")

	def _rotational_partition_function(self, temperature):
		j = 0
		summ = 0

		while (j < j_max):
			summ += (2 * j + 1) * m.exp(- theta_rot / temperature * j * (j + 1))
			j += 1

		return summ

	def _rotational_energy(self, temperatures, rot_part_list):
		
		rotational_energy = [] 

		for i in range(0, len(temperatures) - 1):
			x = k * temperatures[i]**2 * (m.log(rot_part_list[i + 1]) - m.log(rot_part_list[i])) / (temperatures[i + 1] - temperatures[i])
			rotational_energy.append(x)

		return rotational_energy

	def _rotational_capacity(self, temperatures, rotational_energy):

		rotational_capacity = []

		for i in range(0, len(rotational_energy) - 1):
			x = (rotational_energy[i + 1] - rotational_energy[i]) / (temperatures[i + 1] - temperatures[i])
			rotational_capacity.append(x)
		
		return rotational_capacity

rotation = Rotation()

temp_start = 1
temp_end = 10
dtemp = 0.1

# -------------------------------------------------------------
temperatures = np.arange(temp_start, temp_end, dtemp)
rot_part_list = [rotation._rotational_partition_function(temperature) for temperature in temperatures]
rotational_energy = rotation._rotational_energy(temperatures, rot_part_list)
rotational_capacity = rotation._rotational_capacity(temperatures, rotational_energy)
# -------------------------------------------------------------

# -------------------------------------------------------------
# ROTATIONAL PARTITION FUNCTION
plt.figure(figsize = (6, 8))
partition_function = [rotation._rotational_partition_function(temperature) for temperature in temperatures]
plt.plot(temperatures, partition_function)
#plt.show()
# -------------------------------------------------------------

# -------------------------------------------------------------
# ROTATIONAL ENERGY
plt.figure(figsize = (6, 8))
x = [temperatures[i] for i in range(0, len(temperatures) - 1)]
y = [rotational_energy[i] * Na / R for i in range(0, len(rotational_energy))]
plt.plot(x, y)
#plt.show()
# -------------------------------------------------------------

# -------------------------------------------------------------
# ROTATIONAL CAPACITY
plt.figure(figsize = (6, 8))
y = [rotational_capacity[i] * Na / R for i in range(0, len(rotational_capacity))]
x = [temperatures[i] / theta_rot for i in range(0, len(temperatures) - 2)]
plt.plot(x, y)
plt.plot(x, [1] * len(x), '-')
plt.plot(x, [1.05] * len(x), '-')
plt.show()
# -------------------------------------------------------------
