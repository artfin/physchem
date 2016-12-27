#-*- coding: utf-8 -*-

import math as m
import numpy as np

import matplotlib.pyplot as plt

g = 2.595
t_dead = 0.33
temperatures = [323., 328., 333., 338., 343.]
flux = 20
room_temperature = 294
R = 8.314

mean_times = [1.820, 1.557, 1.350, 1.180, 1.040]

volume = [(mean_times[i] - t_dead) / (g * flux * temperatures[i] * room_temperature) for i in range(len(temperatures))]
volume_log = [m.log(val, m.exp(1)) for val in volume]
volume_RT_log = [m.log(volume[i] * R / temperatures[i]) for i in range(len(temperatures))]

inverse_temperatures = [1 / temperature for temperature in temperatures]

m1, b1 = np.polyfit(inverse_temperatures, volume_log, 1)
print "Дифференциальная теплота сорбции q: {0}".format(m1)

m2, b2 = np.polyfit(inverse_temperatures, volume_RT_log, 1)
print "Изостерическая теплота адсорбции q_st: {0}".format(m2)

plt.figure(figsize = (6,8))
plt.plot(inverse_temperatures, volume_log, '--', linewidth = 2)
plt.plot(inverse_temperatures, volume_log, 'ro')
#plt.show()
