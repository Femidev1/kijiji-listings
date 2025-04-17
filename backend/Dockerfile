FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy backend code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the scraper (modify as needed)
CMD ["python", "kijiji_scraper.py"]