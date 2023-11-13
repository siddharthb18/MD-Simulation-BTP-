import numpy as np
import matplotlib.pyplot as plt

# Read the MSD values for 90 atoms
with open("C:/415/BTP/280K/msd_values90_280.txt", "r") as file:
    msd_values90 = [float(line.strip()) for line in file]

# Create time steps for the 90 atoms data
time_steps90 = np.arange(0, len(msd_values90) * 8, 8)

# Create a list of filenames for the other atom counts
filenames = ["msd_values90_280.txt", "msd_values70_280.txt", "msd_values50_280.txt", "msd_values30_280.txt", "msd_values10_280.txt"]

# Initialize an empty list to store the MSD values for different atom counts
msd_values_list = []

# Initialize a list to store the average slopes
average_slopes = []

# Initialize a list of atom counts for labels
atom_counts = [90, 70, 50, 30, 10]

# Create a figure
plt.figure(figsize=(8, 6))

# Read and store MSD values for different atom counts, including 90 atoms
for count, filename in zip(atom_counts, filenames):
    with open(f"C:/415/BTP/280K/{filename}", "r") as file:
        msd_values = [float(line.strip()) for line in file]
    msd_values_list.append(msd_values)

    # Create time steps for the current atom count data
    time_steps = np.arange(0, len(msd_values) * 8, 8)

    # Plot MSD values for the current atom count
    plt.plot(time_steps, msd_values, label=f"{count} atoms")
    
    # Calculate the differences between consecutive MSD values
    differences = [msd_values[j] - msd_values[j-1] for j in range(1, len(msd_values))]

    # Calculate the average slope
    average_slope = sum(differences) / len(differences)
    
    # Append the average slope to the list
    average_slopes.append(average_slope)

# Set plot labels and title
plt.title("MSD Values Over Time for Different Atom Counts")
plt.xlabel("Time(in ps)")
plt.ylabel("MSD Value(in angstrom^2)")
plt.grid(True)

# Add a legend to the plot
plt.legend()

# Show the plot
plt.show()

# Print the average slopes
print("Average Slopes:")
for i, slope in enumerate(average_slopes):
    print(f"{atom_counts[i]} atoms: {slope}")
