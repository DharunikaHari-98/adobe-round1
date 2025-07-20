# Base image with platform specified for AMD64
FROM --platform=linux/amd64 python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory
COPY app ./app

# Command to run the extractor
CMD ["python", "app/main.py"]
