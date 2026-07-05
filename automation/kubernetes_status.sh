#!/bin/bash

echo "Docker"

docker ps

echo ""
echo "Pods"

kubectl get pods -o wide

echo ""
echo "Services"

kubectl get svc

echo ""
echo "Ingress"

kubectl get ingress

echo ""
echo "Nodes"

kubectl get nodes

