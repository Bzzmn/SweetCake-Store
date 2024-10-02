# Use the official Python base image
FROM python:3.12.5-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose port
EXPOSE 8000

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=sweetcake.settings
ENV PYTHONUNBUFFERED=1
ENV DJANGO_DEBUG=False
ENV DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1 [::1]"
ENV USE_SES=False

# Run migrations and start server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]