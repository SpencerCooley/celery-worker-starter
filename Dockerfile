# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY ./app /app

# Install dependencies
RUN pip install -r /app/requirements.txt

# Set environment variables for Celery
ENV C_FORCE_ROOT="true"
ENV PYTHONUNBUFFERED="true"

# Expose the port used by Celery (adjust if needed)
EXPOSE 5672

# Command to run Celery worker
CMD celery -A tasks worker -l Info
