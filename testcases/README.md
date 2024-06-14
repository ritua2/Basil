# Test Cases for Basil

This folder contains some of the test cases that will be used for testing Basil's code generation and optimization capabilities.


### OpenSees Image URI:
* docker: basilproject/basil_sanjeethboddigm_1708638505:latest
        ```
        docker pull basilproject/basil_sanjeethboddigm_1708638505:latest
        docker run -it -v .:/opensees_files basilproject/basil_sanjeethboddigm_1708638505:latest

        # inside the container 
        cd /root/OpenSees/build/bin
        ./OpenSees /opensees_files/Truss.tcl
        mpirun -np 4 --allow-run-as-root ./OpenSeesSP /opensees_files/test_opensees_sp/Example.tcl
        mpirun -np 4 --allow-run-as-root ./OpenSeesMP /opensees_files/test_opensees_mp/Example.tcl
        ```

* singularity: library://sanjeethboddi/opensees/basil-1708643000:1.0.0
        ```
        singularity pull library://sanjeethboddi/opensees/basil-1708643000:1.0.0
        singularity run --fakeroot --no-home -e --bind .:/results --writable basil-1708643000_1.0.0.sif

        # inside the container
        cd /root/OpenSees/build/bin
        ./OpenSees /opensees_files/Truss.tcl
        mpirun -np 4 --allow-run-as-root ./OpenSeesSP /opensees_files/test_opensees_sp/Example.tcl
        mpirun -np 4 --allow-run-as-root ./OpenSeesMP /opensees_files/test_opensees_mp/Example.tcl
        ```

### Jetscape Image URI:
* docker: basilproject/basil_sanjeethboddigm_1708707206:latest
        ```
        docker pull basilproject/basil_sanjeethboddigm_1708707206:latest
        docker run --rm --name jetscape -it basilproject/basil_sanjeethboddigm_1708707206:latest

        # inside the container
        cd JETSCAPE/build/
        ./runJetscape
        ```

* singularity: library://sanjeethboddi/jetscapee/basil-1708708195:1.0.0
        ```
        singularity pull library://sanjeethboddi/jetscapee/basil-1708708195:1.0.0
        singularity run --fakeroot --no-home -e --bind .:/results --writable basil-1708708195_1.0.0.sif

        # inside the container
        cd JETSCAPE/build/
        ./runJetscape
        ```

### AutoDockVina Image URI:
* docker: basilproject/basil_sanjeethboddigm_1709312775:latest
    ```
    docker pull basilproject/basil_sanjeethboddigm_1709312775:latest
    docker run --rm --name autodockvina -it basilproject/basil_sanjeethboddigm_1709312775:latest
    ```
* singularity: library://sanjeethboddi/manual/basil-1709318629:1.0.0 
    ```
    singularity pull library://sanjeethboddi/manual/basil-1709318629:1.0.0 
    singularity run --fakeroot --no-home -e --writable library://sanjeethboddi/manual/basil-1709318629:1.0.0
    ```

### OSU Micro-Benchmarks Image URI:
* docker: basilproject/basil_sanjeethboddigm_1709313258:latest
    ```
    docker pull basilproject/basil_sanjeethboddigm_1709313258:latest
    docker run --rm --name osu-micro-benchmarks -it basilproject/basil_sanjeethboddigm_1709313258:latest
    ```
* singularity: 
    ```
    singularity pull 
    singularity run --fakeroot --no-home -e --writable 
    ```

### Blast Image URI:
* docker: basilproject/basil_sanjeethboddigm_1709315246:latest
    ```
    docker pull basilproject/basil_sanjeethboddigm_1709315246:latest
    docker run --rm --name blast -it basilproject/basil_sanjeethboddigm_1709315246:latest
    ```
* singularity: 
    ```
    singularity pull library://sanjeethboddi/manual/basil-1709319652:1.0.0
    singularity run --fakeroot --no-home -e --writable library://sanjeethboddi/manual/basil-1709319652:1.0.0
    ```


### LAMPPS Image URI: 
* docker: basilproject/basil_sanjeethboddigm_1709313975:latest
    ```
    docker pull basilproject/basil_sanjeethboddigm_1709313975:latest
    docker run --rm --name lammps basilproject/basil_sanjeethboddigm_1709313975:latest
    ```
* singularity: 
    ```
    singularity pull 
    singularity run --fakeroot --no-home -e --writable
    ```


