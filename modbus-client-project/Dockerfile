# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the Modbus server listens on (default: 5020)
EXPOSE 5020

# Command to run the Python Modbus server
CMD ["python3", "modbus_client.py"]
