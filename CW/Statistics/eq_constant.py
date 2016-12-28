import math as m
import numpy as np

Temperature = 298.15

h = 6.62607 * 10**(-34)
c = 2.99792 * 10**(10) # cm / s
k = 1.38 * 10**(-23)
R = 8.314

molar_volume = 22.4 * 10 **(-3)
amu = 1.66054 * 10**(-27)
molecule_mass_1 = 46 * amu # 1 -- no2
molecule_mass_2 = 92 * amu # 2 -- n2o4

avogadro_number = 6.022 * 10 **(23)

internal_energy = 53600

B1 = [0.416, 0.434, 8.072]
B2 = [0.078, 0.122, 0.217]

theta_rot1 = [h * c * val / k for val in B1]
theta_rot2 = [h * c * val / k for val in B2]

print "theta_rot1: {0}".format(theta_rot1)
print "theta_rot2: {0}".format(theta_rot2)

rotational_partition_function_1 = m.sqrt((m.pi * Temperature**3) / (theta_rot1[0] * theta_rot1[1] * theta_rot1[2])) / 2
rotational_partition_function_2 = m.sqrt((m.pi * Temperature**3) / (theta_rot2[0] * theta_rot2[1] * theta_rot2[2])) / 4

print "rotational_partition_function_1: {0}".format(rotational_partition_function_1)
print "rotational_partition_function_2: {0}".format(rotational_partition_function_2)

translational_partition_function_1 = molar_volume * (2 * m.pi * molecule_mass_1 * k * Temperature / h ** 2)**(1.5) / avogadro_number
translational_partition_function_2 = molar_volume * (2 * m.pi * molecule_mass_2 * k * Temperature / h ** 2)**(1.5) / avogadro_number

print "translational_partition_function_1: {0}".format(translational_partition_function_1)
print "translational_partition_function_2: {0}".format(translational_partition_function_2)

freq1 = [757, 1356, 1664]
freq2 = [79, 266, 270, 425, 482, 672, 751, 808, 1264, 1380, 1712, 1758]

vibrational_partition_function_el_1 = [1 / (1 - m.exp((- h * c * val) / (k * Temperature))) for val in freq1]
vibrational_partition_function_el_2 = [1 / (1 - m.exp((- h * c * val) / (k * Temperature))) for val in freq2]

vibrational_partition_function_1 = 1
for val in vibrational_partition_function_el_1:
	vibrational_partition_function_1 = val * vibrational_partition_function_1

vibrational_partition_function_2 = 1
for val in vibrational_partition_function_el_2:
	vibrational_partition_function_2 = val * vibrational_partition_function_2

print "vibrational_partition_function_1: {0}".format(vibrational_partition_function_1)
print "vibrational_partition_function_2: {0}".format(vibrational_partition_function_2)

Q1 = translational_partition_function_1 * vibrational_partition_function_1 * rotational_partition_function_1
Q2 = translational_partition_function_2 * vibrational_partition_function_2 * rotational_partition_function_2

print "Q1: {0}".format(Q1)
print "Q2: {0}".format(Q2)

Q1 = Q1 ** 2  #/ ((avogadro_number * molar_volume) ** 6)
Q2 = Q2       #/ ((avogadro_number * molar_volume) ** 3)

equilibrium_constant = Q1 / Q2 * m.exp(- internal_energy / (R * Temperature))

print "Equilibrium_constant: {0}".format(equilibrium_constant)



























