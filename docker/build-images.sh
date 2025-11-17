#!/bin/bash

# Build Docker Images for Microservices Application
# This script builds all required Docker images for the Kubernetes deployment

set -e

echo "🔨 Building Docker images for microservices application..."

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

# Build each service image
for service in "${!services[@]}"; do
    image_name="${services[$service]}"
    echo ""
    echo "📦 Building $image_name..."
    
    if [ -d "$service" ]; then
        docker build -t "$image_name" "./$service"
        echo "✅ Successfully built $image_name"
    else
        echo "❌ Service directory $service not found!"
        exit 1
    fi
done

echo ""
echo "🎉 All Docker images built successfully!"
echo ""
echo "📋 Built images:"
for image in "${services[@]}"; do
    echo "   - $image"
done

echo ""
echo "💡 To load images into Minikube, run:"
echo "   ./load-images-minikube.sh"
