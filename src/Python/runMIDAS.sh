#!/bin/bash

echo -e "\nWelcome to Project Basil!"
echo -e "\nNow running MIDAS script..."

# Step 1
python3 MIDAS2.py

# Step 2
echo -e "\nBuilding your custom Dockerfile..."
docker build -t my_image -f Dockerfile .

# Step 3
echo -e "\nRunning your Docker image..."
docker run my_image

# Step 4
echo -e "\nRunning SNYK deep analysis for your image..."
chmod +x snyktest.sh
# (make snyktest.sh accept the newly built image name)
./snyktest.sh

# Step 5++ go here >>>
# docker push (here)

echo -e "\nMIDAS execution complete! Please feel free to leave us a constructive review.\n"
