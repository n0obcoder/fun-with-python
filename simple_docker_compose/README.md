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

### How To Run

* Build the docker image first
  ```
  docker-compose up
  ```

* Start the service
  ```
  docker-compose up
  ```

* Build and Start in the same line of code
  ```
  docker-compose up --build
  ```

<strong>NOTE:</strong> If you make some changes in the Dockerfile then to bring the changes into effect, you must re-build the docker image. This can either be done by using the command for building the  image and then starting the service or by simply using the <b>'up'</b> command along with the <b>--build</b> flag.  
