import matplotlib.pyplot as plt

# Define solar spectrum data (AM 1.5 standard)
wavelength = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200]
intensity = [0.001, 0.003, 0.008, 0.022, 0.054, 0.108, 0.186, 0.244, 0.272, 0.248, 0.202, 0.155, 0.114, 0.082, 0.058, 0.040, 0.028, 0.020, 0.014]

# Define perovskite absorption ranges and matching colors
perovskite_labels = ["1.2 eV", "1.4 eV", "1.6 eV", "1.8 eV"]
absorption_ranges = [(300, 1030), (300, 880), (300, 730), (300, 690)]
colors = ['red', 'green', 'blue', 'purple']  # Assigning specific colors for clarity

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(wavelength, intensity, label='Solar Spectrum (AM 1.5)', color='black', linewidth=2)

for label, range, color in zip(perovskite_labels, absorption_ranges, colors):
    plt.axvspan(range[0], range[1], color=color, alpha=0.3, label=label)

plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity (a.u.)')
plt.title('Solar Spectrum and Perovskite Absorption Ranges')
plt.legend()
plt.grid(True)

# Display the plot with clearer color matching
plt.tight_layout()
plt.show()
