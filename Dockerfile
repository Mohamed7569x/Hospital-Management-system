# Use Python 3.12.2 image based on Debian Bullseye in its slim variant as the base image
FROM python:3.10-slim-bullseye

# Set an environment variable to unbuffer Python output, aiding in logging and debugging
ENV PYTHONBUFFERED=1

# Define an environment variable for the web service's port, commonly used in cloud services
ENV PORT 8080

# Set the working directory within the container to /app for any subsequent commands
WORKDIR /app

# Copy the entire current directory contents into the container at /app
COPY . /app/

# Install the necessary system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
    
# Upgrade pip to ensure we have the latest version for installing dependencies
RUN pip install --upgrade pip

# Install dependencies from the requirements.txt file to ensure our Python environment is ready
RUN pip install -r requirements.txt

# Set the command to run our web service using Gunicorn, binding it to 0.0.0.0 and the PORT environment variable
CMD gunicorn final_project.wsgi:application --bind 0.0.0.0:"${PORT}"

# Inform Docker that the container listens on the specified network port at runtime
EXPOSE ${PORT}

# Existing Dockerfile content ...

# Set the command to run migrations and then start the server
CMD python manage.py makemigrations && python manage.py migrate && gunicorn server.wsgi:application --bind 0.0.0.0:"${PORT}"

