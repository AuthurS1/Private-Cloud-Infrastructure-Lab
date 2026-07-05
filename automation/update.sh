#!/bin/bash

./automation/build_docker_image.sh

./automation/deploy_docker.sh

./automation/healthcheck_HTTPCODE.sh

