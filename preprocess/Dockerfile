# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install GDAL (needed for rasterio) and clean up to keep image small
RUN apt-get update && apt-get install -y \
    gdal-bin libgdal-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir rasterio numpy

# Copy the preprocessing script into the container
COPY preprocess.py .

# Set entrypoint to run the script
ENTRYPOINT ["python", "/app/preprocess.py"]
