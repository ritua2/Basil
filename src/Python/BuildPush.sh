#!/bin/bash

DOCKER_USERNAME="enter username here"
DOCKER_PASSWORD="enter password / access token here"
DOCKER_REPO="repo_where_to_send/folder_name"
DOCKER_TAG="set docker tag"
PYTHON_SCRIPT="path to python script"

path to python install location $PYTHON_SCRIPT

docker build -t $DOCKER_REPO:$DOCKER_TAG .

echo "$DOCKER_PASSWORD" | docker login --username "$DOCKER_USERNAME" --password-stdin

docker push $DOCKER_REPO:$DOCKER_TAG

docker logout
