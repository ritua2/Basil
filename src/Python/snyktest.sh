#!/bin/bash

#image_id=$(docker image list | awk 'NR>1{print $3}' | head -n 2 | tail -n 1)
image_id=$1
echo "Image ID: $image_id"

read -p "Would you like to work in Batch Mode or Interactive Mode? Please enter 1 for Batch and 2 for Interactive Mode: " option

if [[ "$option" == "1" ]]; then
  # Batch mode
  echo -e "\nYou are now running Batch Mode, more features coming soon..."

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
