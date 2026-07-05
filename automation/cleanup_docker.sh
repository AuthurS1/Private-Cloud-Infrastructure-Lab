#!/bin/bash

echo "===== CLEANUP ====="

docker system prune -f
docker image prune -f
docker volume prune -f


