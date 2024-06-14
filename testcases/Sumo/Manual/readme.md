
```Bash

## install mesa
# mac
brew install mesa
# ubuntu
sudo apt install mesa-utils


# export display (
# export DISPLAY=`hostname`:0 #WORKED IN MAC
# export DISPLAY=:1 #WORKED IN LINUX

# disable xhost acl
xhost +

# run docker image
docker run -it --rm \
    -e DISPLAY -u `id -u` \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /etc/localtime:/etc/localtime:ro \
    --name sumo \
    sumo bin/netedit
    
# run singularity image
singularity exec --no-home \
                 --env DISPLAY=$DISPLAY \
                 -B /tmp/.X11-unix:/tmp/.X11-unix \
                 sumo.sif sumo/bin/netedit


            

# enable back xhost acl
xhost -
            
```
