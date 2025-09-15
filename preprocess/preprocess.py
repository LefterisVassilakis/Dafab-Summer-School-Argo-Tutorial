import rasterio
import numpy as np
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# Open the multi-band TIFF
with rasterio.open(input_file) as src:
    red = src.read(1).astype(float)
    try:
        nir = src.read(2).astype(float)
    except IndexError:
        print("Band 2 not found, using Red as NIR for tutorial")
        nir = red.copy()
    profile = src.profile

# Scale
red = red / 10000.0
nir = nir / 10000.0

# Compute NDVI
ndvi = (nir - red) / (nir + red + 1e-6)

# Save NDVI GeoTIFF
profile.update(dtype=rasterio.float32, count=1)
with rasterio.open(output_file, "w", **profile) as dst:
    dst.write(ndvi.astype(rasterio.float32), 1)

print(f"NDVI saved to {output_file}")
