#!/bin/bash

echo "===== BUILD IMAGE ====="
docker build -t server-monitor:v2 ..

echo "Done."
docker images | grep server-monitor

