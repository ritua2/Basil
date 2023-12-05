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
        read -p "Would you like to upload the image to the registry? (yes/no): " upload_img_hub

        img_hub_username=""
        img_hub_token=""

        # Inform user about default behavior
        # Read the "midas.yml" file and extract the Image type
        image_type=$(grep "Image type:" midas.yml | awk -F"'" '{print $2}')

        if [[ $upload_img_hub == "yes" ]]; then

            # Check the Image type and perform actions accordingly
            if [ "$image_type" == "singularity" ]; then
                clear 
                echo "Get ready with your singularity container services username and token for the image to be uploaded to your account."
                echo ""
                echo "WARNING: Please do not enter any sensitive information other than your username and token."
                echo ""
                read -p "Enter your username: " img_hub_username
                echo ""
                read -p "Enter your singularity services token: " img_hub_token

            elif [ "$image_type" == "docker" ]; then
                echo "Building your Docker Image..."
                clear 
                echo "Get ready with your dockerhub username and token in case you want the image to be uploaded to your account."
                echo ""
                echo "WARNING: Please do not enter any sensitive information other than your dockerhub username and token."
                echo ""
                echo "You can skip providing username & token details if you want the image to be uploaded to the basil project's dockerhub account."
                echo ""
                read -p "Enter your DockerHub username: " img_hub_username
                # If username is provided, ask for token or use default values
                if [[ -n $img_hub_username ]]; then
                    read -p "Enter your DockerHub token: " img_hub_token
                else
                    echo ""
                    echo "No username provided. The image will be uploaded to the default DockerHub account."
                    img_hub_username="basilproject"
                    img_hub_token="default_token"
                fi
            fi

        fi

        # echo "Uploading the project to build server..."
        output=$(curl --location "http://$GS:5000/api/instance/sync_files" \
        --header "Content-Type: application/json" \
        --data "{
            \"key\": \"$orchestra_key\",
            \"username\": \"$USER\"
        }")

        dirname=$(basename "$PWD")

        output=$(curl --location "http://$GS:5000/api/greyfish/users/$USER/run_midas" \
        --header "Content-Type: application/json" \
        --data "{
            \"key\": \"$orchestra_key\",
            \"project_dir\": \"home/gib$PWD\",
            \"img_hub_uid\": \"$img_hub_username\",
            \"img_hub_token\": \"$img_hub_token\",
            \"publish\": \"$upload_img_hub\",
            \"img_type\": \"$image_type\"
        }")


        echo "Build job is submitted. Please check your email for the results."
        echo ""

    # If running locally, then build the project locally
    else
        # Read the "midas.yml" file and extract the Image type
        image_type=$(grep "Image type:" midas.yml | awk -F"'" '{print $2}')

        # Check the Image type and perform actions accordingly
        if [ "$image_type" == "singularity" ]; then
            echo "Performing actions for Singularity"
            singularity build singularity_image.sif singularity.def
            singularity run singularity_image.sif
        elif [ "$image_type" == "docker" ]; then
            echo "Building your Docker Image..."
            docker build -t my_image -f Dockerfile . # Builds docker image
            image_id=`docker image inspect --format='{{.Id}}' my_image| cut -d ':' -f 2`

            echo "Image ID: $image_id"

            echo "Running SNYK analysis for your image..."
            echo "Image ID: $image_id"

            bash $script_dir/snyktest.sh $image_id

            echo "Running your Docker image..."
            docker run my_image
        else
            echo "Error: Unknown image type"
        fi

        
    fi
   
else
    echo ""
fi



echo ""
echo "Basil execution completed! Please feel free to leave us a constructive review."
