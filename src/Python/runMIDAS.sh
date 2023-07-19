#!/bin/bash

echo "Welcome to Project Basil!\n"

script_dir="$(cd "$(dirname "$0")" && pwd)"

python3 $script_dir/interactive.py

# CHECK IF ABOVE COMMAND EXITED WITH ERROR CODE
if [ $? -eq 1 ]; then
    echo "\nERROR: Exiting MIDAS..."
    exit 1
fi

echo "\nGenerating Dockerfile..."

# Step 1
python3 $script_dir/MIDAS.py

# CHECK IF ABOVE COMMAND EXITED WITH ERROR CODE
if [ $? -eq 1 ]; then
    echo "\nERROR: Exiting MIDAS..."
    exit 1
fi

if [[ $1 == "-b" ]]; then

    # If running on wetty, then upload the project to build server
    if [[ $is_wetty == true ]]; then
        
        # echo "Uploading the project to build server..."
        curl --location "http://$GS:5000/api/instance/sync_files" \
        --header "Content-Type: application/json" \
        --data '{
            "key": "'"$orchestra_key"'",
            "username": "'"$USER"'"
        }'

        dirname=$(basename "$PWD")

        curl --location 'http://$GS:5000/api/greyfish/users/sanjeeth/run_midas' \
                --header 'Content-Type: application/json' \
                --data '{
                    "key":"'"$orchestra_KEY"'",
                    "project_dir":"'"home/gib/$PWD"'",
                }
                '

        echo "Build job is submitted. Please check your email for the results."

    # If running locally, then build the project locally
    else
        # Step 2
        echo "\nBuilding your Docker Image..."
        docker build -t my_image -f Dockerfile . # Builds docker image
        image_id=`docker image inspect --format='{{.Id}}' my_image| cut -d ':' -f 2`

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
    fi
   
else
    echo ""
fi




echo "\nMIDAS execution complete! Please feel free to leave us a constructive review.\n"
