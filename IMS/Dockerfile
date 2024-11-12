# Dockerfile
FROM python:3.10-slim

# Install bcrypt dependencies
RUN apt-get update && apt-get install -y build-essential libffi-dev

# Set up working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Run the app
CMD ["python", "main.py"]
