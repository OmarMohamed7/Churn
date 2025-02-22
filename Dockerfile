# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for Fly.io
EXPOSE 8080

# Run the Dash app
CMD ["gunicorn", "-b", "0.0.0.0:8080", "dashboard:server"]
