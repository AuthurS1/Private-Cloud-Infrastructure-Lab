#!/bin/bash

echo "============================"
echo " SERVER MONITOR AUTOMATION "
echo "============================"

echo "1) Build Docker Image"
echo "2) Deploy Docker"
echo "3) Restart Docker"
echo "4) Rollback"
echo "5) Cleanup"
echo "6) Logs"
echo "7) Status"
echo "8) Backup"
echo "9) Health Check"
echo "10) Update"

read -p "Select: " choice

case $choice in

1)
./automation/build_docker_image.sh
;;

2)
./automation/deploy_docker.sh
;;

3)
./automation/restart_docker.sh
;;

4)
./automation/rollback_docker.sh
;;

5)
./automation/cleanup_docker.sh
;;

6)
./automation/logs_docker.sh
;;

7)
./automation/status_docker.sh
;;

8)
./automation/backup_servermonitor.sh
;;

9)
./automation/healthcheck_HTTPCODE.sh
;;

10)
./automation/update.sh
;;

*)
echo "Invalid option"
;;

esac

