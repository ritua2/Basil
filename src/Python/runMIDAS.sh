#!/bin/bash

echo -e "\nWelcome to Project Basil!"

python ./interactive.py
echo -e "\nNow running MIDAS script..."

# Step 1
python3 MIDAS2.py

# Step 2
echo -e "\nBuilding your custom Docker Image..."
image_id=$(docker build -t my_image -f Dockerfile . | grep -o "Successfully built [0-9a-f]*" | awk '{print $3}')
echo -e "Image ID: $image_id"
# grep to get id, push int to snyk and run cmd

# Step 3
echo -e "\n Running SNYK analysis for your image..."
echo -e "Image ID: $image_id"
chmod +x snyktest.sh
./snyktest.sh $image_id


# Step 4
echo -e "\nRunning your Docker image..."
docker run my_image

# Step 5++ go here >>>
# docker push (here)

echo -e "\nMIDAS execution complete! Please feel free to leave us a constructive review.\n"
