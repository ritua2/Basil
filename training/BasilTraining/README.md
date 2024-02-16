Welcome to Basil training. 

This training has been designed to help you understand the basics of Basil and how to use it to containerize your applications into docker and singularity images. The training is divided into 5 levels with increasing level of complexity. Each module has a README file that explains the concepts and a hands-on exercise to practice the concepts. The training is designed to be self-paced and you can take as much time as you need to complete the training. If you have any questions, feel free to ask the instructor. Enjoy the training!

Requirements:
* You should have a basic understanding of Linux commands.
* You should have a basic understanding of programming language.
* You should have Docker and Singularity installed on your machine.

Note: If you are working on Mac/Windows machine, we don't support MacOS/WindowsOS base images. To work on the training, you can run a ubuntu container and work on the training. To run a ubuntu container, run this command. Replace <PATH_TO_BASIL_TRAINING_DIRECTORY> with the path to the basil training directory.
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
