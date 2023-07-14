# Webcounter
By André
Simple Python Webcounter with redis server

## Manual operations

### Build
    docker build -t palazzag/webcounter:latest .

### Dependencies
    docker run -d  --name redis --rm redis:alpine

### Run
    docker run -d --rm -p8000:5000 --name webcounter --link redis -e REDIS_URL=redis palazzag/webcounter:latest


## Docker Playground example

### Instal gitlab-runner

    sudo apk add gitlab-runner

### Gitlab register

gitlab-runner register -n \
--url https://gitlab.com/ \
--executor shell \
--description "docker-palazzag" \
--tag-list "develop" \
--registration-token GR1348941KAhwZxv_Urp5TjKzt6ep

### Run runner

    gitlab-runner run

## Server Operations

### Install gitlab runner
https://www.fosstechnix.com/install-gitlab-runner-on-ubuntu-22-04-lts/

    curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh" | sudo bash

    sudo apt-get install gitlab-runner

    sudo usermod -a -G docker gitlab-runner

    sudo systemctl restart gitlab-runner

### Register gitlab-runner

    sudo gitlab-runner register -n \
        --url https://gitlab.com/ \
        --executor shell \
        --description "docker-cfreire" \
        --tag-list "develop,production" \
        --registration-token GR1348941KAhwZxv_Urp5TjKzt6ep

### Create a docker swarm cluster

    docker swarm init
    
### Monitor progress

    journalctl -f -u gitlab-runner