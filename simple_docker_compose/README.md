## Simple docker-compose
 
This is a very simple example of how docker-compose can be used to run different services.
 
### Requirements
* docker         (apt-get install docker)   
* docker-compose (apt-get install docker-compose)

### Dockerfile
File containing the information about the docker image to be built
 
### hellp.py
A python script that would be run automatically (using docker-compose command) after the docker image is built
 
### docker-compose.yml
This uses the Dockefile and hello.py to first, build the docker image and then run the python script 
