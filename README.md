# Flask API Template
`Author: Jan Peter Merkel `

# Content:
  1. [Scope](#1-scope)
  2. [Folder Structure](#2-folder-structure)
  3. [Available Routes](#3-available-routes)
  4. [Development Environment Setup](#4-development-environment-setup)
  5. [Application Deploy](#5-application-deploy)

### Minimum requirements:
To run this application you should have the following dependencies on your machine:
 - [Python](https://www.python.org/downloads/)
 - [Docker](https://www.docker.com/products/docker-desktop/)

 **Note:** Ensure pip is also instaled and available on your PATH.



# 1. Scope:
The scope of this repository is to be a template for a minimal Flask API. Covering basic routes, folder structure and containerization.
It also aims to standarize the documentation for future projects with a similar basis.

# 2. Folder Structure

```
TO DO...
```

# 3. Available Routes
TO DO...

# 4. Development Environment Setup

## 4.2 How to generate a requirements.txt file
Requirements.txt is a file that has all the dependencies needed to run our application, this file is not generated by hand. It can be generated automatically with the following command:

`pipreqs .`

If the execution was successfull you should see a new file named `requirements.txt`

## 4.3 How to build a Docker Image
For building a docker image we run the following command

`docker build -t <your_application_name> .`

example:

`docker build -t rest_api .`

## 4.4 Running your Docker Image as a container
After building your Image you can run it as a container with the following command

`docker run -d -p <your_pc_port>:<container_port> <your_application_name>`

example:

`docker run -d -p 5001:5000 rest_api`

The command above has two arguments:

 - -d : This tells docker to run in detached mode, it doesn't lock your terminal while running the application.

 - -p: this tells docker to bind your computer port on the containers port.

 After running the command above the application should be accessible on `http://localhost:5001/`

## 4.5 Killing the application
After running your application, list the containers running with:
`docker ps`

the expected output should be:

```
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                    NAMES
1fe244221799   rest_api   "python3 -m flask ru…"   6 seconds ago   Up 5 seconds   0.0.0.0:5
```

Then you can kill the application with the first Container ID letters as bellow:

`docker kill 1fe`





# 5. Application Deploy
TO DO...

