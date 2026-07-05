#!/bin/bash

echo "===== DEPLOY ====="

docker-compose down
docker-compose up -d
docker-compose ps


