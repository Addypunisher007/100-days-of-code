#!/bin/bash

echo "🚀 Starting CI/CD Pipeline..."

# Load docker permission fix (safe for scripts)
newgrp docker <<EONG

echo "📦 Building Docker Image..."
docker build -t my-flask-app .

echo "🧹 Cleaning old container if exists..."
docker stop myapp 2>/dev/null || true
docker rm myapp 2>/dev/null || true

echo "▶️ Running new container (safe port mapping)..."
docker run -d -p 5001:5000 --name myapp my-flask-app

sleep 3

echo "🧪 Running API Tests..."
python3 test_api.py

echo "📊 Checking container status..."
docker ps | grep myapp

echo "✅ Pipeline Completed Successfully!"
EONG