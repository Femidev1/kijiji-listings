FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all backend files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask server
EXPOSE 5000

# Run the Flask API instead of scraper
CMD ["python", "backend/server.py"]