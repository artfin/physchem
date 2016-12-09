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

theta_rot = B_tilde / 0.695                    # rotational temperature in K
logging.info("rotational temperature: %s", theta_rot)

j_max = 10

class Rotation(object):
	def __init__(self):
		logging.info("initializing rotation class")

	def _rotational_partition_function(self, temperature):

		abs_change = 10**(-1)
		summ = [0, 1]
		j = 1

		while (abs(summ[0] - summ[1]) > abs_change and j < j_max):
			interim = summ[1]
			summ[1] = summ[0] + (2 * j + 1) * m.exp(- theta_rot / temperature * j * (j + 1))
			summ[0] = interim
			j += 1

		return summ[1]

	def _rotational_energy(self, temperatures, rot_part_list):
		
		abs_change = 2 * 10**(-22)
		rotational_energy = [] 

		for i in range(0, len(temperatures) - 1):
			x = k * temperatures[i] * (rot_part_list[i + 1] - rot_part_list[i]) / (temperatures[i + 1] - temperatures[i])
			
			if (len(rotational_energy) > 0):
				if (abs(x - rotational_energy[-1]) < abs_change):
					rotational_energy.append(x)
				else:
					rotational_energy.append(rotational_energy[-1])
			else:
				rotational_energy.append(x)

		return rotational_energy

	def _rotational_capacity(self, temperatures, rotational_energy):
		abs_change = 5 * 10**(-26)
		rotational_capacity = []

		for i in range(0, len(rotational_energy) - 1):
			x = (rotational_energy[i + 1] - rotational_energy[i]) / (temperatures[i + 1] - temperatures[i])

			if (len(rotational_capacity) > 0):
				if (abs(x - rotational_capacity[-1]) < abs_change):
					rotational_capacity.append(x)
				else:
					rotational_capacity.append(rotational_capacity[-1])
			else:
				rotational_capacity.append(x)
		
		return rotational_capacity

rotation = Rotation()

temp_start = 50
temp_end = 1000
dtemp = 0.01

temperatures = np.arange(temp_start, temp_end, dtemp)
rot_part_list = [rotation._rotational_partition_function(temperature) for temperature in temperatures]
rotational_energy = rotation._rotational_energy(temperatures, rot_part_list)
rotational_capacity = rotation._rotational_capacity(temperatures, rotational_energy)

# -------------------------------------------------------------
# ROTATIONAL PARTITION FUNCTION
#plt.figure(figsize = (12, 16))
#plot1 = plot(plt)
#plot1.plt.plot(temperatures, rot_part_list)
#plot1.plt.show()
# -------------------------------------------------------------

# -------------------------------------------------------------
# ROTATIONAL ENERGY
plt.figure(figsize = (6, 8))

x = [temperatures[i] for i in range(0, len(temperatures) - 1)]
y = [rotational_energy[i] * Na / R for i in range(0, len(rotational_energy))]

plt.plot(x, y)
plt.plot([1.5] * (temp_end - temp_start), '-')
plt.show()
# -------------------------------------------------------------

# -------------------------------------------------------------
# ROTATIONAL CAPACITY
plt.figure(figsize = (6, 8))

y = [rotational_capacity[i] * Na / R for i in range(0, len(rotational_capacity))]
x = [temperatures[i] / theta_rot for i in range(0, len(temperatures) - 2)]

plt.plot(x, y)
plt.show()
# -------------------------------------------------------------
