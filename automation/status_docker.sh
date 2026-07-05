#!/bin/bash

echo "===== DOCKER ====="

docker-compose ps

echo
echo "===== KUBERNETES ====="
sudo kubectl get pods

echo
sudo kubectl get svc

