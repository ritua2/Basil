Welcome to the Basil training. 

This training has been designed to help you understand the basics of Basil and how to use it to generate Docker and Singularity images of your applications. The training is divided into 5 levels with increasing level of complexity. Each module has a README file that explains the concepts and a hands-on exercise to practice the concepts. The training is designed to be self-paced. Please feel free to ask any questions related to Basil.

Requirements:
* You should have a basic understanding of Linux commands.
* You should have the instructions for building your code.
* You should have Docker or Singularity installed on your machine for using the Basil images generated using the Basil (https://icompute.us ) web-portal.

Note: We do not support generating images on top of Mac OS/Windows OS base images. You can run an Ubuntu container on a Mac/Windows system to do the training. To run an Ubuntu container, run the command below after replacing <PATH_TO_BASIL_TRAINING_DIRECTORY> with the path to the basil training directory.
```bash
docker run -it --rm -v <PATH_TO_BASIL_TRAINING_DIRECTORY>:/training ubuntu
```

# Contents
* This directory is structured as follows:
```bash
.
├── LEVEL0
│   ├── README.md
│   ├── solution
│   │   └── setup.sh
│   └── src
│       └── hellobasil.py
├── LEVEL1
│   ├── README.md
│   ├── requirements.txt
│   ├── solution
│   │   └── setup.sh
│   └── src
│       └── webapp.py
├── LEVEL2
│   ├── README.md
│   └── src
│       └── webapp.py
├── LEVEL3
│   ├── README.md
│   ├── solution
│   └── src
│       └── donut.c
├── LEVEL4
│   ├── README.md
│   └── src
├── LEVEL5
│   └── README.md
└── README.md
```
