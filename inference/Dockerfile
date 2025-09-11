FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y gdal-bin libgdal-dev && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir rasterio numpy
COPY inference.py /app/inference.py
ENTRYPOINT ["python", "/app/inference.py"]
