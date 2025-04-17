FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Flask
EXPOSE 5000

# Start with gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "server:app"]