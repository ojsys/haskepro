# Use the official Python image from the Docker Hub
FROM python:3.12.2-slim-bullseye

# Install curl
RUN apt-get update && apt-get install -y curl && apt-get clean

# Set an environment variable to unbuffer Python output aiding in logging and debugging
ENV PYTHONBUFFERED=1

# Define an environment variable for the web service's port
ENV PORT 8080

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app/

# Ensure pip is always the latest
RUN pip install --upgrade pip

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the application
CMD gunicorn haske_pro.wsgi:application --bind 0.0.0.0:"${PORT}" --timeout 300

# Inform Docker that the container listens on the speciified network port at runtime
EXPOSE ${PORT}

