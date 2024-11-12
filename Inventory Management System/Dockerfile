# Use an official Python runtime as a parent image (Python 3.11)
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port if needed in the future (optional for now)
EXPOSE 8000

# Run the main application script
CMD ["python", "main.py"]
