import numpy as np
import matplotlib.pyplot as plt
import math

theta_vib = 3120.86
k = 1.38 * 10**(-23)
Na = 6.022 * 10**(23)
R = 8.314

classical_limit = R

temperature = np.arange(100, 3000, 1)
heat_capacity = Na * k / 4 * ((theta_vib / temperature)**2) * (1 / (np.sinh(theta_vib / temperature / 2))**2)

plt.plot(temperature, heat_capacity)
plt.plot(temperature, [classical_limit * 0.8] * len(temperature), '--')
plt.plot(temperature, [classical_limit] * len(temperature))
plt.show()
