# Use the official Python base image
FROM python:3.12.5-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set build-time arguments with default values (no sensitive data)
ARG PORT=8000
ARG DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1 [::1]"

# Set environment variables for build time
ENV PORT=${PORT}
ENV DJANGO_ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS}
ENV DJANGO_DEBUG=False
ENV DJANGO_SETTINGS_MODULE=sweetcake.settings
ENV PYTHONUNBUFFERED=1

# Collect static files with minimal environment
RUN python manage.py collectstatic --noinput \
    --settings=sweetcake.settings \
    DJANGO_SECRET_KEY=dummy-key-for-build \
    DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1 [::1]" \
    DATABASE_URL=sqlite:///db.sqlite3

# Expose port
EXPOSE ${PORT}

# Run migrations and start Gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn --bind 0.0.0.0:${PORT} sweetcake.wsgi:application"]
