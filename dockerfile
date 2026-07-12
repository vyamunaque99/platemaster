# Stage 1: Base Python build stage
FROM python:3.10.12-slim AS python-builder
 
# Create the app directory
RUN mkdir /app
 
# Set the working directory
WORKDIR /app
 
# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
 
# Upgrade pip and install dependencies
RUN pip install --upgrade pip 
 
# Copy the requirements file first (better caching)
COPY requirements.txt /app/
 
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production stage
FROM python:3.10.12-slim

RUN useradd -m -r appuser && \
   mkdir /app && \
   chown -R appuser /app
 
# Copy the Python dependencies from the python-builder stage
COPY --from=python-builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=python-builder /usr/local/bin/ /usr/local/bin/

# Install tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr tesseract-ocr-spa

# Set the working directory
WORKDIR /app

# Copy application code
COPY --chown=appuser:appuser . .

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# Copy entrypoint script into the image
COPY ./entrypoint.sh /entrypoint.sh

# Make the script executable
RUN chmod +x /entrypoint.sh

# Switch to non-root user
USER appuser
 
# Expose the Django port
EXPOSE 8000

# Start the application using Gunicorn
ENTRYPOINT ["/app/entrypoint.sh"]