FROM python:3.11-slim
WORKDIR /app

RUN apt-get update && apt-get install -y libgdal-dev gdal-bin && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir rasterio numpy matplotlib

COPY postprocess.py /app/postprocess.py
ENTRYPOINT ["python", "/app/postprocess.py"]
