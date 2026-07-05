#!/bin/bash

echo "===== ROLLBACK ====="

docker tag server-monitor:v1 server-monitor:v2
docker-compose up -d
docker-compose ps


