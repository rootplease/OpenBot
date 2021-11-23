FROM ubuntu:latest
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive 
RUN apt-get install git python3 python3-dev python3-pip wget curl sudo -y
RUN useradd -rm -d /home/dev -s /bin/bash -g root -G sudo -u 1000 dev
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER dev
WORKDIR /home/dev
ENV TZ=America/Los_Angeles
RUN sudo ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
RUN sudo pip install pre-commit
