#!/bin/bash

# Load Docker Images into Minikube
# This script loads all built images into the Minikube cluster

set -e

echo "🚀 Loading Docker images into Minikube..."

# Define services and their image names
declare -A services=(
    ["auth-service"]="auth-service:latest"
    ["user-service"]="user-service:latest"
    ["book-service"]="book-service:latest"
    ["review-service"]="review-service:latest"
    ["cart-service"]="cart-service:latest"
    ["order-service"]="order-service:latest"
    ["payment-service"]="payment-service:latest"
    ["notification-service"]="notification-service:latest"
    ["frontend-service"]="frontend-service:latest"
)

# Check if Minikube is running
if ! minikube status | grep -q "Running"; then
    echo "❌ Minikube is not running. Please start Minikube first:"
    echo "   minikube start"
    exit 1
fi

# Load each image into Minikube
for image in "${services[@]}"; do
    echo ""
    echo "📦 Loading $image into Minikube..."
    
    if docker images | grep -q "$(echo $image | cut -d: -f1)"; then
        minikube image load "$image"
        echo "✅ Successfully loaded $image"
    else
        echo "❌ Image $image not found locally!"
        echo "   Please run ./build-images.sh first"
        exit 1
    fi
done

echo ""
echo "🎉 All images loaded into Minikube successfully!"
echo ""
echo "📋 Loaded images:"
for image in "${services[@]}"; do
    echo "   - $image"
done

echo ""
echo "💡 To verify images in Minikube, run:"
echo "   minikube image ls"
