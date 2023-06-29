#!/bin/bash

echo "Welcome to Project Basil!\n"

script_dir="$(cd "$(dirname "$0")" && pwd)"

python3 $script_dir/interactive.py

# CHECK IF ABOVE COMMAND EXITED WITH ERROR CODE
if [ $? -eq 1 ]; then
    echo "\nERROR: Exiting MIDAS..."
    exit 1
fi

echo "\nNow running MIDAS script..."

# Step 1
python3 $script_dir/MIDAS.py

# CHECK IF ABOVE COMMAND EXITED WITH ERROR CODE
if [ $? -eq 1 ]; then
    echo "\nERROR: Exiting MIDAS..."
    exit 1
fi

# Step 2
echo "\nBuilding your custom Docker Image..."
image_id=$(docker build -t my_image -f Dockerfile . | grep -o "Successfully built [0-9a-f]*" | awk '{print $3}')
echo "Image ID: $image_id"
# grep to get id, push int to snyk and run cmd

# Step 3
echo "\n Running SNYK analysis for your image..."
echo "Image ID: $image_id"

## Run snyk test
bash $script_dir/snyktest.sh $image_id


# Step 4
echo "\nRunning your Docker image..."
docker run my_image

# Step 5++ go here >>>
# docker push (here)

echo "\nMIDAS execution complete! Please feel free to leave us a constructive review.\n"
