import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 34, 1000)
y = np.linspace(0, 34, 1000)
X, Y = np.meshgrid(x, y)

k = 1.84799568
A = 0.238676

Z = (np.sin(k * X) + np.sin(k * Y)) * A

minima_coordinates = []

tolerance = 0.0005

for i in range(len(x)):
    for j in range(len(y)):
        if abs(np.sin(k * x[i]) + 1) < tolerance and abs(np.sin(k * y[j]) + 1) < tolerance:
            minima_coordinates.append((x[i], y[j], Z[j, i]))

np.random.shuffle(minima_coordinates)

with open('minima_coordinates90.txt', 'w') as f:
    f.write('90')
    f.write('\n\n')
    i = 1
    for coord in minima_coordinates:
        f.write(f'\t {i} \t  1 \t {coord[0]} \t {coord[1]} \t {coord[2]}\n')
        i = i + 1 
        if(i == 91):
            break

print("Minima coordinates saved to 'minima_coordinate90.txt'")
