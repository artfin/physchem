import math as m
import numpy as np
import matplotlib.pyplot as plt

import codecs

def _read_file(number):
	name = str(number) + '.txt' 

	with codecs.open(name, mode = 'r', encoding = 'utf-8') as inputfile:
		data = inputfile.readlines()

	time = []
	temperature = []

	for line in data:
		elements = line.split()
		time.append(float(elements[0]))
		temperature.append(float(elements[1]))

	return time, temperature

plt.figure(figsize = (6,8))

for i in range(0, 4, 1):
	time, temperature = _read_file(i)

	for i in range(1, (len(temperature) - 1)):
		if temperature[i - 1] - temperature[i] > 0 and temperature[i + 1] - temperature[i] > 0:
			plt.plot(time[i], temperature[i], 'ro')

	plt.plot(time, temperature, '--')

plt.savefig('curves.png')









