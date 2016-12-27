import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pandas
import numpy as np
import math

class plot(object):
	def __init__(self, plt):
		self.plt = plt

		self.ax = self.plt.subplot(111)
		self.ax.spines["top"].set_visible(False)
		self.ax.spines["bottom"].set_visible(False)
		self.ax.spines["left"].set_visible(False)
		self.ax.spines["right"].set_visible(False)

		self.ax.get_xaxis().tick_bottom()
		self.ax.get_yaxis().tick_left()

	def _set_xlimiters(self, xlim_min, xlim_max):
		self.xlim_min = xlim_min
		self.xlim_max = xlim_max

		axes = self.plt.gca()
		axes.set_xlim([xlim_min, xlim_max])

	def _set_ylimeters(self, ylim_min, ylim_max):
		self.ylim_min = ylim_min
		self.ylim_max = ylim_max

		axes = self.plt.gca()
		axes.set_ylim([ylim_min, ylim_max])

	def _set_ticks(self):
		self.plt.xticks(fontsize = 14)
		self.plt.yticks(fontsize = 14)

	def _make_grid(self, xstep, ystep):
		#horizontal tick lines
		for y in np.arange(self.ylim_min, self.ylim_max + ystep, ystep):
			self.plt.plot(np.arange(self.xlim_min, self.xlim_max + xstep, xstep), [y] * len(np.arange(self.xlim_min, self.xlim_max + xstep, xstep)), 
			"--", color = "black", lw = 1, alpha = 0.7)

		# vertical tick lines
		for x in np.arange(self.xlim_min, self.xlim_max + xstep, xstep):
			self.plt.plot([x] * len(np.arange(self.ylim_min, self.ylim_max + ystep, ystep)), np.arange(self.ylim_min, self.ylim_max + ystep, ystep), 
				"--", color = "black", lw = 1, alpha = 0.7)

molar_mass1 = 78
molar_mass2 = 60
density1 = 0.874
density2 = 0.785

volume_fraction2 = [1. - 0.1 * i for i in range(0,10)]
molar_fraction_liquid = [1 / ((molar_mass1 * density2) / (molar_mass2 * density1 * val) + 1 - (molar_mass1 * density2) / \
						(molar_mass2 * density1)) for val in volume_fraction2]
molar_fraction_liquid.append(0)
print "molar_fraction_liquid: {0}".format(molar_fraction_liquid)

refraction_index_liquid = [1.5, 1.4879, 1.4728, 1.459, 1.4452, 1.4374, 1.4157, 1.41, 1.3971, 1.3881, 1.377]
refraction_index_gas = [1.498, 1.462, 1.4553, 1.4521, 1.4473, 1.4448, 1.4406, 1.4341, 1.4265, 1.4128, 1.3785]

m1, b1 = np.polyfit(molar_fraction_liquid, refraction_index_liquid, 1)

molar_fraction_gas = [(val - b1) / m1 for val in refraction_index_gas]

boiling_temperature = [81, 75.25, 72.25, 72.25, 72.25, 72.25, 72.5, 74, 76.25, 79, 82.5]

x_values = np.arange(0, 1, 0.01)
linearization1 = [x * m1 + b1 for x in x_values]

plt.figure(figsize = (6,8))
plt.plot(molar_fraction_liquid, refraction_index_liquid, '--', linewidth = 2)
plt.plot(molar_fraction_liquid, refraction_index_liquid, 'ro')
plt.plot(x_values, linearization1, '--', color = 'green', linewidth = 2)


plt.figure(figsize = (6,8))

plot1 = plot(plt)

plot1._set_xlimiters(0, 1)
plot1._set_ylimeters(71, 84)
plot1._make_grid(0.05, 1)

plt.plot(molar_fraction_liquid, boiling_temperature, '--', linewidth = 3, color = 'blue')
plt.plot(molar_fraction_gas, boiling_temperature, '--', linewidth = 3, color = 'green')
plt.plot(molar_fraction_liquid, boiling_temperature, 'ro')
plt.plot(molar_fraction_gas, boiling_temperature, 'ro')
plt.savefig('phase_diagram.png')
