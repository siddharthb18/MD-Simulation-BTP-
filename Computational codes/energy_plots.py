import matplotlib.pyplot as plt

# Initialize lists to store data
time = []
temperature = []
potential_energy = []
total_energy = []

# Read data from the text file
with open('C:/415/BTP/160K/energies10.txt', 'r') as file:
    for line in file:
        columns = line.split()
        time_step = int(columns[0])
        temperature_val = float(columns[1])
        potential_energy_val = float(columns[2])
        total_energy_val = float(columns[4])

        # Append data to respective lists
        time.append(time_step * 4 / 1000)
        temperature.append(temperature_val)
        potential_energy.append(potential_energy_val)
        total_energy.append(total_energy_val)

# Create subplots with a shared x-axis
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 8))

# Plot the data with different colors
ax1.plot(time, temperature, label='Temperature', color='blue')
ax2.plot(time, potential_energy, label='Potential Energy', color='green')
ax3.plot(time, total_energy, label='Total Energy', color='red')

# Add labels and legends
ax1.set_ylabel('Temperature')
ax2.set_ylabel('Potential Energy')
ax3.set_ylabel('Total Energy')
ax3.set_xlabel('Time (ps)')

# Show legends
ax1.legend()
ax2.legend()
ax3.legend()

# Show the plot
plt.show()
