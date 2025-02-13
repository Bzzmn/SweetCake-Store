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
# Use a temporary secret key just for collectstatic
ENV DJANGO_SECRET_KEY="temporary-key-for-collectstatic-only"
ENV DATABASE_URL="sqlite:///db.sqlite3"

# Collect static files
RUN DJANGO_SECRET_KEY="temporary-key-for-collectstatic-only" python manage.py collectstatic --noinput

# Expose port
EXPOSE ${PORT}

# Set runtime environment variables
ENV DJANGO_SETTINGS_MODULE=sweetcake.settings
ENV PYTHONUNBUFFERED=1

# Remove temporary environment variables
ENV DJANGO_SECRET_KEY=
ENV DATABASE_URL=

# Run migrations and start Gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn --bind 0.0.0.0:${PORT} sweetcake.wsgi:application"]
