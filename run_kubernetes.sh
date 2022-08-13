#!/usr/bin/env bash

# Step 1:
# This is your Docker ID/path
dockerpath="tahirsenpai/udacity-capstone:latest"

# Step 2
# Run the Docker Hub container with kubernetes
kubectl run udacity-capstone --image=$dockerpath --port=80

# Step 3:
# List kubernetes pods
kubectl get pods


# Step 4:
# Forward the container port to a host
kubectl port-forward udacity-capstone 80:80