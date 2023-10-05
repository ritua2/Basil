#!/bin/bash

# Get the first image ID from `docker image list`
image_id=$(docker image list | awk 'NR==2 {print $3}')
echo "Image ID: $image_id"

read -p "Would you like to work in Batch Mode or Interactive Mode? Please enter 1 for Batch and 2 for Interactive Mode: " option

if [[ "$option" == "1" ]]; then
  # Batch mode
  echo -e "\nYou are now running Batch Mode, hang on tight..."

  # Run snyk container test
  snyk container test sha256:$image_id > SNYKoutput.txt

  # Get listed recommendations
  recommendations_line=$(grep -n "Recommendations" SNYKoutput.txt | cut -d':' -f1)
  if [ -n "$recommendations_line" ]; then
    base_image=$(grep -o '^[^ ]*:[^ ]*' SNYKoutput.csv | grep -v "Base Image" | head -n1)
    if [ -n "$base_image" ]; then
      echo "Base image to upgrade: $base_image"
      echo -e "\nMajor upgrades found in the listed recommendations."
      echo -e "\nBase image changed to: $base_image"
        # Edit the Dockerfile with new base image
        sed -i "s/FROM .*/FROM $base_image/g" Dockerfile
        echo -e "\nDockerfile updated with new base image!"

    else
      echo "No base image found in the recommendations."
    fi

  else
    echo "No recommendations found."
  fi

elif [[ "$option" == "2" ]]; then
  # Interactive mode
  echo -e "\nYou are now running Interactive Mode, hang on tight..."
  snyk container test sha256:$image_id > SNYKoutput.txt
  recommendations_line=$(grep -n "Recommendations" SNYKoutput.txt | cut -d':' -f1)
  if [ -n "$recommendations_line" ]; then
    grep -A "$((recommendations_line - 1))" "Recommendations" SNYKoutput.txt | awk '/^-+$/ { exit } { print }' > SNYKoutput.csv
    cat SNYKoutput.csv

    read -p "Would you like to change the base image to a different one? (Y/N): " change_base_image
    if [[ "$change_base_image" == "Y" || "$change_base_image" == "y" ]]; then

      # if YES
      read -p "Enter the new base image: " new_base_image
      echo -e "\nBase image changed to: $new_base_image"

      # Edit the Dockerfile with new base image
      sed -i "s/FROM .*/FROM $new_base_image/g" Dockerfile
      echo -e "\nDockerfile updated with new base image!"

    else
      echo "Base image remains unchanged."
    fi

  else
    echo "No recommendations found."
  fi

else
  echo "Invalid option. Please choose either 1 or 2."
fi
