FROM python:3.11

# Install system dependencies required by geopandas and psycopg2-binary
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    g++ \
    python3-dev \
    libgeos-dev \
    libproj-dev \
    proj-data \
    proj-bin \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

# Install dependencies
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Copy project
COPY ergetl ergetl/
COPY config.json config.json

ENTRYPOINT ["python3", "-m", "ergetl"]
