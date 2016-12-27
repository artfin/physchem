import math as m
import numpy as np
import matplotlib.pyplot as plt

dead_time = 0.31

g = 2.379 # g
Temperature = 353. # K
F = 25.0 # cm^3 / min
R = 8.314

density = 0.87 # g / cm^3
molar_mass = 78

volume = [1, 2, 3, 4, 5, 6, 7, 8]
m = [vol * density * 1000 / molar_mass for vol in volume]

retention_time = [8.24, 3.03, 2.84, 2.75, 2.65, 2.61, 2.57, 2.51]

h = [69.111, 129.271, 212.401, 268.092, 332.341, 364.274, 406.677, 454.034]

S = [46.7757, 89.1549, 152.7152, 199.7581, 251.0490, 293.4332, 339.9819, 395.5551]
S1 = [35.3959, 65.8851, 114.2126, 145.2935, 183.5105, 212.9472, 248.6489, 286.9172]
S3 = [retention_time[i] * h[i] for i in range(len(retention_time))]
S_ads = [S1[i] + S3[i] for i in range(len(retention_time))]

adsorption = [m[i] * S_ads[i] / g / S[i] for i in range(len(volume))][1 : len(volume)]
pressure = [m[i] * h[i] * R * Temperature/ S[i] / F for i in range(len(volume))][1 : len(volume)]

plt.figure(figsize = (6,8))
plt.plot(pressure, adsorption, '--')
plt.savefig('isotherm.png')













