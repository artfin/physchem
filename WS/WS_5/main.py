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
d1 = 0.874
d2 = 0.785

phi2 = [1 - 0.1*i for i in range(0,10)]
print phi2
