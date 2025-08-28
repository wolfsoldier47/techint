#!/bin/bash

set -e

# Run tests
  # Go to backend directory

echo "Running tests..."
pytest

# Build Docker image
echo "Building Docker image..."
docker build -t myfastapiapp .

# Stop and remove any existing container
if [ $(docker ps -aq -f name=myfastapiapp) ]; then
    echo "Stopping and removing existing container..."
    docker stop myfastapiapp || true
    docker rm myfastapiapp || true
fi

# Run Docker container
echo "Running Docker container..."
docker run -d --name myfastapiapp -p 8000:8000 myfastapiapp

echo "Deployment complete. App is running on http://localhost:8000"
