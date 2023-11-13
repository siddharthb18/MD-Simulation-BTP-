import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 34, 100)  # Reduced the number of points
y = np.linspace(0, 34, 100)  # Reduced the number of points
X, Y = np.meshgrid(x, y)

k = 1.84799568
A = 0.238676

Z = (np.sin(k * X) + np.sin(k * Y)) * A

plt.contourf(X, Y, Z, cmap='viridis', levels=100)
plt.colorbar(label='Z(in angstrom)')
plt.xlabel('X(in angstrom)')
plt.ylabel('Y(in angstrom)')
plt.title('External potential U')
plt.show()
