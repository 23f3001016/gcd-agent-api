# Base Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (Vercel uses 8080 internally)
EXPOSE 8080

# Start FastAPI app from main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

