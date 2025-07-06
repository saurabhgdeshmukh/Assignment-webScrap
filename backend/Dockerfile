# Use an official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy code and dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port Flask will run on
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
