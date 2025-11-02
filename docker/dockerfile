# Create file: Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY devcontainer/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ ./src/
COPY examples/ ./examples/
COPY notebooks/ ./notebooks/

# Expose Jupyter port
EXPOSE 8888

# Default command
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]