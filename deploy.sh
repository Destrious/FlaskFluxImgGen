#!/bin/bash

# Remove existing Docker container and images
docker container prune -f
docker image prune -f

# Build the Docker image
docker build --tag flask-img-gen .

# Tag the Docker image to Docker Account
docker image tag flask-img-gen destrious/flask-img-gen:latest

# Push the Docker image to Docker Hub
docker push destrious/flask-img-gen:latest

# Run the Docker image
docker run -it --env-file .env destrious/flask-img-gen
