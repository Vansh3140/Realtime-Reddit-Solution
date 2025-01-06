# Use Python 3.9 slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libnss3 \
    libnspr4 \
    libdbus-1-3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libx11-6 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libdrm2 \
    libxcb1 \
    libxkbcommon0 \
    libpango-1.0-0 \
    libcairo2 \
    libasound2 \
    libatspi2.0-0


# Install other dependencies from requirements.txt
RUN pip install --no-cache-dir --use-deprecated=legacy-resolver -r requirements.txt

# Install hrequests with all extras and run its setup
RUN pip install --no-cache-dir -U hrequests==0.8.0 && \
    python -m hrequests install

# Copy the rest of the application
COPY . .

# Dynamic port binding for Render
ENV PORT=5000

# Set the entrypoint command or script
ENTRYPOINT ["python3", "server.py"]
