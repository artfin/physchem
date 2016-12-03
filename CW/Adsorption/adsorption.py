# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pandas
import numpy as np
import math

fontsize = 14
tableau20 = [(31, 119, 180), (199, 21, 133),(255, 127, 80)]

for i in range(len(tableau20)):
	r, g, b = tableau20[i]
	tableau20[i] = (r / 255., g / 255., b / 255.)

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

molar_mass = 78
density = 0.879
sigma = 28.88 * math.pow(10, -7)
R = 8.314
Temp = 293
molar_volume = molar_mass / density 

adsorption = [0.444, 0.655, 0.806, 0.83, 0.89, 1.09, 1.17, 1.43, 1.62,
	 1.71, 1.88, 2.08, 2.35, 2.43, 2.93, 3.35, 4.31, 4.90, 9.00,
	 17.20, 18.80, 19.00, 19.05, 19.20]

adsorption_pressures = [0.0563, 0.108, 0.161, 0.191, 0.216, 0.287, 0.330,
			 0.479, 0.551, 0.573, 0.634, 0.660, 0.714, 0.734,
			 0.763, 0.782, 0.808, 0.826, 0.846, 0.882, 0.908,
			 0.942, 0.966, 0.999]

desorption = [18.98, 18.78, 18.75, 18.70, 18.18, 17.65, 14.69, 
			  7.14, 3.60, 2.67, 2.11, 1.91, 1.77]

desorption_pressures = [0.948, 0.880, 0.876, 0.852, 0.839, 0.832,
						0.810, 0.770, 0.724, 0.686, 0.646, 0.610,
						0.585]

volume_pores_ads = [math.pow(10,-3) * molar_mass * adsorption[i] for i in range(0, len(adsorption))]

volume_pores_des = []
for num in reversed(desorption):
	volume_pores_des.append(math.pow(10,-3)*molar_mass*num)

radius_ads = [-2*sigma*molar_volume/(R*Temp*math.log(adsorption_pressures[i])) for i in range(0, len(adsorption_pressures))]
radius_des = [-2*sigma*molar_volume/(R*Temp*math.log(desorption_pressures[i])) for i in range(0, len(desorption_pressures))]

radius_ads_average = [(radius_ads[i] + radius_ads[i+1])/2 for i in range(0, len(radius_ads)-1)]
radius_des_average = [(radius_des[i] + radius_des[i+1])/2 for i in range(0, len(radius_des)-1)]

delta_adsorption = [adsorption[i] - adsorption[i+1] for i in range(0, len(adsorption)-1)]
delta_desorption = [desorption[i] - desorption[i+1] for i in range(0, len(desorption)-1)]

# --------------------------------------------------------------------------------------

plt.figure(figsize = (12, 16))

plot1 = plot(plt)

plot1._set_xlimiters(0, 1)
plot1._set_ylimeters(0, 20)
plot1._make_grid(0.05, 1)

plot1.plt.plot(adsorption_pressures, adsorption, lw = 2.5, label = "Adsorption", color = tableau20[0])
plot1.plt.plot(desorption_pressures, desorption, lw = 2.5, label = "Desorption", color = tableau20[1])
plot1.plt.plot(adsorption_pressures, adsorption, 'ro')
plot1.plt.plot(desorption_pressures, desorption, 'ro')

plot1.plt.xlabel('p/ps', fontsize = fontsize)
plot1.plt.ylabel('Adsorption', fontsize = fontsize)
plot1.plt.title('Adsorption hysteresis', fontsize = fontsize)

patch1 = mpatches.Patch(color = tableau20[0], label = "Adsorption")
patch2 = mpatches.Patch(color = tableau20[1], label = "Desorption")
plot1.plt.legend(handles = [patch1, patch2], bbox_to_anchor=(0.05, 0.95), 
		   loc=2, borderaxespad=0., prop = {'size' : 20})

plot1.plt.savefig('hysteresis.png')
# -----------------------------------------------------------------------------------

plt.figure(2, figsize = (12, 16))

plot2 = plot(plt)

plot2._set_xlimiters(0, 1)
plot2._set_ylimeters(0, 1.75)
plot2._make_grid(0.1, 0.2)

plot2.plt.plot(desorption_pressures, volume_pores_des, lw = 2.5, color = tableau20[1])
plot2.plt.plot(desorption_pressures, volume_pores_des, 'ro')

plot2.plt.xlabel('p/ps', fontsize = fontsize)
plot2.plt.ylabel('Retained volume', fontsize = fontsize)

plot2.plt.plot(adsorption_pressures, volume_pores_ads, lw = 2.5, color = tableau20[2])
plot2.plt.plot(adsorption_pressures, volume_pores_ads, 'ro')

patch1 = mpatches.Patch(color = tableau20[1], label = "Desorption")
patch2 = mpatches.Patch(color = tableau20[2], label = "Adsorption")
plot2.plt.legend(handles = [patch1, patch2], bbox_to_anchor = (0.05, 0.95),
		loc = 2, borderaxespad=0., prop = {'size' : 20})

plot2.plt.savefig('RetainedVolume.png')
# -------------------------------------------------------------------------------------

plt.figure(3, figsize = (12, 16))

plot3 = plot(plt)

plot3._set_xlimiters(0, 5 * math.pow(10,-6))
plot3._set_ylimeters(-10, 10)
plot3._make_grid(5*math.pow(10,-7), 1)

delta_adsorption_minus = [-delta_adsorption[i] for i in range(0, len(delta_adsorption))]

plot3.plt.plot(radius_des_average, delta_desorption, lw = 2.5, color = tableau20[1])
plot3.plt.plot(radius_ads_average, delta_adsorption_minus, lw = 2.5, color = tableau20[2])
plot3.plt.plot(radius_des_average, delta_desorption, 'ro')
plot3.plt.plot(radius_ads_average, delta_adsorption_minus, 'ro')

plot3.plt.xlabel('Pore radius', fontsize = fontsize)
plot3.plt.ylabel('Adsorption delta', fontsize = fontsize)
plot3.plt.title('Differential distribution curve', fontsize = fontsize)

patch1 = mpatches.Patch(color = tableau20[1], label = "Desorption")
patch2 = mpatches.Patch(color = tableau20[2], label = "Adsorption")
plot3.plt.legend(handles = [patch1, patch2], bbox_to_anchor = (0.70, 0.95),
		loc = 2, borderaxespad = 0., prop = {'size' : 20})

plot3.plt.savefig('DDC.png')