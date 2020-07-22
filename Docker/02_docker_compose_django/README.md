## 02_docker_compose_django
 
This is a very simple example of how <strong>docker-compose</strong> can be used with <strong>docker</strong> to run a  <strong>django application</strong> (a service) automatically.
 
### Requirements
* docker         (apt-get install docker)   
* docker-compose (apt-get install docker-compose)

### Files and their Functionns

* ### Dockerfile
  File containing the information about the docker image to be built
 
* ### requirements.txt
  A text file containing the list of all the pythi packages to be installed in the docker container
 
* ### docker-compose.yml
  This uses the Dockefile to build the docker image and run the django application in th container 

### How To Run

* Build the docker image first
  ```
  docker-compose up
  ```

* Make a Django project 
  ```
  docker-compose run <service_name> <bash commmand>
  ```
  or
  ```
  docker-compose run django_webapp django-admin startproject my_webapp
  ```
  where <br>
  <strong>django_webapp</strong> (in docker-compose.yml) is the name of the service,<br>
  <strong>my_webapp</strong> is the name of the django project, and  <br>
  <strong>/usr/src/django_app_dir</strong> (in docker-compose.yml) is the the path of the directory to which the local machine's volume would be mounted in the docker container

* Start the service
  ```
  docker-compose up
  ```

* Go to http://localhost:7575/ and see the Django web app in action !
<hr>
<strong>NOTE:</strong> If you make some changes in the Dockerfile then to bring the changes into effect, you must re-build the docker image. This can be done by using the command for building the  image and then starting the service up.  
