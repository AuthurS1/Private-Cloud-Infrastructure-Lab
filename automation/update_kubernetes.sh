#!/bin/bash

set -e

echo "Build image..."

docker build -t server-monitor:v2 .

echo ""
echo "Import image.."
sudo k3s ctr images import <(docker save server-monitor:v2)

echo ""
echo "Restart deployment..."

kubectl rollout restart deployment/server-monitor
kubectl rollout status deployment/server-monitor

echo ""

kubectl get pods

