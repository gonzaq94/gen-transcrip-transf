# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install the Python packages specified in requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Set the working directory in the container
WORKDIR /app

# Copy the app.py and src/ directory into the container
COPY app.py /app/
COPY src /app/

# Add the src directory to the PYTHONPATH
ENV PYTHONPATH=/app:/app/src

# Command to run your application (modify this as necessary)
CMD ["python", "app.py"]