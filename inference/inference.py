import rasterio
import numpy as np
import sys

input_file = sys.argv[1]
threshold = sys.argv[2]
output_file = sys.argv[3]

# Open NVDI file
with rasterio.open(input_file) as src:
    ndvi = src.read(1)
    profile = src.profile

# Compute mask
threshold = float(threshold)
classified = np.where(ndvi > threshold, 1, 0)

# Save make GeoTiff
profile.update(dtype=rasterio.uint8, count=1)
with rasterio.open(output_file, "w", **profile) as dst:
    dst.write(classified.astype(np.uint8), 1)
