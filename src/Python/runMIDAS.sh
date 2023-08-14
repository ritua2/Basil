#!/bin/bash

echo "Welcome to Project Basil!"
echo ""

script_dir="$(cd "$(dirname "$0")" && pwd)"

python3 $script_dir/interactive.py

# CHECK IF ABOVE COMMAND EXITED WITH ERROR CODE
if [ $? -eq 1 ]; then
    echo "ERROR: Exiting Basil..."
    exit 1
fi

echo "Generating Dockerfile..."

# Step 1
python3 $script_dir/MIDAS.py

# CHECK IF ABOVE COMMAND EXITED WITH ERROR CODE
if [ $? -eq 1 ]; then
    echo "ERROR: Exiting Basil..."
    exit 1
fi

if [[ $1 == "-b" ]]; then

    # If running on wetty, then upload the project to build server
    if [[ $is_wetty == true ]]; then

        # ask if user want to upload to dockerhub
        read -p "Would you like to upload the built Docker image to DockerHub? (yes/no): " upload_dockerhub

        dockerhub_username=""
        dockerhub_token=""


        # Ask for username and token only if user wants to upload

        if [[ $upload_dockerhub == "yes" ]]; then
            # Inform user about default behavior
            clear 
            echo "Get ready with your dockerhub username and token in case you want the image to be uploaded to your account."
            echo ""
            echo "WARNING: Please do not enter any sensitive information other than your dockerhub username and token."
            echo ""
            echo "You can skip providing username & token details if you want the image to be uploaded to the basil project's dockerhub account."
            echo ""
            read -p "Enter your DockerHub username: " dockerhub_username

            # If username is provided, ask for token or use default values
            if [[ -n $dockerhub_username ]]; then
                read -p "Enter your DockerHub token: " dockerhub_token
            else
                echo ""
                echo "No username provided. The image will be uploaded to the default DockerHub account."
                dockerhub_username="basilproject"
                dockerhub_token="default_token"
            fi
        fi


        
        # echo "Uploading the project to build server..."
        output = curl --location "http://$GS:5000/api/instance/sync_files" \
        --header "Content-Type: application/json" \
        --data "{
            \"key\": \"$orchestra_key\",
            \"username\": \"$USER\"
        }"

        dirname=$(basename "$PWD")

        output = curl --location "http://$GS:5000/api/greyfish/users/$USER/run_midas" \
        --header "Content-Type: application/json" \
        --data "{
            \"key\": \"$orchestra_key\",
            \"project_dir\": \"home/gib$PWD\",
            \"docker_uid\": \"$dockerhub_username\",
            \"docker_token\": \"$dockerhub_token\",
            \"publish\": \"$upload_dockerhub\"
        }"


        echo "Build job is submitted. Please check your email for the results."
        echo ""

    # If running locally, then build the project locally
    else
        # Step 2
        echo "Building your Docker Image..."
        docker build -t my_image -f Dockerfile . # Builds docker image
        image_id=`docker image inspect --format='{{.Id}}' my_image| cut -d ':' -f 2`

        echo "Image ID: $image_id"
        # grep to get id, push int to snyk and run cmd

        # Step 3
        echo "Running SNYK analysis for your image..."
        echo "Image ID: $image_id"

        ## Run snyk test
        bash $script_dir/snyktest.sh $image_id


        # Step 4
        echo "Running your Docker image..."
        docker run my_image
    fi
   
else
    echo ""
fi



echo ""
echo "Basil execution completed! Please feel free to leave us a constructive review."
