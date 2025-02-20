# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY src/requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY src/ /app/

# Copy the .env file to the container
COPY src/.env /app/

# Install necessary packages for PostgreSQL
RUN apt-get update && \
    apt-get install -y postgresql postgresql-contri

# Expose port 5432 for PostgreSQL
EXPOSE 5432

# Expose port 80 for the application
EXPOSE 80

# Define environment variable
ENV NAME World

# Run main.py when the container launches
CMD ["python", "main.py"]
