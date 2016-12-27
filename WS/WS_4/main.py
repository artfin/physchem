# -*- coding: utf-8 -*-

import math as m
import numpy as np
import matplotlib.pyplot as plt

R = 8.314
molar_mass = 74 # диэтиловый эфир

temperatures1 = [23., 26., 29., 32., 35., 38., 41., 44.]
temperatures1 = [temperature + 273 for temperature in temperatures1]
p1_left = [428, 442, 455, 470, 488, 507, 528, 553]
p1_right = [249, 237, 225, 213, 196, 177, 160, 132]
p1_delta = [p1_left[i] - p1_right[i] for i in range(len(p1_left))]
print "p1_delta: {0}".format(p1_delta)

temperatures2 = [41., 39.5, 36.5, 33.5, 30.5, 27.5, 24.5]
temperatures2 = [temperature + 273 for temperature in temperatures2]
p2_left = [531, 519, 497, 478, 462, 445, 433]
p2_right = [157, 168, 188, 205, 219, 235, 246]
p2_delta = [p2_left[i] - p2_right[i] for i in range(len(p2_left))]
print "p2_delta_reversed: {0}".format(p2_delta[::-1])

temperatures = sorted(temperatures1 + temperatures2, reverse = True) 
delta_p = sorted(p1_delta + p2_delta, reverse = False)
print "delta_p: {0}".format(delta_p)

delta_p_log = [m.log(val, m.exp(1)) for val in delta_p]
inverse_temperatures = [1 / temperature for temperature in temperatures]

print "inverse_temperatures: {0}".format(inverse_temperatures)
print "delta_p_log: {0}".format(delta_p_log)

m1, b1 = np.polyfit(inverse_temperatures, delta_p_log, 1)
print "m1: {0}; b1: {1}".format(m1, b1)

delta_H_v = R * m1
print "Энтальпия испарения: {0} (Дж / моль)".format(delta_H_v)

T_normal = m1 / (- b1 + m.log(760, m.exp(1)))
print "Нормальная температура кипения: {0} (К)".format(T_normal)

delta_S_v = delta_H_v / T_normal
print "Изменение энтропии: {0} (Дж / моль / К)".format(delta_S_v)

E = 0.002 * T_normal ** 2 * molar_mass / delta_H_v

print "Эбуллиоскопическая константа: {0} (К * кг / моль)".format(E) 

x_values = np.arange(0.00313, 0.00345, 0.00005)

plt.figure(figsize = (6,8))
plt.plot(inverse_temperatures, delta_p_log, '--', color = 'blue')
plt.plot(inverse_temperatures, delta_p_log, 'ro')
plt.plot(x_values, m1 * x_values + b1, '--', linewidth = 2, color = 'green')
plt.savefig("graph.png")

