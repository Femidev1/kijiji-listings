FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Use Gunicorn to serve Flask app
CMD ["gunicorn", "-b", "0.0.0.0:5000", "backend.server:app"]