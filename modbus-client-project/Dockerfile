# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local project files to the container
COPY . .

# Install dependencies
RUN pip install pymodbus

# Command to run the Python Modbus client script
CMD ["python3", "modbus_client.py"]

