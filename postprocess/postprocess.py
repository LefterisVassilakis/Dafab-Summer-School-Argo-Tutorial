import rasterio
import numpy as np
import matplotlib.pyplot as plt
import sys

# Input: classified TIFF from inference
input_file = sys.argv[1]
# Output: PNG plot
output_plot = sys.argv[2]

with rasterio.open(input_file) as src:
    classified = src.read(1)

# Compute statistics
vegetation_percent = (classified == 1).sum() / classified.size * 100
print(f"Vegetation covers {vegetation_percent:.2f}% of the patch")

# Plot
plt.imshow(classified, cmap='Greens', vmin=0, vmax=1)
plt.title(f"Vegetation map ({vegetation_percent:.2f}%)")
plt.colorbar(label='Class')
plt.savefig(output_plot)
plt.close()
print(f"Plot saved to {output_plot}")
