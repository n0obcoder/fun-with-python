## 02_docker_compose_django
 
This is a very simple example of how <strong>docker-compose</strong> can be used with <strong>docker</strong> to run a  <strong>django application</strong> (a service) automatically.
 
### Requirements
* docker         (apt-get install docker)   
* docker-compose (apt-get install docker-compose)

### Dockerfile
File containing the information about the docker image to be built
 
### requirements.txt
A text file containing the list of all the pythi packages to be installed in the docker container
 
### docker-compose.yml
This uses the Dockefile to build the docker image and run the django application in th container 

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

<strong>NOTE:</strong> If you make some changes in the Dockerfile then to bring the changes into effect, you must re-build the docker image. This can either be done by using the command for building the  image and then starting the service or by simply using the <b>up</b> command along with the <b>--build</b> flag.  
