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

        declare -A options=(
            [501339]="Agriculture, Forestry, and Fisheries"
            [501342]="Agriculural Biotechnology"
            [501386]="Analytical and Materials Chemistry"
            [501340]="Animal and Dairy Science"
            [501369]="Applied Computer Science"
            [501365]="Applied Mathematics"
            [501371]="Artificial Intelligence and Intelligent Systems"
            [501356]="Arts"
            [501375]="Astronomy and Planetary Sciences"
            [501388]="Atmospheric Sciences"
            [501378]="Atomic, Molecular, and Optical Physics"
            [501334]="Basic Medicine"
            [501404]="Behavioral Sciences Biology"
            [501397]="Biochemistry and Molecular Biology"
            [501396]="Biophysics"
            [501398]="Cell Biology"
            [501326]="Chemical Engineering"
            [501323]="Civil Engineering"
            [501389]="Climate and Global Dynamics"
            [501335]="Clinical Medicine"
            [501368]="Computer Science"
            [501376]="Condensed Matter Physics"
            [501400]="Developmental Biology"
            [501402]="Ecology"
            [501345]="Economics and Business"
            [501346]="Educational Sciences"
            [501324]="Electrical, Electronic, and Information Engineering"
            [501403]="Environmental Biology"
            [501330]="Environmental Biotechnology"
            [501329]="Environmental Engineering"
            [501381]="Fluid and Plasma Physics"
            [501399]="Genetics"
            [501392]="Geology and Solid Earth Sciences"
            [501391]="Geophysics and Geochemistry"
            [501377]="Gravitational Physics"
            [501336]="Health Sciences"
            [501353]="History and Archaeology"
            [501394]="Hydrology and Water Resources"
            [501331]="Industrial Biotechnology"
            [501373]="Informatics, Analytics and Information Science"
            [501361]="Infrastructure and Instrumentation"
            [501385]="Inorganic and Nuclear Chemistry"
            [501354]="Languages and Literature"
            [501348]="Law"
            [501390]="Magnetospheric and Upper Atmospheric Physics"
            [501327]="Materials Engineering"
            [501325]="Mechanical Engineering"
            [501351]="Media and communications"
            [501337]="Medical Biotechnology"
            [501328]="Medical Engineering"
            [501332]="Nanotechnology"
            [501379]="Nuclear Physics"
            [501393]="Oceanography and Ocean Sciences"
            [501384]="Organic Chemistry"
            [501363]="Other"
            [501343]="Other Agricultural Sciences"
            [501405]="Other Biological Sciences"
            [501387]="Other Chemical Sciences"
            [501374]="Other Computer and Information Sciences"
            [501395]="Other Earth and Environmental Sciences"
            [501333]="Other Engineering and Technologies"
            [501367]="Other Mathematics"
            [501338]="Other Medical Sciences"
            [501322]="Other Natural Sciences"
            [501382]="Other Physical Sciences"
            [501357]="Other humanities"
            [501352]="Other social sciences"
            [501380]="Particle and High-Energy Physics"
            [501360]="Performance Evaluation and Benchmarking"
            [501355]="Philosophy, Ethics, and Religion"
            [501383]="Physical Chemistry"
            [501349]="Political Science"
            [501344]="Psychology"
            [501364]="Pure Mathematics"
            [501362]="Science and Engineering Education"
            [501350]="Social and Economic Geography"
            [501347]="Sociology"
            [501370]="Software Engineering, Systems, and Development"
            [501359]="Staff Activities "
            [501366]="Statistics and Probability"
            [501401]="Systematics and Population Biology"
            [501358]="Training"
            [501341]="Veterinary Science"
            [501372]="Visualization and Human-Computer Systems"
    )

    selected_tags=()

    for index in "${!options[@]}"
    do
        echo "$index: ${options[$index]}"
    done

    echo "Select your tags by entering the index numbers (separated by commas), or press ENTER to finish:"
    while :
    do
        read -p "Enter index number(s): " user_input
        if [ -z "$user_input" ]; then
            break
        fi

        IFS=',' read -ra selected_indices <<< "$user_input"
        for idx in "${selected_indices[@]}"
        do
            if [ ${options[$idx]+_} ]; then
                selected_ids+=("$idx")
                selected_tags+=("${options[$idx]}")
            fi
        done
    done


        # Remove duplicates from selected IDs
        selected_ids=($(printf "%s\n" "${selected_ids[@]}" | awk '!seen[$0]++'))

        echo "Selected IDs :"
        for id in "${selected_ids[@]}"
        do
            echo "$id"
        done


        selected_ids_str=$(IFS=,; echo "${selected_ids[*]}")


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
            \"img_type\": \"$image_type\",
            \"meta_options\": \"$selected_ids_str\",
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