### REDIAL Image URI:
* docker: basilproject/basil_sanjeethboddigm_1709251331:latest
    ```
    docker pull basilproject/basil_sanjeethboddigm_1709251331:latest
    docker run --rm --name basil_sanjeethboddigm_1709251331 -v $(pwd):/results --env input_file=sample_data.csv basilproject/basil_sanjeethboddigm_1709251331:latest
        ```
* singularity: library://sanjeethboddi/redial/basil-1709242030:1.0.0
    ```
    singularity pull library://sanjeethboddi/redial/basil-1709242030:1.0.0
    singularity run --fakeroot --no-home -e --bind .:/results --writable --env input_file=sample_data.csv basil-1709242030_1.0.0.sif
    ```

### LIGANDNET Image URI: 
* docker: basilproject/basil_sanjeethboddigm_1709246618:latest
    ```
    docker pull basilproject/basil_sanjeethboddigm_1709246618:latest
    docker run --rm --name basil_sanjeethboddigm_1709246618 -v $(pwd):/LigandNet/results --env smile=CCCC basilproject/basil_sanjeethboddigm_1709246618:latest
    ```
* singularity: library://basiltemp/ligandnet/basil-1709245541:1.0.0
    ```
    singularity pull library://basiltemp/ligandnet/basil-1709245541:1.0.0 # unable to pull the image
    singularity run --fakeroot --no-home -e --bind .:/LigandNet/results --env smile=CCCC basil-1709245541_1.0.0.sif
    ```
### OpenDMPK Image URI:
* docker: basilproject/basil_sanjeethboddigm_1709253069:latest
    ```
    docker pull basilproject/basil_sanjeethboddigm_1709253069:latest
    docker run --rm --name basil_sanjeethboddigm_1709253069 -v $(pwd):/OpenDMPK/results --env smile=CCCC basilproject/basil_sanjeethboddigm_1709253069:latest
    ```
* singularity: library://sanjeethboddi/opendmpk/basil-1709248912:1.0.0
    ```
        singularity pull singularity pull library://sanjeethboddi/opendmpk/basil-1709248912:1.0.0
        singularity run --fakeroot --no-home -e  --writable --env smile=CCCC basil-1709248912_1.0.0.sif
    ```

### BiasNet Image URI:
* docker: basilproject/basil_sanjeethboddigm_1712843728:latest
    ```
    docker pull basilproject/basil_sanjeethboddigm_1712843728:latest
    docker run --rm --name basil_sanjeethboddigm_1712843728 --env smile=CCCC basilproject/basil_sanjeethboddigm_1712843728:latest
    ```
* singularity: library://sanjeethalt/biasnet/basil-1712846389:1.0.0
    ```
        singularity pull library://sanjeethalt/biasnet/basil-1712846389:1.0.0
        singularity run --fakeroot --no-home -e  --writable --env smile=CCCC basil-1712846389_1.0.0.sif
    ```

### Sumo Image URI:
* docker: basilproject/basil_hr1335wa_1718398088:latest
    ```
    docker pull basilproject/basil_hr1335wa_1718398088:latest

    # disable xhost acl
    xhost +

    # run net edit
    docker run -it --rm \
        -e DISPLAY -u `id -u` \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        -v /etc/localtime:/etc/localtime:ro \
        --name sumo \
        basilproject/basil_hr1335wa_1718398088:latest sumo/bin/netedit
    
    # run sumo gui
    docker run -it --rm \
        -e DISPLAY -u `id -u` \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        -v /etc/localtime:/etc/localtime:ro \
        --name sumo \
        basilproject/basil_hr1335wa_1718398088:latest sumo/bin/sumo-gui
        
    # enable back xhost acl
    xhost -
    ```
* singularity: library://baseswe99/sumo/basil-1718400424:1.0.0
    ```
    singularity pull library://baseswe99/sumo/basil-1718400424:1.0.0

    # disable xhost acl
    xhost +

    # run net edit
    singularity exec --no-home \
                 --env DISPLAY=$DISPLAY \
                 -B /tmp/.X11-unix:/tmp/.X11-unix \
                 basil-1718400424_1.0.0.sif sumo/bin/netedit
    
    # run sumo gui
    singularity exec --no-home \
                 --env DISPLAY=$DISPLAY \
                 -B /tmp/.X11-unix:/tmp/.X11-unix \
                 basil-1718400424_1.0.0.sif sumo/bin/netedit
        
    # enable back xhost acl
    xhost -
    ```



    