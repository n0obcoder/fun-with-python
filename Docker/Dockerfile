# Parent Image
FROM ubuntu:18.04

# Prints a text while building the Dockerfile
RUN echo n0obcode \
-a misnomer

# https://phoenixnap.com/kb/how-to-install-python-3-ubuntu
###

# use of apt-get is preferred over apt
# -y automaticlly picks YES from [YES|NO]
# these 2 things must be kept in mind while using apt in a script

# Update and Refresh Repository Lists
RUN apt-get -y update && apt-get -y upgrade 

# Install Supporting Software
# The software-properties-common package gives you better control over your package manager by letting you add PPA (Personal Package Archive) repositories. Install the supporting software with the command: 
RUN apt-get -y install software-properties-common

# Add Deadsnakes PPA
# Deadsnakes is a PPA with newer releases than the default Ubuntu repositories. Add the PPA by entering the following:
RUN add-apt-repository ppa:deadsnakes/ppa

# The following line of code fixes the bugs that would otherwise occur while importing cv2
RUN apt-get install -y libsm6 libxext6 libxrender-dev

# Install nano
RUN apt-get install nano

# Install curl
RUN apt-get -y install curl

# Install screen 
RUN apt-get -y install screen 

# Install python 3.8
RUN apt-get -y install python3.8

# Install pip3
RUN apt-get -y install python3-pip

# Install Git
RUN apt-get -y install git
###

# COPY adds files from your Docker client’s current directory.
COPY . /app

# Change working directory
WORKDIR /app

# Install python packages using pip3
RUN pip3 install -r requirements.txt

# Git Clone a repo
RUN git clone https://github.com/n0obcoder/dukaan.git

# Run a python script to print something out in the terminal
#CMD python3 /app/this.py
