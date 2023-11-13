import numpy as np

N = 90
T = 50001

x = np.zeros((N, T))
y = np.zeros((N, T))

with open('C:/415/BTP/280K/Trajectory90', 'r') as f:
    for t in range(T):
        for _ in range(9):
            next(f)

        for n in range(N):
            line = next(f)
            atom_data = line.strip().split()

            try:
                x_coord = float(atom_data[1])
                y_coord = float(atom_data[2])

                x[n, t] = x_coord
                y[n, t] = y_coord

            except IndexError:
                print(f"Incomplete atom data at timestep {t} for atom {n}")

output_file = 'C:/415/BTP/280K/output_coordinates90_280.txt'
with open(output_file, 'w') as output:
    for t in range(0, T, 100): 
        for n in range(N):
            output.write(f"{x[n, t]} ")
        output.write("\n")
    
    for t in range(0, T, 100): 
        for n in range(N):
            output.write(f"{y[n, t]} ")
        output.write("\n")

print(f"Data has been written to {output_file}")
