Welcome to the Basil training. 

This training has been designed to explain the basics of Basil and how to use it in a stand-alone environment and also on the icompute.us web-portal to generate Docker and Singularity images. The training is divided into 5 levels with increasing level of complexity. Each module has a README file that explains the concepts and a hands-on exercise to practice the concepts. The training is designed to be self-paced and one can take as much time as you need to complete the training. 

Requirements:
* You should have a basic understanding of Linux commands.
* You should have a basic understanding of a programming language.
* You should have Docker and Singularity installed on the system on which you would like to run the Docker/Singularity images generated by basil.

Note for Windows/Mac users: We do not support MacOS/WindowsOS base images. To work on the training, you can run an Ubuntu container and work on the training. To run an Ubuntu container, run the command below after replacing <PATH_TO_BASIL_TRAINING_DIRECTORY> with the path to the basil training directory.
```bash
docker run -it --rm -v <PATH_TO_BASIL_TRAINING_DIRECTORY>:/training ubuntu
```

# Contents
* This directory is structured as follows:
```bash
.
├── LEVEL0
│   ├── README.md
│   ├── solution
│   │   └── setup.sh
│   └── src
│       └── hellobasil.py
├── LEVEL1
│   ├── README.md
│   ├── requirements.txt
│   ├── solution
│   │   └── setup.sh
│   └── src
│       ├── templates
│       │   └── home.html
│       └── webapp.py
├── LEVEL2
│   ├── README.md
│   ├── requirements.txt
│   ├── solution
│   │   └── setup.sh
│   └── src
│       ├── templates
│       │   ├── home.html
│       │   └── image.html
│       └── webapp.py
├── LEVEL3
│   ├── README.md
│   ├── solution
│   │   └── setup.sh
│   └── src
│       └── donut.c
├── LEVEL4
│   ├── README.md
│   └── setup.sh
├── LEVEL5
│   └── README.md
└── README.md
```
