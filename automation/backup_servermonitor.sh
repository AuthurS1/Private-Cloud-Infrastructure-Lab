#!/bin/bash

DATE=$(date +"$F_%H-%M")

mkidr -p backup

tar -czf backup/server-monitor-$DATE.tar.gz .

echo "Backup created."

