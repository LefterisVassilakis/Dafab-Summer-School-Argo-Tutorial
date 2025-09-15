import rasterio
import numpy as np
import matplotlib.pyplot as plt
import sys

ndvi_file = sys.argv[1]
vegetation_file = sys.argv[2]
output_plot = sys.argv[3]

# Read NDVI file
with rasterio.open(ndvi_file) as src:
    ndvi = src.read(1)

# Read vegetation mask
with rasterio.open(vegetation_file) as src:
    veg_mask = src.read(1)

# Compute percentage
veg_percent = (veg_mask == 1).sum() / veg_mask.size * 100
print(f"Vegetation covers {veg_percent:.2f}% of the patch")

# Plot
plt.imshow(ndvi, cmap='Greens', vmin=-0.1, vmax=1.0)
plt.title(f"Vegetation map ({veg_percent:.2f}%)")
plt.colorbar(label='NDVI')
plt.savefig(output_plot)
plt.close()
print(f"Plot saved to {output_plot}")
