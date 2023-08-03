#!/bin/bash

echo "Welcome to Project Basil!\n"

script_dir="$(cd "$(dirname "$0")" && pwd)"

python3 $script_dir/interactive.py

# CHECK IF ABOVE COMMAND EXITED WITH ERROR CODE
if [ $? -eq 1 ]; then
    echo "ERROR: Exiting MIDAS..."
    exit 1
fi

echo "Generating Dockerfile..."

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

        # ask if user want to upload to dockerhub
        read -p "Would you like to upload built docker image to DockerHub? (yes/no): " upload_dockerhub

        dockerhub_username=""
        dockerhub_token=""
        # ask for username and token if they want to upload to their dockerhub account or let them know by default it will be uploaded to our dockerhub
        echo "Please note that by default, the built docker image will be uploaded to our DockerHub account."
        echo "If you would like to upload to your DockerHub account, please enter your username and token below."
        if [[ $upload_dockerhub == "yes" ]]; then
            read -p "Enter your DockerHub username: " dockerhub_username
            read -p "Enter your DockerHub token: " dockerhub_token
        fi
        
        # echo "Uploading the project to build server..."
        curl --location "http://$GS:5000/api/instance/sync_files" \
        --header "Content-Type: application/json" \
        --data "{
            \"key\": \"$orchestra_key\",
            \"username\": \"$USER\"
        }"


        dirname=$(basename "$PWD")

        curl --location "http://$GS:5000/api/greyfish/users/sanjeeth/run_midas" \
        --header "Content-Type: application/json" \
        --data "{
            \"key\": \"$orchestra_key\",
            \"project_dir\": \"home/gib/$PWD\",
            \"docker_uid\": \"$dockerhub_username\",
            \"docker_token\": \"$dockerhub_token\",
            \"publish\": \"$upload_dockerhub\"
        }"


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
